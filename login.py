import sys
import qtpy
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout, QStackedWidget
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy, QHeaderView, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPalette, QColor, QCursor, QFont, QPixmap, QBitmap, QPainter, QPainterPath
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import mysql.connector
from mysql.connector import Error

def create_admin_page():
    admin_page = QWidget()
    admin_page.setWindowTitle("Admin Page")
    admin_page.setFixedSize(1380, 650)
    grid = QGridLayout()
    admin_page.setLayout(grid)
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(200, 162, 200))
    admin_page.setPalette(palette)
    welcome_note = QLabel("Welcome, Admin!")
    welcome_note.setAlignment(Qt.AlignCenter)
    welcome_note.setStyleSheet(
        '''
        font-size: 30px;
        color: purple;
        border: 2px solid black;
        background-color: #FFC0CB;
        padding: 10px;
        '''
    )
    grid.addWidget(welcome_note, 0, 0, 1, 7)
    b1 = button_maker("Q1")
    grid.addWidget(b1, 1, 0)
    b1.clicked.connect(lambda: Q1())
    b2 = button_maker("Q2")
    grid.addWidget(b2, 2, 1)
    b2.clicked.connect(lambda: Q2())
    b3 = button_maker("Q3")
    grid.addWidget(b3, 1, 2)
    b3.clicked.connect(lambda: Q3())
    b4 = button_maker("Q4")
    grid.addWidget(b4, 2, 3)
    b4.clicked.connect(lambda: Q4())
    b5 = button_maker("Q5")
    grid.addWidget(b5, 1, 4)
    b5.clicked.connect(lambda: Q5())
    b6 = button_maker("Q6")
    grid.addWidget(b6, 2, 5)
    b6.clicked.connect(lambda: Q6())
    b7 = button_maker("Q7")
    grid.addWidget(b7, 1, 6)
    b7.clicked.connect(lambda: Q7())
    return admin_page

def button_maker(txt):
    b = QPushButton(txt)
    b.setFixedWidth(100)
    b.setCursor(QCursor(Qt.PointingHandCursor))
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

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="bonjour1",
            database="mydb"
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def execute_query(query):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()
            return rows
        except Error as e:
            print(f"Error executing query: {e}")
            conn.close()
            return []
    else:
        return []

def Q1():
    query = '''
        Select ENROLLMENT_STID from student where ENROLLMENT_STID IN (select * from STSEC)
        '''
    rows = execute_query(query)
    for row in rows:
        print(row[0])
    rows = execute_query(query)
    result_page = QWidget()
    layout = QVBoxLayout(result_page)
    title = QLabel("Query 1 Result")
    title.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
    title.setStyleSheet(
        '''
        font-size: 30px;
        color: purple;
        border: 2px solid black;
        background-color: #FFC0CB;
        padding: 10px;
        '''
    )
    layout.addWidget(title)
    table = QTableWidget()
    table.setStyleSheet("background-color: #9F86C0; border: 3px solid #231942;")
    table.horizontalHeader().setStyleSheet("font-size: 15px; color: white;")
    if rows:
        table.setRowCount(len(rows))
        table.setColumnCount(1)
        for row_index, row_data in enumerate(rows):
            table.setItem(row_index, 0, QTableWidgetItem(str(row_data[0])))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        table.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        table.setMaximumSize(600, table.verticalHeader().defaultSectionSize() * len(rows) + 50)
        layout.addWidget(table)
    else:
        no_data_label = QLabel("No data found for Query 1.")
        no_data_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(no_data_label)
    result_page.setLayout(layout)
    result_page.show()

def Q2():
    query = '''
        SELECT course_coid FROM mydb.section AS s
        WHERE year = YEAR(CURRENT_DATE()) AND semester = CASE 
                                WHEN MONTH(CURRENT_DATE()) IN (9, 10, 11, 12, 1) THEN 1
                                ELSE 2
                                END
        AND 5 < (SELECT COUNT(student_enrollment_stid) FROM mydb.stsec
                WHERE stsec.section_secid = s.secid)
        '''
    rows = execute_query(query)
    for row in rows:
        print(row[0])

