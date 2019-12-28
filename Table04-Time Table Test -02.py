import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class EditButtonsWidget(QWidget):

    def __init__(self, parent=None):
        super(EditButtonsWidget,self).__init__(parent)

        # add your buttons
        layout = QVBoxLayout(self)

        # adjust spacings to your needs
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        # add your buttons
        layout.addWidget(QPushButton('Save'))
        layout.addWidget(QPushButton('Edit'))
        layout.addWidget(QPushButton('Delete'))
        self.setLayout(layout)



class Widget1(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        lay = QVBoxLayout(self)
        for i in range(4):
            lay.addWidget(QPushButton("{}".format(i)))


class LoadTable(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(LoadTable, self).__init__(1, 8, parent)
        self.setFont(QtGui.QFont("Helvetica", 10, QtGui.QFont.Normal, italic=False))   
        headertitle = ("Time-Course","Mon","Tue","Wed","Thu","Fri","Sat","Sun")
        self.setHorizontalHeaderLabels(headertitle)
        self.verticalHeader().hide()
        self.horizontalHeader().setHighlightSections(False)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.setColumnWidth(0, 130)
        combox_lay = QtWidgets.QComboBox(self)
        combox_lay.addItems(["I","II"])
     
        self.setCellWidget(0,5, EditButtonsWidget())
        self.setCellWidget(0, 4, combox_lay)
       
        self.cellChanged.connect(self._cellclicked)

    @QtCore.pyqtSlot(int, int)
    def _cellclicked(self, r, c):
        it = self.item(r, c)
        it.setTextAlignment(QtCore.Qt.AlignCenter)        

    @QtCore.pyqtSlot()
    def _addrow(self):
        rowcount = self.rowCount()
        self.insertRow(rowcount)
        combox_add = QtWidgets.QComboBox(self)
        combox_add.addItems(["I","II"])
        self.setCellWidget(rowcount, 4, combox_add)
        self.setCellWidget(rowcount,5, EditButtonsWidget())

    @QtCore.pyqtSlot()
    def _removerow(self):
        if self.rowCount() > 0:
            self.removeRow(self.rowCount()-1)


class ThirdTabLoads(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ThirdTabLoads, self).__init__(parent)    

        table = LoadTable()

        add_button = QtWidgets.QPushButton("Add")
        add_button.clicked.connect(table._addrow)

        delete_button = QtWidgets.QPushButton("Delete")
        delete_button.clicked.connect(table._removerow)

        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(add_button, alignment=QtCore.Qt.AlignBottom)
        button_layout.addWidget(delete_button, alignment=QtCore.Qt.AlignTop)


        tablehbox = QtWidgets.QHBoxLayout()
        tablehbox.setContentsMargins(10, 10, 10, 10)
        tablehbox.addWidget(table)

        grid = QtWidgets.QGridLayout(self)
        grid.addLayout(button_layout, 0, 1)
        grid.addLayout(tablehbox, 0, 0)        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = ThirdTabLoads()
    w.show()
    sys.exit(app.exec_())
