import sys
import qtpy
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox , QVBoxLayout, QStackedWidget
from PyQt5.QtWidgets import  QTableWidget, QTableWidgetItem , QSizePolicy , QHeaderView , QHBoxLayout
from PyQt5.QtGui import QPalette, QColor, QCursor
from PyQt5.QtGui import QPalette, QColor , QCursor
from PyQt5 import QtCore 
from PyQt5.QtCore import Qt
import mysql.connector
from mysql.connector import Error

import sys
import qtpy
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox , QVBoxLayout, QStackedWidget
from PyQt5.QtWidgets import  QTableWidget, QTableWidgetItem , QSizePolicy , QHeaderView , QHBoxLayout
from PyQt5.QtGui import QPalette, QColor, QCursor
from PyQt5.QtGui import QPalette, QColor , QCursor
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
    palette.setColor(QPalette.Window, QColor(200, 162, 200))  # lilac color
    admin_page.setPalette(palette)

    welcome_note = QLabel("Welcome, Admin!")
    welcome_note.setAlignment(Qt.AlignCenter)
    welcome_note.setStyleSheet(
        '''
        font-size: 30px;
        color: purple;
        border: 2px solid black;
        background-color: #FFC0CB;  # light pink background color
        padding: 10px;
        '''
    )
    grid.addWidget(welcome_note, 0, 0, 1, 7)

    b1 = button_maker("Q1")
    grid.addWidget(b1, 1, 0)
    b1.clicked.connect(lambda: queries.Q1())
    b2 = button_maker("Q2")
    grid.addWidget(b2, 2, 1)
    b2.clicked.connect(lambda: queries.Q2())
    b3 = button_maker("Q3")
    grid.addWidget(b3, 1, 2)
    b3.clicked.connect(lambda: queries.Q3())
    b4 = button_maker("Q4")
    grid.addWidget(b4, 2, 3)
    b4.clicked.connect(lambda: queries.Q4())
    b5 = button_maker("Q5")
    grid.addWidget(b5, 1, 4)
    b5.clicked.connect(lambda: queries.Q5())
    b6 = button_maker("Q6")
    grid.addWidget(b6, 2, 5)
    b6.clicked.connect(lambda: queries.Q6())
    b7 = button_maker("Q7")
    grid.addWidget(b7, 1, 6)
    b7.clicked.connect(lambda: queries.Q7())

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


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.setFixedSize(1380, 650)
        
        # Set the background color to lilac
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(200, 162, 200))  # lilac color
        self.setPalette(palette)
        
        # Create a stacked widget to hold different pages--------------------------------------
        self.stacked_widget = QStackedWidget(self)
        
        # Login page widget --------------------------------------------------------------------------
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
                                     + 'border-radius: 10px;' 
                                     + 'font-size: 15px;' 
                                     + 'color: white;' 
                                     + 'padding: 25x 0;' 
                                     + 'margin: 15px 20px;}'
                                     + "*:hover{background: '#5E548E';}")
        button_professor.setStyleSheet("border: 3px solid '#231942';" 
                                     + 'border-radius: 10px;' 
                                     + 'font-size: 15px;' 
                                     + 'color: white;' 
                                     + 'padding: 25x 0;' 
                                     + 'margin: 15px 20px;}'
                                     + "*:hover{background: '#5E548E';}")
        button_admin.setStyleSheet("border: 3px solid '#231942';" 
                                     + 'border-radius: 10px;' 
                                     + 'font-size: 15px;' 
                                     + 'color: white;' 
                                     + 'padding: 25x 0;' 
                                     + 'margin: 15px 20px;}'
                                     + "*:hover{background: '#5E548E';}")
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
        
        
        # Add login widget to stacked widget
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.setCurrentWidget(self.login_widget)

        # Set layout for main window
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
        password = '11'  # Replace with actual password retrieval logic

        if username == self.lineEdit_username.text() and password == self.lineEdit_password.text():
            msg = QMessageBox()
            msg.setText('Admin Login Successful')
            msg.exec_()
            self.show_admin_page()  # Call the function to show admin page
        else:
            msg = QMessageBox()
            msg.setText('Incorrect Admin Username or Password')
            msg.exec_()

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
                # Perform further actions after successful login
                self.login_action('STUDENT', result[0])
                print(result[0])
                
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
                # Perform further actions after successful login
                self.login_action('PROFESSOR', result[0])
                
            else:
                msg.setText('Incorrect Professor Username')
                msg.exec_()

    def login_action(self, user_type, user_id):
    # Clear any previous pages from stacked widget
        while self.stacked_widget.count() > 1:
            self.stacked_widget.removeWidget(self.stacked_widget.widget(1))

        # Fetch user data from database based on user_type and user_id
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            if user_type == 'STUDENT':
                query = "SELECT * FROM STUDENT WHERE ENROLLMENT_STID = %s"
            elif user_type == 'PROFESSOR':
                query = "SELECT * FROM PROFESSOR WHERE PROF_ID = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()  # Assuming there's only one record for the ID

            # Close the database connection
            connection.close()

            if result:
                self.student_page(cursor, result) if user_type == 'STUDENT' else self.professor_page(cursor, result)
            else:
                # Handle case where no data was found (though it shouldn't happen if login is successful)
                msg = QMessageBox()
                msg.setText('No data found for user ID.')
                msg.exec_()
            
        else:
            # Handle case where database connection failed
            msg = QMessageBox()
            msg.setText('Database connection failed.')
            msg.exec_()

    def student_page(self, cursor, result):
        # Create a new widget to display user data
        user_page = QWidget()
        layout = QVBoxLayout(user_page)

        # Add a table to display the data
        table = QTableWidget()
        table.setStyleSheet("background-color: #9F86C0; border: 3px solid #231942;")

        # Adjusting the cell font
        table.horizontalHeader().setStyleSheet("font-size: 15px; color: white;")

        table.setHorizontalHeaderLabels(["STUDENT ID", "NAME", "MAJOR", "TOTAL PASSED CREDIT", "LEVEL", "TERM", "STATE"])
    
        table.setRowCount(1)
        table.setColumnCount(len(result))
        table.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])

        # Fill the table with data
        for col_index, col_value in enumerate(result):
            table.setItem(0, col_index, QTableWidgetItem(str(col_value)))
            
    # Resize the columns to content
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    # Set the size policy for the table
        table.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        table.setMaximumSize(610, table.verticalHeader().defaultSectionSize() + 60)
        