def Q3():
    query = '''
        SELECT stsec.student_enrollment_stid, (SUM(stsec.grade * course.credit)/SUM(course.credit)) AS 'weighted average'
        FROM course
        INNER JOIN section ON course.coid = section.course_coid
        INNER JOIN stsec ON section.secid = stsec.section_secid
        GROUP BY stsec.student_enrollment_stid
        '''
    rows = execute_query(query)
    for row in rows:
        print(row)
    result_page = QWidget()
    layout = QVBoxLayout(result_page)
    title = QLabel("Query 3 Result")
    title.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
    title.setStyleSheet(
        '''
        font-size: 30px;
        color: purple;
        border: 2px solid black;
        background-color: #FFC0CB;
        padding: 10px;
        '''
    )
    layout.addWidget(title)
    table = QTableWidget()
    table.setStyleSheet("background-color: #9F86C0; border: 3px solid #231942;")
    table.horizontalHeader().setStyleSheet("font-size: 15px; color: white;")
    rows = execute_query(query)
    if rows:
        show_results_page(rows)
    else:
        print("No results found.")

def show_results_page(rows):
    results_page = QWidget()
    layout = QVBoxLayout(results_page)
    result_label = QLabel("Results for Q3:")
    layout.addWidget(result_label)
    table = QTableWidget()
    table.setColumnCount(1)
    table.setRowCount(len(rows))
    table.setHorizontalHeaderLabels(["Student Enrollment ID"])
    for row_index, row in enumerate(rows):
        table.setItem(row_index, 0, QTableWidgetItem(str(row[0])))
    layout.addWidget(table)
    results_page.setLayout(layout)
    form.stacked_widget.addWidget(results_page)
    form.stacked_widget.setCurrentWidget(results_page)

def Q4():
    query = '''
        SELECT * FROM professor AS p
        WHERE 2 < (SELECT SUM(credit) FROM course
                    WHERE coid IN (SELECT course_coid FROM section
                                    WHERE section.professor_prof_id = p.prof_id))
        '''
    rows = execute_query(query)
    for row in rows:
        print(row)

def Q5():
    query = '''
        SELECT book.name FROM book
        WHERE isbn IN (SELECT book_isbn FROM library_has_book AS lhb
                        WHERE 4 < (SELECT COUNT(DISTINCT student_enrollment_stid) FROM borrows
                                    WHERE borrows.library_has_book_bookid = lhb.bookid))
        '''
    rows = execute_query(query)
    for row in rows:
        print(row)

def Q6():
    query = '''
        select secid from stsec where group by 
        '''
    rows = execute_query(query)
    for row in rows:
        print(row)

