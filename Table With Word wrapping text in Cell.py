from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self, rows, columns):
        super(Window, self).__init__()
        self.table = QtWidgets.QTableView(self)
        self.table.horizontalHeader().setVisible(False)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.table)
        model =  QtGui.QStandardItemModel(rows, columns, self.table)
        self.table.setModel(model)
        text = 'some long item of text that requires word-wrapping'
        for column in range(model.columnCount()):
            self.table.setColumnWidth(column, 150)
            for row in range(model.rowCount()):
                item = QtGui.QStandardItem(text)
                model.setItem(row, column, item)
                # self.table.setRowHeight(row, 100)
        self.table.resizeRowsToContents()

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window(4, 3)
    window.setGeometry(800, 150, 500, 250)
    window.show()
    sys.exit(app.exec_())
