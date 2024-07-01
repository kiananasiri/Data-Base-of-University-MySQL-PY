import sys
import qtpy
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox , QVBoxLayout, QStackedWidget
from PyQt5.QtWidgets import  QTableWidget, QTableWidgetItem , QSizePolicy , QHeaderView
from PyQt5.QtGui import QPalette, QColor, QCursor
from PyQt5.QtGui import QPalette, QColor , QCursor
from PyQt5 import QtCore
import mysql.connector
from mysql.connector import Error
import queries

class Admin_page(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Page")
        self.setFixedSize(1380, 650)

        grid = QGridLayout()
        self.setLayout(grid)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(200, 162, 200))  # lilac color
        self.setPalette(palette)

        welcome_note = QLabel("Welcome, Admin!")
        welcome_note.setAlignment(QtCore.Qt.AlignCenter)
        welcome_note.setStyleSheet(
            '''
            font-size: 30px;
            color: purple;
            top-margin: 20px;
            '''
        )
        grid.addWidget(welcome_note, 0, 0, 1, 7)

        b1 = button_maker("Q1")
        grid.addWidget(b1, 1, 0)
        b1.clicked.connect(lambda:queries.Q1())
        b2 = button_maker("Q2")
        grid.addWidget(b2, 2, 1)
        b2.clicked.connect(lambda: queries.Q2())
        b3 = button_maker("Q3")
        grid.addWidget(b3, 1, 2)
        b3.clicked.connect(lambda: queries.Q3())
        b4 = button_maker("Q4")
        grid.addWidget(b4, 2, 3)
        b4.clicked.connect(lambda: queries.Q4())
        b5= button_maker("Q5")
        grid.addWidget(b5, 1, 4)
        b5.clicked.connect(lambda: queries.Q5())
        b6 = button_maker("Q6")
        grid.addWidget(b6, 2, 5)
        b6.clicked.connect(lambda: queries.Q6())
        b7 = button_maker("Q7")
        grid.addWidget(b7, 1, 6)
        b7.clicked.connect(lambda: queries.Q7())



        #b.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

def button_maker(txt):
    b = QPushButton(txt)
    b.setFixedWidth(100)
    b.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    b.setStyleSheet(
        '''
        *{
            border: 3px solid '#231942';
            border-radius: 25px;
            border-collapse: separate;
            color: purple;
            font-size: 16px;
            padding: 15px 5px;
            margin-top: 10px;
            margin-bottom: 30px;
        }
        *:hover{
            background: '#231942';
            border: none;
            color: white;
        }
        '''
    )
    return b



app = QApplication(sys.argv)
ap = Admin_page()
ap.show()
sys.exit(app.exec_())
