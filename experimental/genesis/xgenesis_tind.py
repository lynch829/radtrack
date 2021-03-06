__author__ = 'swebb'

from radtrack.genesis.rbXGenesisTInd import RbXGenesisTInd

test_plotter = RbXGenesisTInd()

test_plotter.parse_output('ttf.out')
#test_plotter.set_ploterrors()

#test_plotter.set_semilog()

power, length = test_plotter.compute_saturation()
print 'Saturation Power =', power, 'Watts'
print 'Saturation Length =', length, 'meters'
test_plotter.plot_data('z', 'Power')
test_plotter.plot_data('z', 'Increment')
test_plotter.plot_data('z', 'Rad. Size')
test_plotter.plot_data('z', 'X Beam Size')
test_plotter.plot_data('z', 'Y Beam Size')