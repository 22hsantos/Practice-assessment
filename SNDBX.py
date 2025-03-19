''' 
This program allows the user to access 
and modify student NCEA data through the menu.
'''

#List of all students
student_list = [['Sue DidntPass', 11, 3, 4, 6], 
                ['Richard DidPass', 12, 40,10, 10],
                ['Mary Gotexcellence', 13, 0, 0,80]]


#Prints all students and credits- working
def all_students():
    for student in student_list:
        print(f'''
{student[0]}\n
Year {student[1]}\n
{student[2]} credits in Achieved\n
{student[3]} credits in Merit\n
{student[4]} credits in Excellence\n ''')


#main menu
def menu():
    while True:
        menu_input = input(
            '''
NCEA Student Qualification Portal\n
1. All Student Data\n
2. All Passing Students\n
3. All Endorsed Students\n
4. Student Summary\n
5. Adjust Credits\n
6. Add new Student data.\n
>''').strip()
        
        if menu_input == '1':
            all_students()
            break
        if menu_input == '2':
            passing_students()
            break
        if menu_input == '3':
            endorsed_students()
            break
        if menu_input == '4':
            summary_menu()
            break
        if menu_input == '5':
            adjust_credit()
            break
        if menu_input == '6':
            add_student_data()
            break
        else:
            print('Please enter a valid input.')


all_students()