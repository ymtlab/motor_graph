# -*- coding: utf-8 -*-
import sys
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg

from motor_graph_calculate import motor_graph_calculate
from mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet("QMainWindow {background: 'white';}")

        # plotwidget setting
        def settings_plotwidget(plotwidget, bottom_label, left_label):
            plotwidget.setBackground("#FFFFFFFF")
            plotitem = plotwidget.plotItem
            plotitem.setLabels(bottom=bottom_label, left=left_label)
            plotitem.getAxis('bottom').setPen(pg.mkPen(color='#000000'))
            plotitem.getAxis('left').setPen(pg.mkPen(color='#000000'))
        
        settings_plotwidget(self.ui.plotwidget_ta,   't [sec]', 'a [m/ss]')
        settings_plotwidget(self.ui.plotwidget_tv,   't [sec]', 'v [m/s]')
        settings_plotwidget(self.ui.plotwidget_tx,   't [sec]', 'x [m]')
        settings_plotwidget(self.ui.plotwidget_trev, 't [sec]', 'rev [rpm]')

        # slider setting
        def settings_slider(widget, label_text, minimum, maximum, steps, defoult_value):
            widget.label.setText(label_text)
            widget.set_minimum(minimum)
            widget.set_maximum(maximum)
            widget.set_single_step(steps)
            widget.set_value(defoult_value)
        
        settings_slider(self.ui.acceleration, 'acceleration[m/ss]', 0.001, 30, 0.001, 10)
        settings_slider(self.ui.v_max, 'v_max[m/s]', 0.001, 10, 0.001, 1)
        settings_slider(self.ui.distance, 'distance[m]', 0.001, 3, 0.001, 0.6)
        settings_slider(self.ui.steps, 'steps', 1, 20, 1, 10)
        settings_slider(self.ui.decimals, 'decimals', 1, 10, 1, 6)
        settings_slider(self.ui.lead, 'ballscrew lead[mm]', 0.1, 60, 0.1, 10)

        u = self.ui
        for w in [u.acceleration, u.v_max, u.distance, u.steps, u.decimals, u.lead]:
            w.non_update = False
            w.double_spinbox.valueChanged.emit(w.double_spinbox.value())

    def update_plotwidget(self):
        try:
            # clear plotwidgets
            self.ui.plotwidget_ta.clear()
            self.ui.plotwidget_tv.clear()
            self.ui.plotwidget_tx.clear()
            self.ui.plotwidget_trev.clear()

            # get conditions
            acceleration = float( self.ui.acceleration.double_spinbox.value() )
            v_max = float( self.ui.v_max.double_spinbox.value() )
            distance = float( self.ui.distance.double_spinbox.value() )
            step = int( self.ui.steps.double_spinbox.value() )
            decimals = int( self.ui.decimals.double_spinbox.value() )

            # calculate
            t, a, v, x = motor_graph_calculate(acceleration, v_max, distance, step, decimals)

            # calculate revolution
            rev = [ np.round( vi * 1000.0 / self.ui.lead.double_spinbox.value() * 60.0, decimals ) for vi in v ]
            
            # plot
            pen = pg.mkPen(color='#000000', width=1)
            for ti, ai, vi, xi, revi in zip(t, a, v, x, rev):
                self.ui.plotwidget_ta.addItem( pg.PlotDataItem(x=ti, y=ai, pen=pen, antialias=True) )
                self.ui.plotwidget_tv.addItem( pg.PlotDataItem(x=ti, y=vi, pen=pen, antialias=True) )
                self.ui.plotwidget_tx.addItem( pg.PlotDataItem(x=ti, y=xi, pen=pen, antialias=True) )
                self.ui.plotwidget_trev.addItem( pg.PlotDataItem(x=ti, y=revi, pen=pen, antialias=True) )
            
            text  = 'V max = ' + str( max([max(vi) for vi in v]) ) +'\n'
            text += 't max = ' + str( max([max(ti) for ti in t]) ) +'\n'
            text += 'a max = ' + str( max([max(ai) for ai in a]) ) +'\n'
            text += 'X max = ' + str( max([max(xi) for xi in x]) ) +'\n'
            text += 'Rev max = ' + str( max([max(revi) for revi in rev]) ) +'\n'
            text += 't = ' + ', '.join( [str(i) for i in [max(ti) for ti in t]] )
            self.ui.textBrowser.setText(text)
        except:
            self.ui.textBrowser.setText('Error!!!\n\n' + '\n'.join( [str(i) for i in sys.exc_info()] ))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
