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
        layout.addWidget(QPushButton('Subject'))
        layout.addWidget(QPushButton('Faculty'))
        layout.addWidget(QPushButton('Room No'))
        self.setLayout(layout)




class CustomWidget(QWidget):

    def __init__(self, parent=None):
        super(CustomWidget,self).__init__(parent)

        # add your buttons
        layout = QVBoxLayout(self)

        # adjust spacings to your needs
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        list = QListWidget()
        list.setMaximumHeight(100)


        item2 = QListWidgetItem(list)
        item_widget2 = EditButtonsWidget()
        item2.setSizeHint(item_widget2.sizeHint())
        list.addItem(item2)
        list.setItemWidget(item2, item_widget2)

        item3 = QListWidgetItem(list)
        item_widget3 = EditButtonsWidget()
        item3.setSizeHint(item_widget3.sizeHint())
        list.addItem(item3)
        list.setItemWidget(item3, item_widget3)

        # add your buttons
        layout.addWidget(list)
        
        self.setLayout(layout)

        


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
        
        self.setCellWidget(0,5, EditButtonsWidget())
        self.setCellWidget(0,3, CustomWidget())
        self.resizeRowsToContents()
        self.cellChanged.connect(self._cellclicked)

    @QtCore.pyqtSlot(int, int)
    def _cellclicked(self, r, c):
        it = self.item(r, c)
        it.setTextAlignment(QtCore.Qt.AlignCenter)        

    @QtCore.pyqtSlot()
    def _addrow(self):
        rowcount = self.rowCount()
        self.insertRow(rowcount)
        self.setCellWidget(rowcount,5, EditButtonsWidget())
        self.resizeRowsToContents()

    @QtCore.pyqtSlot()
    def _testrow(self):
        self.setItem(0,0, QTableWidgetItem("Cell (0,0)"))
        item=self.itemAt(0,0)
        print(item)
       


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

        test_button = QtWidgets.QPushButton("Test")
        test_button.clicked.connect(table._testrow)

        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(add_button, alignment=QtCore.Qt.AlignBottom)
        button_layout.addWidget(delete_button, alignment=QtCore.Qt.AlignTop)
        button_layout.addWidget(test_button, alignment=QtCore.Qt.AlignTop)


        tablehbox = QtWidgets.QHBoxLayout()
        tablehbox.setContentsMargins(10, 10, 10, 10)
        tablehbox.addWidget(table)

        grid = QtWidgets.QGridLayout(self)
        grid.addLayout(button_layout, 0, 1)
        grid.addLayout(tablehbox, 0, 0)        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = ThirdTabLoads()
    w.setGeometry(0, 0, 1000,400)
    w.show()
    sys.exit(app.exec_())
