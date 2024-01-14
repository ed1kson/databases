import sqlite3

db_name = 'my_db.db'

conn = sqlite3.connect(db_name, check_same_thread=False)
cursor = conn.cursor()
#creating tables

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20),
    age INT,
    major TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses(
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name VARCHAR(100),
    instructor VARCHAR(60)
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS relation(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INT,
    student_id INT,
    FOREIGN KEY(course_id) REFERENCES courses(course_id),
    FOREIGN KEY(student_id) REFERENCES students(id)
)''')
conn.commit()

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
        return students
    return wrapper

def func5(func):
    def wrapper():
        courses = func()
        return courses
    return wrapper

def func6(func):
    def wrapper(course_name):
        students = func(course_name)
        return students
    return wrapper
        
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
    conn.commit()

@func3
def add_student_to_course(student_name, course_name):
    cursor.execute('''
    INSERT INTO relation (student_id, course_id)
    VALUES((SELECT id FROM students WHERE name = (?)), (SELECT course_id FROM courses WHERE course_name=(?)))
    ''', (student_name, course_name))
    conn.commit()

@func4
def get_students_info():
    cursor.execute('SELECT name, age, major FROM students')
    return cursor.fetchall()
    
@func5
def get_courses_info():
    cursor.execute('SELECT * FROM courses')
    return cursor.fetchall()

@func6
def get_students_by_course(course_name):
    cursor.execute('''
    SELECT name, age, major FROM students WHERE id IN (SELECT student_id FROM relation WHERE course_id = (SELECT course_id FROM courses WHERE course_name = (?)))
    ''', (course_name,))
    return cursor.fetchall()

def delete_smth(column_name, id):
    cursor.execute(f'''
    DELETE FROM {column_name} WHERE id = (?)
    ''', id)
    conn.commit()

def student_is_there(student_name):
    cursor.execute
