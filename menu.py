# V 1.0.0
import python_class.student_operations as so
while True:
    so.clear()
    print("---------------------------------------------------------------------------")
    print("to Add student press A:   ")
    print("to Find and Search a student press F:   ")
    print("to Delete a student press D(also for moving a student to graduated):   ")
    print("to Edit student information press E:  ")
    print("to see the list of student press L:  ")
    print("to Save the student press S:   ")
    print("to Quit the app press Q:   ")
    print("for get more information about student(min,max,...)press M:  ")
    print("---------------------------------------------------------------------------")
    choice = input("your choice is:   ").upper()
    if choice == "A":
        so.add_student()
    elif choice == "F":
        so.find_student()
    elif choice == "D":
        so.delete_student()
    elif choice == "E":
        so.edit_student()
    elif choice == "L":
        so.list_student()
    elif choice == "S":
        so.save_student()
    elif choice == "M":
        so.more_information()
    elif choice == "Q":
        break
    else :
        so.clear()
        print("wrong choice!!!")
        input("press any key:\t")