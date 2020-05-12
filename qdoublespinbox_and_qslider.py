# -*- coding: utf-8 -*-
import sys
from decimal import Decimal, ROUND_HALF_UP
from PyQt5 import QtCore, QtGui, QtWidgets

class QDoublespinboxAndQSlider(QtWidgets.QWidget):
    def __init__(self, parent, minimum=0, maximum=100, step=1):
        super(QDoublespinboxAndQSlider, self).__init__(parent)

        self.non_update = True
        
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)

        self.label = QtWidgets.QLabel('Label', self)
        self.label.setSizePolicy(size_policy)

        self.double_spinbox = QtWidgets.QDoubleSpinBox(self)
        self.double_spinbox.setSizePolicy(size_policy)

        self.slider = QtWidgets.QSlider(self)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setSizePolicy(size_policy)

        self.double_spinbox.valueChanged.connect(self.double_spinbox_changed)
        self.slider.valueChanged.connect(self.slider_changed)
        
        self.horizontal_widget = QtWidgets.QWidget(self)
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.horizontal_widget)
        self.horizontal_layout.addWidget(self.label)
        self.horizontal_layout.addWidget(self.double_spinbox)
        
        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.addWidget(self.horizontal_widget)
        self.vertical_layout.addWidget(self.slider)
        
        self.set_single_step(step)
        self.slider.setMinimum(0)
        self.set_minimum(minimum)
        self.set_maximum(maximum)

    def set_value(self, value):
        self.double_spinbox.setValue(value)
        
    def set_maximum(self, value):
        self.double_spinbox.setMaximum(value)
        self.set_slider_maximum()

    def set_minimum(self, value):
        self.double_spinbox.setMinimum(value)
        self.set_slider_maximum()

    def set_single_step(self, value):
        self.double_spinbox.setSingleStep( value )
        self.double_spinbox.setDecimals( len(str(value).split('.')[-1]) )
        self.set_slider_maximum()

    def set_slider_maximum(self):
        double_spinbox_range = self.double_spinbox.maximum() - self.double_spinbox.minimum()
        slider_max = double_spinbox_range / self.double_spinbox.singleStep()
        self.slider.setMaximum( int(slider_max) )

    def slider_changed(self, value):
        if self.non_update:
            return
        value2 = self.round2( float(value) * self.double_spinbox.singleStep() )
        self.double_spinbox.setValue(value2)
        self.update_plotwidget()

    def double_spinbox_changed(self, value):
        if self.non_update:
            return
        value2 = int( self.round2( value / self.double_spinbox.singleStep() ) )
        self.slider.setValue(value2)
        self.update_plotwidget()

    def round2(self, value):
        dicimals = str( self.double_spinbox.singleStep() / 10.0 )
        value2 = float( Decimal( str(value) ).quantize( Decimal(dicimals), rounding=ROUND_HALF_UP ) )
        return value2

    def update_plotwidget(self):
        mainwindow = self.find_mainwindow(self)
        if mainwindow is None:
            return
        mainwindow.update_plotwidget()

    def find_mainwindow(self, parent):
        if parent is None:
            return None
        if parent.inherits('QMainWindow'):
            return parent
        return self.find_mainwindow(parent.parent())

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.doublespinbox_and_slider = QDoublespinboxAndQSlider(self, 0, 20, 0.001)
        self.verticalLayout.addWidget(self.doublespinbox_and_slider)

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow(None)
    mainwindow.show()
    app.exec()
 
if __name__ == '__main__':
    main()