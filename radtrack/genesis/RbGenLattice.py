"""
Copyright (c) 2015 RadiaBeam Technologies. All rights reserved

classes for genesis propagation
"""

__author__ = 'swebb'

import numpy as np
from radtrack.genesis.rbGenLatFile import GenLatFile
from scipy import constants as consts
import operator

class GenLattice(object):
    """
    This class takes a list of elements recongized by Genesis -- undulators,
    quadrupoles, and drifts -- and plots the beta function across these
    elements. This is to be used to aid lattice design for FELs. It also can
    use the rbGenLatFile to generate a .lat file from the lattice
    it is storing.
    """

    def __init__(self, latticename='genesis_lattice'):

        self.list = []
        self.latticename = latticename


    def add_quadrupole(self, Kq, pos, length):
        """
        Adds a quadrupole to the lattice

        Args:
            Kq (float): Quadrupole strength in m^-2
            pos (float): Beginning position of the quadrupole
            length (float): The length of the quadrupole
        """
        # Add the quad to the list

        quadrupoleDict = {}
        quadrupoleDict['type'] = 'quadrupole'
        quadrupoleDict['Kq'] = Kq
        quadrupoleDict['pos'] = pos
        quadrupoleDict['length'] = length

        # Add the transfer map
        transfermap = np.zeros((4,4))
        Kl = np.sqrt(np.abs(Kq))*length
        if Kq > 0:
            transfermap[0,0] = np.cos(Kl)
            transfermap[0,1] = np.sin(Kl)/np.sqrt(np.abs(Kq))
            transfermap[1,0] = -np.sin(Kl)*np.sqrt(np.abs(Kq))
            transfermap[1,1] = np.cos(Kl)

            transfermap[2,2] = np.cosh(Kl)
            transfermap[2,3] = np.sinh(Kl)/np.sqrt(np.abs(Kq))
            transfermap[3,2] = np.sinh(Kl)*np.sqrt(np.abs(Kq))
            transfermap[3,3] = np.cosh(Kl)

        else:

            transfermap[0,0] = np.cosh(Kl)
            transfermap[0,1] = np.sinh(Kl)/np.sqrt(np.abs(Kq))
            transfermap[1,0] = np.sinh(Kl)*np.sqrt(np.abs(Kq))
            transfermap[1,1] = np.cosh(Kl)

            transfermap[2,2] = np.cos(Kl)
            transfermap[2,3] = np.sin(Kl)/np.sqrt(np.abs(Kq))
            transfermap[3,2] = -np.sin(Kl)*np.sqrt(np.abs(Kq))
            transfermap[3,3] = np.cos(Kl)

        quadrupoleDict['map'] = transfermap

        self.list.append(quadrupoleDict)


    def add_undulator(self, aw, pos, length):
        """
        Adds an undulator to the lattice

        Args:
            aw (float): RMS undulator strength
            pos (float): Beginning position of the undulator
            length (float): The length of the undulator section
        """

        # Add the undulator to the list

        undulatorDict = {}
        undulatorDict['type'] = 'undulator'
        undulatorDict['aw'] = aw
        undulatorDict['pos'] = pos
        undulatorDict['length'] = length

        # Ignoring undulator focusing for now...
        transfermap = np.identity(4)
        transfermap[0,1] = length
        transfermap[2,3] = length
        undulatorDict['map'] = transfermap

        self.list.append(undulatorDict)


    def add_drift(self, pos, length):
        """
        Adds a drift section to the lattice

        Args:
            pos (float): Starting position of the drift
            length (float): The length of the drift
        """

        driftDict = {}
        driftDict['type'] = 'drift'
        driftDict['pos'] = pos
        driftDict['length'] = length

        transfermap = np.identity(4)
        transfermap[0,1] = length
        transfermap[2,3] = length
        driftDict['map'] = transfermap

        self.list.append(driftDict)


    def compute_beamline(self):
        """
        Compute the transfer matrix and Twiss parameters for the stored
        beamline.

        Returns:
            beta_x (float): Matched beta in x direction
            beta_y (float): Matched beta in y direction
            alpha_x (float): Matched alpha in x direction
            alpha_y (float): Matched alpha in y direction
            transfermap (array): 4x4 transfer matrix for the beamline
        """

        self.list.sort(key=operator.itemgetter('pos'))

        transfermap = np.identity(4)

        for elements in self.list:
            transfermap = np.dot(transfermap, elements['map'])

        phi_x = np.arccos(0.5*(transfermap[0,0] + transfermap[1,1]))
        phi_y = np.arccos(0.5*(transfermap[2,2] + transfermap[3,3]))

        print 'phi_x =', phi_x
        print 'phi_y =', phi_y

        betax = (transfermap[0,1]/np.sin(phi_x))
        betay = (transfermap[2,3]/np.sin(phi_y))
        alphax = -0.5*(transfermap[0,0]-transfermap[1,1])/np.sin(phi_x)
        alphay = -0.5*(transfermap[2,2]-transfermap[3,3])/np.sin(phi_y)

        return betax, alphax, betay, alphay, transfermap


    def compute_beta_func(self):
        """
        Computes the beta function along the lattice currently stored by the
        class, assuming that this represents a unit cell of a lattice.

         Returns:
            betax_array (list): List of values of beta_x
            betay_array (list): List of values of beta_y
            s_array (list): The s coordinates corresponding to the beta
            function arrays
        """

        self.list.sort(key=operator.itemgetter('pos'))

        betax, alphax, betay, alphay, transfermap = self.compute_beamline()
        gammax = (1.+alphax**2)/betax
        gammay = (1.+alphay**2)/betay
        twissx = np.array([betax, alphax, gammax])
        twissy = np.array([betay, alphay, gammay])
        betax_array = [betax]
        betay_array = [betay]
        s_position = [0.]

        for element in self.list:
            if element['type'] == 'quadrupole':
                map = element['map']
                Mtwiss = np.zeros((3,3))
                Mtwiss[0,0] = (map[0,0])**2
                Mtwiss[0,1] = -2.*map[0,0]*map[0,1]
                Mtwiss[0,2] = (map[0,1])**2
                Mtwiss[1,0] = -map[0,0]*map[1,0]
                Mtwiss[1,1] = map[0,0]*map[1,1]+map[0,1]*map[1,0]
                Mtwiss[1,2] = -map[0,1]*map[1,1]
                Mtwiss[2,0] = map[1,0]**2
                Mtwiss[2,1] = -2.*map[1,1]*map[1,0]
                Mtwiss[2,2] = (map[1,1])**2

                twissx = np.dot(Mtwiss, twissx)
                betax_array.append(twissx[0])

                Mtwiss[0,0] = (map[2,2])**2
                Mtwiss[0,1] = -2.*map[2,2]*map[2,3]
                Mtwiss[0,2] = (map[2,3])**2
                Mtwiss[1,0] = -map[2,2]*map[3,2]
                Mtwiss[1,1] = map[2,2]*map[3,3]+map[2,3]*map[3,2]
                Mtwiss[1,2] = -map[2,3]*map[3,3]
                Mtwiss[2,0] = map[3,2]**2
                Mtwiss[2,1] = -2.*map[3,3]*map[3,2]
                Mtwiss[2,2] = (map[3,3])**2

                twissy = np.dot(Mtwiss, twissy)
                betay_array.append(twissy[0])

                s_position.append(element['pos']+element['length'])

            # will need to add special behavior for undulator here
            else:
                ds = 0.001*element['length']
                my_position = 0.
                Mtwiss = np.identity(3)
                Mtwiss[0,1] = -2.*ds
                Mtwiss[0,2] = ds**2
                Mtwiss[1,2] = -ds
                while my_position < element['length']:
                    twissx = np.dot(Mtwiss, twissx)
                    twissy = np.dot(Mtwiss, twissy)
                    my_position += ds
                    betax_array.append(twissx[0])
                    betay_array.append(twissy[0])
                    s_position.append(element['pos']+my_position)
        return betax_array, betay_array, s_position


    def export_genesis_lattice(self, unit_length, gamma):
        """
        Generate a Genesis .lat file from the current lattice being stored.
        This is output to a text file Genesis can read.

        Note that I expect unit_length and gamma to disappear when a Genesis
        class that holds general simulation data gets created.

        Args:
            unit_length (float): The unit_length for Genesis, typically the
            wiggler period
            gamma (float): Relativistic gamma
        """

        elems_dict = {}
        # Populate each element with sequential three-arrays
        elems_dict['QF'] = []
        elems_dict['AW'] = []
        quad_pos = 0.
        undulator_pos = 0.
        for element in self.list:
            if element['type'] == 'quadrupole':
                # compute dB/dx from Kq
                dBdx = element['Kq']*gamma*consts.m_e*consts.c\
                         /consts.elementary_charge
                length = element['length']
                distance = element['pos'] - quad_pos
                quad_pos = element['pos'] + element['length']
                length = round(length/unit_length, 0)
                distance = round(distance/unit_length, 0)
                elems_dict['QF'].append(np.array([dBdx, length, distance]))
            elif element['type'] == 'undulator':
                aw = element['aw']
                length = element['length']
                distance = element['pos'] - undulator_pos
                undulator_pos = element['pos'] + element['length']
                length = round(length/unit_length, 0)
                distance = round(distance/unit_length, 0)
                elems_dict['AW'].append(np.array([aw, length, distance]))

        lattice_file = GenLatFile(self.latticename, elems_dict, unit_length)
        lattice_file.write_lat_file()