# buttons book nad sec stsec hosetly 

        # Add buttons to the student page
        table_widget = QWidget()
        table_layout = QVBoxLayout(table_widget)
        table_layout.addWidget(table)
        table_layout.setAlignment(QtCore.Qt.AlignCenter)  # Align table in the center
        layout.addWidget(table_widget, alignment=Qt.AlignCenter)

        layout.addWidget(table)

        # Add buttons to the student page
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

        # Align buttons to the bottom-center
        button_widget = QWidget()
        button_widget.setLayout(button_layout)
        layout.addWidget(button_widget, alignment=QtCore.Qt.AlignBottom)
        
        buttonstu_section.clicked.connect(self.show_section_data)
        buttonstu_book.clicked.connect(lambda: self.show_borrowed_books(result[0]))  # Assuming result[0] is the student ID

    # Add student page widget to stacked widget
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
                    SELECT STSEC.* , SECTION.*
                    FROM STSEC
                    JOIN SECTION ON STSEC.SECTION_SECID = SECTION.SECID
                    WHERE STSEC.STUDENT_ENROLLMENT_STID = %s
                """
                cursor.execute(query, (self.lineEdit_username.text(),))
                results = cursor.fetchall()

                # Close the database connection
                connection.close()
                

                # Create a new widget to display section data
                section_page = QWidget()
                layout = QVBoxLayout(section_page)
                
                title = QLabel("Section Page")
                title.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
                title.setStyleSheet(
        '''
        font-size: 30px;
        color: purple;
        border: 2px solid black;
        background-color: #FFC0CB;  /* light pink background color */
        padding: 10px;
        '''
    )
                title.setMaximumSize(700 , 80)
                layout.addWidget(title)
                section_page.setLayout(layout)
                # Add a table to display the data
                section_table = QTableWidget()
                section_table.setStyleSheet("background-color: #9F86C0; border: 3px solid #231942;")

                # Adjusting the cell font
                section_table.horizontalHeader().setStyleSheet("font-size: 15px; color: white;")

                if results:
                    section_table.setRowCount(len(results))
                    section_table.setColumnCount(len(results[0]))
                    section_table.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])

                    # Fill the table with data
                    for row_index, row_data in enumerate(results):
                        for col_index, col_value in enumerate(row_data):
                            section_table.setItem(row_index, col_index, QTableWidgetItem(str(col_value)))

                    # Resize the columns to content
                    section_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

                    # Set the size policy for the table
                    section_table.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    section_table.setMaximumSize(1190, section_table.verticalHeader().defaultSectionSize() * len(results) + 50)

                else:
                    # Handle case where no data was found
                    msg = QMessageBox()
                    msg.setText('No section data found for the student.')
                    msg.exec_()

                layout.addWidget(section_table)
                self.stacked_widget.addWidget(section_page)
                self.stacked_widget.setCurrentWidget(section_page)

               
                

        except Error as e:
            print(f"Error retrieving data: {e}")
            # Handle error, show message box or log error
            
    def show_borrowed_books(self, student_id):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                SELECT BOOK.NAME , LIBRARY_has_BOOK.BOOK_ISBN , BORROWS.TAKE_DATE, BORROWS.RETURN_DATE
                FROM BORROWS
                JOIN LIBRARY_has_BOOK ON BORROWS.LIBRARY_has_BOOK_BOOKID = LIBRARY_has_BOOK.BOOKID
                JOIN BOOK on LIBRARY_has_BOOK.BOOK_ISBN = BOOK.ISBN
                WHERE BORROWS.STUDENT_ENROLLMENT_STID = %s
            """
            cursor.execute(query, (student_id,))
            borrowed_books = cursor.fetchall()
            connection.close()

            # Display the borrowed books in a new table
            borrowed_books_page = QWidget()
            layout = QVBoxLayout(borrowed_books_page)

            borrowed_books_table = QTableWidget()
            borrowed_books_table.setStyleSheet("background-color: #9F86C0; border: 2px solid #231942;")
            borrowed_books_table.setRowCount(len(borrowed_books))
            borrowed_books_table.setColumnCount(4)
            borrowed_books_table.setHorizontalHeaderLabels(["NAME", "BOOKID" , "BORROW DATE", "RETURN DATE"])

            # Fill the table with borrowed books data
            for row_index, row_data in enumerate(borrowed_books):
                for col_index, col_value in enumerate(row_data):
                    borrowed_books_table.setItem(row_index, col_index, QTableWidgetItem(str(col_value)))

            borrowed_books_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            borrowed_books_table.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            borrowed_books_table.setMaximumSize(800, 400)  # Adjust as needed

            layout.addWidget(borrowed_books_table)
            self.stacked_widget.addWidget(borrowed_books_page)
            self.stacked_widget.setCurrentWidget(borrowed_books_page)     
        
        
        
        
        
        
        
        
        
        
        
        

    def professor_page(self, cursor, result):
         # Create a new widget to display user data
        user_page = QWidget()
        layout = QVBoxLayout(user_page)

        # Add a table to display the data
        table = QTableWidget()
        table.setStyleSheet("background-color: #9F86C0; border: 3px solid #231942;")

        # Adjusting the cell font
        table.horizontalHeader().setStyleSheet("font-size: 15px; color: white;")

        table.setHorizontalHeaderLabels(["PROF_ID" , "NAME" ,"SALARY" , "DEPARTMENT" , "PHONE"])
    
        table.setRowCount(1)
        table.setColumnCount(len(result)-3)
        table.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])

        # Fill the table with data
        for col_index, col_value in enumerate(result):
            table.setItem(0, col_index, QTableWidgetItem(str(col_value)))
            
    # Resize the columns to content
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    # Set the size policy for the table
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
