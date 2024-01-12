import main

def output(answer):
    if answer == 1:
        name = input('enter name')
        age = int(input('enter age'))
        major = input('major')
        main.new_student(name, age, major)
    elif answer == 2:
        course_name = input('enter course name')
        instructor = input('enter instructor')
        main.new_course(course_name, instructor)
    elif answer == 3:
        print(main.get_students_info())
    elif answer == 4:
        print(main.get_courses_info)
    elif answer == 5:
        student_name = input('enter the students name')
        course_name = input('enter the courses name')
        main.add_student_to_course(student_name, course_name)
    elif answer == 6:
        course_name = input('enter the courses name')
        print(main.get_students_by_course)
    else:
        return 'Please, type down a number from 1 to 7'
        
run = True

while run:
    print('''1. Додати нового студента
          2. Додати новий курс
          3. Показати список студентів
          4. Показати список курсів
          5. Зареєструвати студента на курс
          6. Показати студентів на конкретному курсі
          7. Вийти''')
    
    answer = int(input('enter your answer please(1-7)'))

    if answer == 7:
        break
    
    print(output(answer))
    

