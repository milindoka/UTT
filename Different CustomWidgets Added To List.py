import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
    QHBoxLayout




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







class CustomQWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomQWidget, self).__init__(parent)

        label = QLabel("I am a custom widget")

        button = QPushButton("A useless button")

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    title = QLabel("Demo for widgets in a QListWidget")

    list = QListWidget()

    item = QListWidgetItem(list)
    item_widget = CustomQWidget()
    item.setSizeHint(item_widget.sizeHint())
    list.addItem(item)
    list.setItemWidget(item, item_widget)

    list.addItem("string displayed as string")

    item2 = QListWidgetItem(list)
    item_widget2 = CustomQWidget()
    item2.setSizeHint(item_widget2.sizeHint())
    list.addItem(item2)
    list.setItemWidget(item2, item_widget2)


    item3 = QListWidgetItem(list)
    item_widget3 = EditButtonsWidget()
    item3.setSizeHint(item_widget3.sizeHint())
    list.addItem(item3)
    list.setItemWidget(item3, item_widget3)




    

    window_layout = QVBoxLayout(window)
    window_layout.addWidget(title)
    window_layout.addWidget(list)
    window.setLayout(window_layout)

    window.show()

    sys.exit(app.exec_())
