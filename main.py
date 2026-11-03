import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='ATTENDANCE'
)

mycursor = mydb.cursor()

q = 'CREATE TABLE IF NOT EXISTS RECORD(RNO INT PRIMARY KEY, NAME VARCHAR(15))'
mycursor.execute(q)


def add_students():
    n = int(input("Enter the number of Students : "))
    try:
        for i in range(n):
            rno = int(input("Enter Roll No. : "))
            name = input("Enter name : ")
            q = 'INSERT INTO RECORD(RNO, NAME) VALUES(%s,"%s")' % (rno, name)
            mycursor.execute(q)
        mydb.commit()
        print("Success")
    except:
        print("Roll Number Already Exists")
        ch = input("Want to continue (y/n)? ")
        if ch == 'y':
            add_students()


def stud_list():
    q = 'SELECT * FROM RECORD'
    mycursor.execute(q)
    data = mycursor.fetchall()
    print("Roll No.\tName")
    for i in data:
        print(i[0], '\t\t', i[1])


def update_student():
    rno = int(input("Enter the Roll No. : "))
    q = 'SELECT * FROM RECORD'
    mycursor.execute(q)
    data = mycursor.fetchall()
    record_found = False

    for i in data:
        if rno == i[0]:
            name = input("Enter the Updated Name : ")
            q = 'UPDATE RECORD SET NAME = "%s" WHERE RNO = %s' % (name, rno)
            mycursor.execute(q)
            mydb.commit()
            print("Record Updated")
            record_found = True
            break

    if not record_found:
        print("Roll Number Does Not Exist")


def mark_attend():
    q = 'SELECT * FROM RECORD'
    mycursor.execute(q)
    data = mycursor.fetchall()
    date = input("Enter date (DDMMYYYY) : ")
    d = 'D' + date
    q = 'ALTER TABLE RECORD ADD COLUMN %s VARCHAR(15)' % (d,)
    mycursor.execute(q)

    for i in range(len(data)):
        rno = int(input("Enter Roll No. : "))
        status = input("Enter Status (P/A) : ")
        q = 'UPDATE RECORD SET %s = "%s" WHERE RNO = %s' % (d, status, rno)
        mycursor.execute(q)
        mydb.commit()

    print('Record Added')


def update_attend():
    date = input("Enter date (DDMMYYYY) : ")
    d = 'D' + date
    rno = int(input("Enter the Roll No. : "))
    q = 'SELECT * FROM RECORD'
    mycursor.execute(q)
    data = mycursor.fetchall()
    record_found = False

    for i in data:
        if rno == i[0]:
            status = input("Enter Status (P/A) : ")
            q = 'UPDATE RECORD SET %s = "%s" WHERE RNO = %s' % (d, status, rno)
            mycursor.execute(q)
            mydb.commit()
            print("Record Updated")
            record_found = True
            break

    if not record_found:
        print("Roll Number Does Not Exist")


def absent():
    date = input("Enter date (DDMMYYYY) : ")
    d = 'D' + date
    q = 'SELECT * FROM RECORD WHERE %s = "A"' % (d,)
    mycursor.execute(q)
    data = mycursor.fetchall()
    mydb.commit()

    for i in data:
        print(i[1])


def total_days():
    q = 'SELECT * FROM RECORD'
    mycursor.execute(q)
    data = mycursor.fetchall()
    total = len(data[0]) - 2
    print('Total Working Days : ', total)
    mydb.commit()


def attend():
    count = 0
    name = input("Enter the name of student : ")
    q = 'SELECT * FROM RECORD'
    mycursor.execute(q)
    data = mycursor.fetchall()
    total = len(data[0]) - 2

    for i in data:
        if i[1] == name:
            for j in i:
                if str(j) == 'P':
                    count += 1

    print("Total Working Days : ", total)
    print('No of Days', name, 'was present : ', count)
    print("%age : ", (count / total) * 100)


while True:
    print('****STUDENT ATTENDANCE MANAGEMENT****')
    print('''
    1. Add Students
    2. Student List
    3. Update Student Name
    4. Add Attendance
    5. Update Attendance
    6. Absentees
    7. Total Working Days
    8. Calculate Attendance of a Student
    9. Exit
    ''')

    choice = int(input("Enter Choice : "))

    if choice == 1:
        add_students()
    elif choice == 2:
        stud_list()
    elif choice == 3:
        update_student()
    elif choice == 4:
        mark_attend()
    elif choice == 5:
        update_attend()
    elif choice == 6:
        absent()
    elif choice == 7:
        total_days()
    elif choice == 8:
        attend()
    elif choice == 9:
        break
    else:
        print('Invalid Choice')
        break
