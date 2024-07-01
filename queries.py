import mysql.connector
from PyQt5.QtWidgets import QTableView

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
def Querify(qn):
    match qn:
        case 1:
            Q1()
        case 2:
            Q2()
        case 3:
            Q3()
        case 4:
            Q4()
        case 5:
            Q5()
        case 6:
            Q6()
        case 7:
            Q7()

def Q1():
    cursor.execute(
        f'''
        select student_enrollment_stid from mydb.stsec
        where section_secid in (select secid from mydb.section
            where year = {year}
            and semester = {semester})
        '''
    )
    rows = []
    for row in cursor:
        rows.append(row[0])
        print(row[0])
def Q2():
    cursor.execute(
        f'''
        select course_coid from mydb.section as s
        where year = {year}
        and semester = {semester}
        and 5 < (select count(student_enrollment_stid) from mydb.stsec
            where stsec.section_secid = s.secid)
        '''
    )
    rows = []
    for row in cursor:
        rows.append(row)
        print(row)
def Q3():
    cursor.execute(
        '''
        select stsec.student_enrollment_stid, (sum(stsec.grade * course.credit)/sum(course.credit)) as 'weighted average'
        from course
        inner join section on course.coid = section.course_coid
        inner join stsec on section.secid = stsec.section_secid
        group by stsec.student_enrollment_stid
        '''
    )
    rows = []
    for row in cursor:
        rows.append(row)
        print(row)

def Q4():
    cursor.execute(
        '''
        select * from professor as p
        where 70 < (select sum(credit) from course
            where coid in (select course_coid from section
                where section.professor_prof_id = p.prof_id))
        '''
    )
    rows = []
    for row in cursor:
        rows.append(row)
        print(row)

def Q5():
    cursor.execute(
        '''
        select book.name from book
        where isbn in (select book_isbn from library_has_book as lhb
            where 4 < (select count(distinct student_enrollment_stid) from borrows
                where borrows.library_has_book_bookid = lhb.bookid))
        '''
    )
    rows = []
    for row in cursor:
        rows.append(row)
        print(row)

def Q6():
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
    rows = []
    for row in cursor:
        rows.append(row)
        print(row)

def Q7():
    cursor.execute(
        '''
        select * from student
        where enrollment_stid not in (select student_enrollment_stid from stsec)
        '''
    )
    rows = []
    for row in cursor:
        rows.append(row)
        print(row)

