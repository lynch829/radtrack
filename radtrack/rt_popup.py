# -*- coding: utf-8 -*-
u"""Pop up window to enter params for a section of SRW.

:copyright: Copyright (c) 2015 Bivio Software, Inc.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from io import open

import collections
import enum

from radtrack.rt_qt import QtCore, QtGui

from pykern import pkcompat
from pykern import pkresource
from pykern import pkio
from pykern.pkdebug import pkdc, pkdp

from radtrack import RbUtility
from radtrack import rt_params
from radtrack import rt_qt

class Window(QtGui.QDialog):
    def __init__(self, defaults, params, file_prefix, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle(rt_qt.i18n_text(defaults.decl.label))
        self.setStyleSheet(pkio.read_text(pkresource.filename(file_prefix + '_popup.css')))
        self._form = Form(defaults, params, self)

    def get_params(self,):
        """Convert values in the window to "param" values"""
        return self._form._get_params()


class Form(object):
    BUTTON_HEIGHT = 30
    BUTTON_WIDTH = 120
    CHAR_HEIGHT = BUTTON_HEIGHT - 2
    CHAR_WIDTH = 6
    MARGIN_HEIGHT = 20
    MARGIN_WIDTH = 30

    def __init__(self, defaults, params, window):
        super(Form, self).__init__()
        self._defaults = defaults
        self._frame = QtGui.QWidget(window)
        self._layout = QtGui.QFormLayout(self._frame)
        self._layout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self._layout.setMargin(0)
        sizes = self._init_fields(params)
        self._init_buttons(window)
        self._set_geometry(sizes)

    def _get_params(self):
        def _num(d, w):
            # need type checking
            if w is None:
                return None
            v = w.text()
            if d.units:
                v = RbUtility.convertUnitsStringToNumber(v, d.units)
            return d.py_type(v)

        def _iter_children(parent_defaults):
            res = collections.OrderedDict()
            for df in parent_defaults.children.values():
                d = df.decl
                if df.children:
                    res[d.name] = _iter_children(df)
                    continue
                f = self._fields[d.name]
                w = f['widget']
                if issubclass(d.py_type, bool):
                    v = w.isChecked()
                elif isinstance(d.py_type, enum.EnumMeta):
                    v = d.py_type(w.itemData(w.currentIndex()).toInt()[0])
                elif issubclass(d.py_type, float) or issubclass(d.py_type, int):
                    v = _num(d, w)
                else:
                    raise AssertionError('bad type: ' + str(d.py_type))
                res[d.name] = v
            return res

        return pkdp(_iter_children(self._defaults))

    def _init_buttons(self, window):
        self._buttons = rt_qt.set_id(QtGui.QDialogButtonBox(window), 'standard')
        self._buttons.setCenterButtons(1)
        self._buttons.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        for b in self._buttons.buttons():
            b.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self._layout.addRow(self._buttons)
        QtCore.QObject.connect(
            self._buttons, QtCore.SIGNAL('accepted()'), window.accept)
        QtCore.QObject.connect(
            self._buttons, QtCore.SIGNAL('rejected()'), window.reject)

    def _init_fields(self, params):
        """Create widgets"""
        self._fields = {}
        res = {
            'num': 0,
            'max_value': 0,
            'max_label': 0,
        }

        def _label(d):
            qlabel = QtGui.QLabel(self._frame)
            l = rt_qt.i18n_text(d.label, qlabel)
            if len(l) > res['max_label']:
                res['max_label'] = len(l)
            return qlabel

        def _heading(qlabel):
            rt_qt.set_id(qlabel, 'heading')
            qlabel.setAlignment(QtCore.Qt.AlignCenter)
            self._layout.addRow(qlabel)

        def _value_widget(d, p):
            t = d.py_type
            if isinstance(t, enum.EnumMeta):
                widget = QtGui.QComboBox(self._frame)
                v = ''
                for e in t:
                    n = rt_qt.i18n_text(e.display_name)
                    widget.addItem(n, userData=e.value)
                    if len(n) > len(v):
                        v = n
                rt_qt.set_widget_value(d, p, widget)
            elif issubclass(t, bool):
                widget = QtGui.QCheckBox(self._frame)
                v = rt_qt.i18n_text(d.label, widget)
                rt_qt.set_widget_value(d, p, widget)
            else:
                widget = QtGui.QLineEdit(self._frame)
                v = rt_qt.set_widget_value(d, p, widget)
            return (widget, v)

        def _iter_children(parent_default, p):
            for df in parent_default.children.values():
                d = df.decl
                qlabel = _label(d)
                if df.children:
                    _heading(qlabel)
                    res['num'] += 1
                    widget = None
                    _iter_children(df, p[d.name])
                else:
                    rt_qt.set_id(qlabel, 'form_field')
                    (widget, value) = _value_widget(d, p[d.name])
                    self._layout.addRow(qlabel, widget)
                    if len(value) > res['max_value']:
                        res['max_value'] = len(value)
                self._fields[d.name] = {
                    'qlabel': qlabel,
                    'declaration': d,
                    'widget': widget,
                }
                res['num'] += 1

        _iter_children(self._defaults, params)
        return res

    def _set_geometry(self, sizes):
        g = QtCore.QRect(
            self.MARGIN_WIDTH,
            self.MARGIN_HEIGHT,
            2 * self.MARGIN_WIDTH + (sizes['max_label'] + sizes['max_value']) * self.CHAR_WIDTH,
            2 * self.MARGIN_HEIGHT + self.CHAR_HEIGHT * sizes['num'] + self.BUTTON_HEIGHT,
        )
        self._frame.setGeometry(g)
