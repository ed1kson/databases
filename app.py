import main

def output(answer):
    if answer == 1:
        name = input('enter name:')
        age = int(input('enter age:'))
        major = input('major:')
        return main.new_student(name, age, major)
    elif answer == 2:
        course_name = input('enter course name:')
        instructor = input('enter instructor:')
        return main.new_course(course_name, instructor)
    elif answer == 3:
        return main.get_students_info()
    elif answer == 4:
        return main.get_courses_info()
    elif answer == 5:
        student_name = input('enter the students name:')
        course_name = input('enter the courses name:')
        return main.add_student_to_course(student_name, course_name)
    elif answer == 6:
        course_name = input('enter the courses name:')
        return main.get_students_by_course(course_name)
    elif answer == 7:
        table = input('enter table name:')
        id = input('enter id:')
        main.delete_smth(table, id)
        return 'deleted'
    else:
        return 'Please, type down a number from 1 to 8:'
        
run = True

while run:
    print('''
          1. Додати нового студента
          2. Додати новий курс
          3. Показати список студентів
          4. Показати список курсів
          5. Зареєструвати студента на курс
          6. Показати студентів на конкретному курсі
          7. Видалити запис
          8. Вийти''')
    
    answer = int(input('enter your answer please(1-8):'))

    if answer == 8:
        break
    
    print(output(answer))
