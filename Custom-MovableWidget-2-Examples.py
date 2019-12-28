import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget



class MovableWidget(QWidget):

    def __init__(self):
        super(MovableWidget, self).__init__()

        #remove the frame
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.pressing = False

    # overriding the three next methods is a way to customize your Widgets
    # not just in terms of appearance but also behavioral.

    def mousePressEvent(self, QMouseEvent):
        #the pos of the widget when you first pressed it.
        self.start = QMouseEvent.pos()
        #to make sure you are holding mouse button down
        self.pressing = True

    def mouseMoveEvent(self, QMouseEvent):

        # You can Verify if it's also the left button and some other things
        # you need.
        if self.pressing : #and QMouseEvent.type() == Qt.LeftButton
            self.end = QMouseEvent.pos()
            self.delta = self.mapToGlobal(self.end-self.start)
            self.move(self.delta)
            self.end = self.start

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

# inherits from QDialog and from MovableWidget so we can have its properties.
class CustomDialog(QDialog, MovableWidget):

    def __init__(self):
        super(CustomDialog, self).__init__()

        #Make the Dialog transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        # the widget will dispose itself according to the layout rules he's
        # inserted into.
        self.inner_widget = QWidget()
        self.inner_widget.setFixedSize(300,300)
        self.inner_layout = QHBoxLayout()
        self.inner_widget.setLayout(self.inner_layout)

        self.btn_change_color = QPushButton("Roll Color")

        self.btn_change_color.setStyleSheet("""
            background-color: green;
        """)

        # will connect to a function to be executed when the button is clicked.
        self.btn_change_color.clicked.connect(self.change_color)
        self.inner_layout.addWidget(self.btn_change_color)

        # Choose among many layouts according to your needs, QVBoxLayout,
        # QHBoxLayout, QStackedLayout, ... you can set its orientation
        # you can set its policies, spacing, margins. That's one of the main
        # concepts you have to learn to customize your Widget in the way
        # you want.
        self.layout = QVBoxLayout()

        # stylesheet have basically CSS syntax can call it QSS.
        # it can be used only on objects that come from Widgets
        # Also one of the main things to learn about customizing Widgets.

        # Note: The stylesheet you set in the "father" will be applied to its
        # children. Unless you tell it to be applied only to it and/or specify
        # each children's style.

        # The point I used inside the StyleSheet before the QDialog
        # e.g .QDialog and .QWidget says it'll be applied only to that
        # instance.

        self.setStyleSheet("""
            .QDialog{
                border-radius: 10px;
            }
        """)
        self.inner_widget.setStyleSheet("""
            .QWidget{
                background-color: red;
            }
        """)


        self.layout.addWidget(self.inner_widget)
        self.setLayout(self.layout)

    def change_color(self):
        red = random.choice(range(0,256))
        green = random.choice(range(0,256))
        blue = random.choice(range(0,256))
        self.inner_widget.setStyleSheet(
        """
            background-color: rgb({},{},{});
        """.format(red,green,blue)
        )

# since MovableWidget inherits from QWidget it also have QWidget properties.
class ABitMoreCustomizedWidget(MovableWidget):

    def __init__(self):
        super(ABitMoreCustomizedWidget, self).__init__()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.custom_button1 = CustomButton("Button 1")
        self.custom_button1.clicked.connect(self.btn_1_pressed)
        self.custom_button2 = CustomButton("Button 2")
        self.custom_button2.clicked.connect(self.btn_2_pressed)

        self.layout.addWidget(self.custom_button1)
        self.layout.addWidget(self.custom_button2)

    def btn_1_pressed(self):
        self.custom_button1.hide()
        self.custom_button2.show()

    def btn_2_pressed(self):
        self.custom_button2.hide()
        self.custom_button1.show()

class CustomButton(QPushButton):

    # it could receive args and keys** so all the QPushButton initializer
    # would work for here too.
    def __init__(self, txt):
        super(CustomButton, self).__init__()
        self.setText(txt)
        self.setStyleSheet("""
            QPushButton{
                background-color: black;
                border-radius: 5px;
                color: white;
            }
            QPushButton::pressed{
                background-color: blue;
            }
            QPushButton::released{
                background-color: gray;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    custom_dialog = CustomDialog()
    custom_widget = ABitMoreCustomizedWidget()
    custom_dialog.show()
    custom_widget.show()
    sys.exit(app.exec_())