def Q7():
    query = '''
        SELECT * FROM student
        WHERE enrollment_stid NOT IN (SELECT student_enrollment_stid FROM stsec)
        '''
    rows = execute_query(query)
    for row in rows:
        print(row)

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.setFixedSize(1380, 650)
        
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(200, 162, 200))
        self.setPalette(palette)
        
        self.stacked_widget = QStackedWidget(self)
        
        self.login_widget = QWidget()
        layout = QGridLayout(self.login_widget)

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        label_name.setFixedWidth(200)
        label_name.setAlignment(QtCore.Qt.AlignHCenter)
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1, 1, 3)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        label_password.setFixedWidth(200)
        label_password.setAlignment(QtCore.Qt.AlignHCenter)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1, 1, 3)

        button_admin = QPushButton('Admin Login')
        button_student = QPushButton('Student Login')
        button_professor = QPushButton('Professor Login')

        button_admin.setFixedWidth(170)
        button_student.setFixedWidth(170)
        button_professor.setFixedWidth(170)
        
        button_student.setStyleSheet("border: 3px solid '#231942';"
                                     'border-radius: 10px;'
                                     'font-size: 15px;'
                                     'color: white;'
                                     'padding: 25x 0;'
                                     'margin: 15px 20px;}'
                                     "*:hover{background: '#5E548E';}")
        button_professor.setStyleSheet("border: 3px solid '#231942';"
                                     'border-radius: 10px;'
                                     'font-size: 15px;'
                                     'color: white;'
                                     'padding: 25x 0;'
                                     'margin: 15px 20px;}'
                                     "*:hover{background: '#5E548E';}")
        button_admin.setStyleSheet("border: 3px solid '#231942';"
                                     'border-radius: 10px;'
                                     'font-size: 15px;'
                                     'color: white;'
                                     'padding: 25x 0;'
                                     'margin: 15px 20px;}'
                                     "*:hover{background: '#5E548E';}")
        button_admin.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button_student.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button_professor.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        button_admin.clicked.connect(self.check_admin_password)
        layout.addWidget(button_admin, 2, 1)

        button_student.clicked.connect(self.check_student_password)
        layout.addWidget(button_student, 2, 2)

        button_professor.clicked.connect(self.check_professor_password)
        layout.addWidget(button_professor, 2, 3)

        layout.setRowMinimumHeight(2, 75)
        
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.setCurrentWidget(self.login_widget)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

        self.setLayout(layout)

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='mydb',
                user='root',
                password='bonjour1'
            )
            if connection.is_connected():
                return connection
        except Error as e:
            msg = QMessageBox()
            msg.setText(f"Error while connecting to MySQL: {e}")
            msg.exec_()
            return None

    def check_admin_password(self):
        username = 'admin'
        password = '11'

        if username == self.lineEdit_username.text() and password == self.lineEdit_password.text():
            msg = QMessageBox()
            msg.setText('Admin Login Successful')
            msg.exec_()
            self.show_admin_page()
        else:
            msg = QMessageBox()
            msg.setText('Incorrect Admin Username or Password')
            msg.exec_()

    def show_admin_page(self):
        admin_page = create_admin_page()
        self.stacked_widget.addWidget(admin_page)
        self.stacked_widget.setCurrentWidget(admin_page)
        
    def check_student_password(self):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT ENROLLMENT_STID FROM STUDENT WHERE ENROLLMENT_STID = %s"
            cursor.execute(query, (self.lineEdit_username.text(),))
            result = cursor.fetchone()
            connection.close()

            msg = QMessageBox()
            if result:
                msg.setText('Student Login Successful')
                msg.exec_()
                self.login_action('STUDENT', result[0])
            else:
                msg.setText('Incorrect Student Username')
                msg.exec_()

    def check_professor_password(self):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT PROF_ID FROM PROFESSOR WHERE PROF_ID = %s"
            cursor.execute(query, (self.lineEdit_username.text(),))
            result = cursor.fetchone()
            connection.close()

            msg = QMessageBox()
            if result:
                msg.setText('Professor Login Successful')
                msg.exec_()
                self.login_action('PROFESSOR', result[0])
            else:
                msg.setText('Incorrect Professor Username')
                msg.exec_()

    def login_action(self, user_type, user_id):
        while self.stacked_widget.count() > 1:
            self.stacked_widget.removeWidget(self.stacked_widget.widget(1))

        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            if user_type == 'STUDENT':
                query = "SELECT * FROM STUDENT WHERE ENROLLMENT_STID = %s"
            elif user_type == 'PROFESSOR':
                query = "SELECT * FROM PROFESSOR WHERE PROF_ID = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            connection.close()

            if result:
                self.student_page(cursor, result) if user_type == 'STUDENT' else self.professor_page(cursor, result)
            else:
                msg = QMessageBox()
                msg.setText('No data found for user ID.')
                msg.exec_()
            
        else:
            msg = QMessageBox()
            msg.setText('Database connection failed.')
            msg.exec_()

    def student_page(self, cursor, result):
        user_page = QWidget()
        layout = QVBoxLayout(user_page)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(5, 5)
        shadow.setColor(QColor(136, 136, 136))

        image_label = QLabel()
        pixmap = QPixmap("/Users/kiananasiri/Desktop/welcomestu.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        size = 200
        scaled_pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
 
        layout.addWidget(image_label)
        self.setLayout(layout)

        table = QTableWidget()
        table.setStyleSheet("background-color: #d3d3d3 ; border: 2px solid #231942;")
        table.horizontalHeader().setStyleSheet("font-size: 10px; color: black;")
        table.setHorizontalHeaderLabels(["STUDENTID", "NAME", "MAJOR", "TOTAL PASSED CREDIT", "LEVEL", "TERM", "STATE"])
    
        table.setRowCount(1)
        table.setColumnCount(len(result))
        table.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])
        row_label = "STUDENT INFO"
        table.setVerticalHeaderLabels([row_label])
        for col_index, col_value in enumerate(result):
            table.setItem(0, col_index, QTableWidgetItem(str(col_value)))
            
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        table.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        table.setMaximumSize(600, table.verticalHeader().defaultSectionSize() + 20)
        
        table_widget = QWidget()
        table_layout = QVBoxLayout(table_widget)
        table_layout.addWidget(table)
        table_layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(table_widget, alignment=Qt.AlignCenter)

        layout.addWidget(table)

        buttonstu_section = QPushButton('SECTION')
        buttonstu_book = QPushButton('BOOK')
        buttonstu_another = QPushButton('ANOTHER')

        buttonstu_section.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        buttonstu_book.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        buttonstu_another.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        button_layout = QHBoxLayout()
        button_layout.addWidget(buttonstu_section)
        button_layout.addWidget(buttonstu_book)
        button_layout.addWidget(buttonstu_another)
        
        buttonstu_book.setStyleSheet("QPushButton {"
                             "    border: 3px solid #231942;"
                             "    border-radius: 10px;"
                             "    font-size: 15px;"
                             "    color: white;"
                             "    padding: 10px 20px;"
                             "    margin: 15px 20px;"
                             "}"
                             "QPushButton:hover {"
                             "    background-color: #5E548E;"
                             "}"
                             "QPushButton:pressed {"
                             "    background-color: #231942;"
                             "    border-color: #231942;"
                             "}")
        buttonstu_section.setStyleSheet("QPushButton {"
                             "    border: 3px solid #231942;"
                             "    border-radius: 10px;"
                             "    font-size: 15px;"
                             "    color: white;"
                             "    padding: 10px 20px;"
                             "    margin: 15px 20px;"
                             "}"
                             "QPushButton:hover {"
                             "    background-color: #5E548E;"
                             "}"
                             "QPushButton:pressed {"
                             "    background-color: #231942;"
                             "    border-color: #231942;"
                             "}")
        buttonstu_book.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        button_widget = QWidget()
        button_widget.setLayout(button_layout)
        layout.addWidget(button_widget, alignment=QtCore.Qt.AlignBottom)
        
        buttonstu_section.clicked.connect(self.show_section_data)
        buttonstu_book.clicked.connect(lambda: self.show_borrowed_books(result[0]))

        self.stacked_widget.addWidget(user_page)
        self.stacked_widget.setCurrentWidget(user_page)

    
    def show_section_data(self):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='mydb',
            user='root',
            password='bonjour1'
        )
        
        if connection:
            cursor = connection.cursor()
            query = """
                SELECT STSEC.*, SECTION.*
                FROM STSEC
                JOIN SECTION ON STSEC.SECTION_SECID = SECTION.SECID
                WHERE STSEC.STUDENT_ENROLLMENT_STID = %s
            """
            cursor.execute(query, (self.lineEdit_username.text(),))
            results = cursor.fetchall()
            connection.close()
            
            section_page = QWidget()
            layout = QVBoxLayout(section_page)
            
            title = QLabel("Section Page")
            title.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
            title.setStyleSheet('''
                font-size: 30px;
                color: black;
                border: 2px solid black;
                background-color: #CECECE;
                padding: 10px;
            ''')
            title.setMaximumSize(700, 80)
            layout.addWidget(title)
            section_page.setLayout(layout)

            section_table = QTableWidget()
            section_table.setStyleSheet("background-color: #9F86C0; border: 3px solid #231942;")
            section_table.horizontalHeader().setStyleSheet("font-size: 15px; color: white;")

            if results:
                section_table.setRowCount(len(results))
                section_table.setColumnCount(len(results[0]))
                section_table.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])
                
                for row_index, row_data in enumerate(results):
                    for col_index, col_value in enumerate(row_data):
                        section_table.setItem(row_index, col_index, QTableWidgetItem(str(col_value)))
                        
                section_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                section_table.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                section_table.setMaximumSize(1190, section_table.verticalHeader().defaultSectionSize() * len(results) + 50)
            else:
                msg = QMessageBox()
                msg.setText('No section data found for the student.')
                msg.exec_()

            layout.addWidget(section_table)
            self.stacked_widget.addWidget(section_page)
            self.stacked_widget.setCurrentWidget(section_page)

    except Error as e:
        print(f"Error retrieving data: {e}")

