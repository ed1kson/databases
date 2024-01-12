import sqlite3

db_name = 'my_db.db'

conn = sqlite3.connect(db_name, check_same_thread=False)
cursor = conn.cursor()

#funcs
def func1(func):
    def wrapper(name, age, major):
        func(name, age, major)
        print('excellent! Student added.')
    return wrapper

def func2(func):
    def wrapper(course_name, instructor):
        func(course_name, instructor)
        print('excellent! Student added.')
    return wrapper 

def func3(func):
    def wrapper(student_name, course_name):
        func(student_name, course_name)
        print('excellent!!!')
    return wrapper 

def func4(func):
    def wrapper():
        students = func()
        print(students)
    return wrapper

def func5(func):
    def wrapper():
        courses = func()
        print(courses)
    return wrapper

def func6(func):
    def wrapper(course_name):
        students = func(course_name)
        print(students)
        
@func1
def new_student(name, age, major):
    cursor.execute('''
    INSERT INTO students (name, age, major)
    VALUES(?, ?, ?)
    ''', (name, age, major))

@func2
def new_course(course_name, instructor):
    cursor.execute('''
    INSERT INTO courses (course_name, instructor)
    VALUES(?, ?)
''', (course_name, instructor))

@func3
def add_student_to_course(student_name, course_name):
    cursor.execute('''
    INSERT INTO courses (student_id, course_id)
    VALUES((SELECT id FROM students WHERE name = (?)), (SELECT course_id FROM courses WHERE course_name=(?)))
''', (student_name, course_name))

@func4
def get_students_info():
    cursor.execute('SELECT name, major FROM students')
    return cursor.fetchall()

@func5
def get_courses_info():
    cursor.execute('SELECT name, instructor FROM courses')
    return cursor.fetchall()

@func6
def get_students_by_course(course_name):
    cursor.execute('''
    SELECT name, major FROM students WHERE id = (SELECT student_id FROM relation_table WHERE course_id = (SELECT course_id FROM courses WHERE course_name = (?)))
    ''', course_name)
    return cursor.fetchall()


