import sys
import qtpy
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout, QStackedWidget
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy, QHeaderView
from PyQt5.QtGui import QPalette, QColor, QCursor
from PyQt5.QtGui import QPalette, QColor, QCursor
from PyQt5 import QtCore
import mysql.connector
from mysql.connector import Error


class AdminPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Page")
        self.setFixedSize(1380, 650)

        self.stacked_widget = QStackedWidget(self)

        self.headers = []
        self.rows = []

        self.login_widget = QWidget()
        layout = QGridLayout(self.login_widget)

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
        layout.addWidget(welcome_note, 0, 0, 1, 7)

        b1 = button_maker("Q1")
        layout.addWidget(b1, 1, 0)
        b1.clicked.connect(lambda: self.querify(1))
        b2 = button_maker("Q2")
        layout.addWidget(b2, 2, 1)
        b2.clicked.connect(lambda: self.querify(2))
        b3 = button_maker("Q3")
        layout.addWidget(b3, 1, 2)
        b3.clicked.connect(lambda: self.querify(3))
        b4 = button_maker("Q4")
        layout.addWidget(b4, 2, 3)
        b4.clicked.connect(lambda: self.querify(4))
        b5= button_maker("Q5")
        layout.addWidget(b5, 1, 4)
        b5.clicked.connect(lambda: self.querify(5))
        b6 = button_maker("Q6")
        layout.addWidget(b6, 2, 5)
        b6.clicked.connect(lambda: self.querify(6))
        b7 = button_maker("Q7")
        layout.addWidget(b7, 1, 6)
        b7.clicked.connect(lambda: self.querify(7))

        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.setCurrentWidget(self.login_widget)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

        self.setLayout(layout)

    def querify(self, qn):
        match qn:
            case 1:
                self.q1()
            case 2:
                self.q2()
            case 3:
                self.q3()
            case 4:
                self.q4()
            case 5:
                self.q5()
            case 6:
                self.q6()
            case 7:
                self.q7()
        while self.stacked_widget.count() > 1:
            self.stacked_widget.removeWidget(self.stacked_widget.widget(1))
        self.tabular_view(cursor)

    def q1(self):
        cursor.execute(
            f'''
            select student_enrollment_stid from mydb.stsec
            where section_secid in (select secid from mydb.section
                where year = {year}
                and semester = {semester})
            '''
        )
        self.headers = []
        self.headers.append("STUDENT ID")
        self.rows = []
        for row in cursor:
            self.rows.append(row[0])
            print(row[0])

    def q2(self):
        cursor.execute(
            f'''
            select course_coid from mydb.section as s
            where year = {year}
            and semester = {semester}
            and 5 < (select count(student_enrollment_stid) from mydb.stsec
                where stsec.section_secid = s.secid)
            '''
        )
        self.headers = []
        self.headers.append("COURSE ID")
        self.rows = []
        for row in cursor:
            self.rows.append(row)
            print(row)

    def q3(self):
        cursor.execute(
            '''
            select stsec.student_enrollment_stid, (sum(stsec.grade * course.credit)/sum(course.credit)) as 'weighted average'
            from course
            inner join section on course.coid = section.course_coid
            inner join stsec on section.secid = stsec.section_secid
            group by stsec.student_enrollment_stid
            '''
        )
        self.headers = []
        self.headers.append("STUDENT ID")
        self.headers.append("WEIGHTED AVERAGE")
        self.rows = []
        for row in cursor:
            self.rows.append(row)
            print(row)

    def q4(self):
        cursor.execute(
            '''
            select * from professor as p
            where 70 < (select sum(credit) from course
                where coid in (select course_coid from section
                    where section.professor_prof_id = p.prof_id))
            '''
        )
        self.headers = []
        self.headers = ["PROF_ID", "NAME", "SALARY", "DEPARTMENT", "PHONE"]
        self.rows = []
        for row in cursor:
            self.rows.append(row)
            print(row)

    def q5(self):
        cursor.execute(
            '''
            select book.name from book
            where isbn in (select book_isbn from library_has_book as lhb
                where 4 < (select count(distinct student_enrollment_stid) from borrows
                    where borrows.library_has_book_bookid = lhb.bookid))
            '''
        )
        self.headers = []
        self.headers.append("BOOK NAME")
        self.rows = []
        for row in cursor:
            self.rows.append(row)
            print(row)

    def q6(self):
        cursor.execute(
            f'''
            select professor_prof_id, group_concat(schedule separator "\\n") from section as s
            where year = {year}
            and semester = {semester}
            and 20 < (select count(student_enrollment_stid) from stsec
                where s.secid = stsec.section_secid)
            and 3 <= (select count(course_coid) from section
                where year = {year}
                and semester = {semester}
                and section.professor_prof_id = s.professor_prof_id)
            group by professor_prof_id
            '''
        )
        self.headers = []
        self.headers.append("PROF_ID")
        self.headers.append("SCHEDULE")
        self.rows = []
        for row in cursor:
            self.rows.append(row)
            print(row)

    def q7(self):
        cursor.execute(
            '''
            select * from student
            where enrollment_stid not in (select student_enrollment_stid from stsec)
            '''
        )
        self.headers = []
        self.headers = ["STUDENT ID", "NAME", "MAJOR", "TOTAL PASSED CREDIT", "LEVEL", "TERM", "STATE"]
        self.rows = []
        for row in cursor:
            self.rows.append(row)
            print(row)

    def tabular_view(self, cursor):
        print("send help")
        admin_page = QWidget()
        layout = QVBoxLayout(admin_page)

        # Add a table to display the data
        table = QTableWidget()
        table.setStyleSheet("background-color: #9F86C0; border: 3px solid #231942;")

        # Adjusting the cell font
        '''table.horizontalHeader().setStyleSheet("font-size: 15px; color: white;")

        table.setHorizontalHeaderLabels(self.headers)

        table.setRowCount(len(self.rows))
        table.setColumnCount(len(self.headers))
        table.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])

        # Fill the table with data
        for row in self.rows:
            for column in row:
                table.setItem(row, column, self.rows[row][column])

        # Resize the columns to content
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Set the size policy for the table
        table.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        table.setMaximumSize(580, table.verticalHeader().defaultSectionSize() + 50)'''

        layout.addWidget(table)


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


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="de1u1ub*By",
    database="mydb"
)
cursor = conn.cursor()
cursor.execute("select year(current_date())")
year = cursor.fetchone()[0]
cursor.execute("select month(current_date())")
semester = 0
month = cursor.fetchone()[0]
if month in {9, 10, 11, 12, 1}:
    semester = 1
elif month in {2, 3, 4, 5, 6, 7}:
    semester = 2
app = QApplication(sys.argv)
ap = AdminPage()
ap.show()
sys.exit(app.exec_())