def show_borrowed_books(self, student_id):
    connection = self.create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
            SELECT BOOK.NAME, LIBRARY_has_BOOK.BOOK_ISBN, BORROWS.TAKE_DATE, BORROWS.RETURN_DATE
            FROM BORROWS
            JOIN LIBRARY_has_BOOK ON BORROWS.LIBRARY_has_BOOK_BOOKID = LIBRARY_has_BOOK.BOOKID
            JOIN BOOK on LIBRARY_has_BOOK.BOOK_ISBN = BOOK.ISBN
            WHERE BORROWS.STUDENT_ENROLLMENT_STID = %s
        """
        cursor.execute(query, (student_id,))
        borrowed_books = cursor.fetchall()
        connection.close()

        borrowed_books_page = QWidget()
        layout = QVBoxLayout(borrowed_books_page)

        borrowed_books_table = QTableWidget()
        borrowed_books_table.setStyleSheet("background-color: #9F86C0; border: 2px solid #231942;")
        borrowed_books_table.setRowCount(len(borrowed_books))
        borrowed_books_table.setColumnCount(4)
        borrowed_books_table.setHorizontalHeaderLabels(["NAME", "BOOKID", "BORROW DATE", "RETURN DATE"])

        for row_index, row_data in enumerate(borrowed_books):
            for col_index, col_value in enumerate(row_data):
                borrowed_books_table.setItem(row_index, col_index, QTableWidgetItem(str(col_value)))

        borrowed_books_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        borrowed_books_table.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        borrowed_books_table.setMaximumSize(800, 400)

        layout.addWidget(borrowed_books_table)
        self.stacked_widget.addWidget(borrowed_books_page)
        self.stacked_widget.setCurrentWidget(borrowed_books_page)

def professor_page(self, cursor, result):
    user_page = QWidget()
    layout = QVBoxLayout(user_page)

    table = QTableWidget()
    table.setStyleSheet("background-color: #9F86C0; border: 3px solid #231942;")
    table.horizontalHeader().setStyleSheet("font-size: 15px; color: white;")
    table.setHorizontalHeaderLabels(["PROF_ID", "NAME", "SALARY", "DEPARTMENT", "PHONE"])

    table.setRowCount(1)
    table.setColumnCount(len(result) - 3)
    table.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])

    for col_index, col_value in enumerate(result):
        table.setItem(0, col_index, QTableWidgetItem(str(col_value)))

    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    table.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    table.setMaximumSize(620, table.verticalHeader().defaultSectionSize() + 50)

    layout.addWidget(table)
    self.stacked_widget.addWidget(user_page)
    self.stacked_widget.setCurrentWidget(user_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoginForm()
    form.show()
    sys.exit(app.exec_())
