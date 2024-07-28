from datetime import datetime as dt
from pickle import dump
from pickle import load
from os import system
from statistics import mean
clear =lambda:system("cls")
active_students=[]
graduated_students=[]
try :
    with open("active_student.info","rb") as m:
        active_students = load(m)
    with open("graduated_student.info","rb") as o:
        graduated_students = load(o)
except(FileNotFoundError):
    active_students=[]
    graduated_students=[]
def check_codemelli(c):
    for i in active_students:
        if len(c)!=10:
            return False
        elif i['code_melli']==c:
            return False
    else:
        if len(c)!=10:
            return False
        else:
            return True
def check_studentcode(a):
    for i in active_students:
        if len(str(a))!=9:
            return False
        elif i['student_code']==a :
            return False
    else :
        if len(str(a))!=9:
            return False
        else :
            return True
def add_student():
    courses_list=[]
    grade_list=[]
    clear()
    student_dict={}
    print("-----------------------------------------------------------------")
    student_dict["first_name"]=input("please enter student first name: ")
    student_dict["last_name"]=input("please enter student last name: ")
    while True:
        try:
            a=input("please enter student birthday(Gregorian)(format is YYYY/MM/DD): ")
            student_dict["birthday"]=dt.strptime(a,"%Y/%m/%d")
            break
        except(ValueError):
            print("format YYYY/mm/dd didnt matched!!!")
    while True:
        try:
            temp1=input("please enter student's code melli:  ")
            code_temp=temp1
            int(temp1)
            if check_codemelli(code_temp)==False:
                print("code melli is not 10 digit or repeated!!!")
            else:
                student_dict["code_melli"]=code_temp
                break
        except(ValueError):
            print("code melli must be number only!!!")
            continue
    while True:
        try:
            l=int(input("please enter student code: "))
            if check_studentcode(l)==False:
                print("student code must be 9 digit or it is reapeted!!!")
                continue
            else:
                student_dict["student_code"]=l
                break
        except(ValueError):
            print("student code must be digit only!!!")
    while True:
        temp1=input("please enter student courses: ")
        courses_list.append(temp1)
        choice_course1=input("do you want to add another  course y/n:  ").upper()
        if choice_course1=="N":
            print("your courses is:\n",courses_list)
            break
        elif choice_course1 == "Y":
            print("###################################################################")
            continue
        else:
            print("wrong input!!!")
    student_dict.setdefault("courses",courses_list)
    for h in courses_list:
        while True:
            try:
                temp2=int(input("please enter student grade(grades must be related to courses!!!): "))
                if temp2>20:
                    print("grades must be 20 or under it!!!")
                    continue
                else :
                    break
            except(ValueError):
                print("grades must be digit!!!")
        grade_list.append(temp2)
    print("your grades are:\t",grade_list)
    student_dict.setdefault("grades",grade_list)
    active_students.append(student_dict)
    print("--------------------------------------------------------------------------")
    input("enter any key:\t")
def find_student():
    clear()
    try:
        find_student=int(input("please enter student_code to find student:\t"))
    except(ValueError):
        print("student code must be digit only!!!")
        input("enter eny key:\t")
        return False
    if len(str(find_student))!=9:
        print("student code must be 9 digit!!!")
        input("press any key:\t")
        return False
    choice_find=input("for searching in active_students enter A and searching in graduated-sudents enter G:\t").upper()
    if choice_find == "A":
        for k in active_students:
            if  find_student == k['student_code']:
                print("student found !!!")
                print("=========================================")
                print(f"first name:\t     {k['first_name']}")
                print(f"last name:\t      {k['last_name']}")
                print(f"birthday:\t       {k['birthday']}")
                print(f"code melli:\t     {k['code_melli']}")
                print(f"student code:\t   {k['student_code']}")
                print(f"student courses:\t{k['courses']}")
                print(f"grades:\t         {k['grades']}")
                print("===========================================")
                break
        else:
            print("no student found in active_student !!!")
    elif choice_find=="G":
        for x in active_students:
            if  find_student == x['student_code']:
                print("student found !!!")
                print("=========================================")
                print(f"first name:\t     {x['first_name']}")
                print(f"last name:\t      {x['last_name']}")
                print(f"birthday:\t       {x['birthday']}")
                print(f"code melli:\t     {x['code_melli']}")
                print(f"student code:\t   {x['student_code']}")
                print(f"student courses:\t{x['courses']}")
                print(f"grades:\t         {x['grades']}")
                print("===========================================")
                break
        else:
            print("no student found in graduated_students!!! ")
    else:
        print("wrong input!!!")
    input("press any key!\t")
def delete_student():
    clear()
    try:
        student_delete=int(input("please enter student code you want to delete:\t"))
    except(ValueError):
        print("student code must be digit!!!")
        input("press any key:\t")
        return False
    if len(str(student_delete))!=9:
        print("student code must be 9 digit!!!")
        input("press any key:\t")
        return False
    for i in active_students:
        if  student_delete == i['student_code']:
            print("student found !!!")
            print("=========================================")
            print(f"first name:\t     {i['first_name']}")
            print(f"last name:\t      {i['last_name']}")
            print(f"birthday:\t       {i['birthday']}")
            print(f"code melli:\t     {i['code_melli']}")
            print(f"student code:\t   {i['student_code']}")
            print(f"student courses:\t{i['courses']}")
            print(f"grades:\t         {i['grades']}")
            print("===========================================")
            print("do you want to delete this student or move it to graduated student?\n")
            choice_delete1=input("for moving enter M and for deleting enter D:\t").upper()
            if choice_delete1 == "D":
                print("are you sure you want to delete this student???")
                choice_delete2=input("enter y/n:").upper()
                if choice_delete2 == "N":
                    input("press any key:\t")
                    return False
                elif choice_delete2 == "Y":
                    active_students.remove(i)
                    print("student has been deleted succesfully!")
                    break
                else :
                    print("wrong input!!!")
            elif choice_delete1 == "M":
                print("are you sure you want to move this student???")
                choice_delete3=input("enter y/n:\t").upper()
                if choice_delete3 == "N":
                    input("press any key:\t")
                    return False
                elif choice_delete3 == "Y":
                    graduated_students.append(i)
                    active_students.remove(i)
                    print("student has been moved succesfully!!")
                    break
                else :
                    print("wrong input!!!")
            else:
                print("wrong input!!!!")
            break
    else :
        print("student not found!!!!")
    input("press any key:\t")
def edit_student():#kharab ast bayad dorost shavad
    clear()
    temp_grade=[]
    temp_courses=[]
    try:
        student_edit=int(input("enter student code for edit courses and grades:\t"))
    except(ValueError):
        print("student score must be digit!!")
        input("press any key:\t")
        return False
    if len(str(student_edit))!=9:
        print("student code must be 9 digit!!!")
        input("press any key:\t")
        return False
    for i in active_students:
        if  student_edit == i['student_code']:
            print("student found !!!")
            print("===========================================")
            print(f"first name:\t     {i['first_name']}")
            print(f"last name:\t      {i['last_name']}")
            print(f"birthday:\t       {i['birthday']}")
            print(f"code melli:\t     {i['code_melli']}")
            print(f"student code:\t   {i['student_code']}")
            print(f"student courses:\t{i['courses']}")
            print(f"grades:\t         {i['grades']}")
            print("===========================================")
            temp_grade.append(i['grades'])
            temp_courses.append(i['courses'])
            grade_list=(temp_grade[0])
            courses_list=(temp_courses[0])
            while True:
                choice_edit=input("enter C for courses and G for grade:\t").upper()
                if choice_edit == "C":
                    print("do you want to change course or add course???")
                    edit1=input("enter C for change course and A for add course and D for delete course:\t").upper()
                    if edit1 == "A":
                        new1=input("enter course name you want to add:")
                        courses_list.append(new1)
                        print(courses_list)
                        try:
                            new2=int(input("enter grade :"))
                            if new2>20:
                                print("grade must be 20 or less!!")
                                input("press any key:\t")
                                continue
                            else:
                                grade_list.append(new2)
                        except(ValueError):
                            print("grade must be digit!!!")
                            input("enter any key:\t")
                            continue
                    elif edit1 == "C":
                        edit_temp1=input("enter course name you want to change:\t")
                        edit_temp2=input("enter the name you want to alter perevious course name:\t")
                        for j in courses_list:
                            if j==edit_temp1:
                                index1=courses_list.index(j)
                                courses_list.insert(index1,edit_temp2)
                                courses_list.remove(edit_temp1)
                                print("course has been changed sucessfully!")
                                break
                        else :
                            print("course name that you wanna change is wrong")
                            input("press any key:\t")
                            return False
                    elif edit1=="D":
                        edit_delete=input("enter course name you wanna delete(grade also will be deleted):\t")
                        for t in courses_list:
                            if t==edit_delete:
                                index2=courses_list.index(t)
                                courses_list.remove(edit_delete)
                                grade_list.pop(index2)
                                print("course has been deleted!!!")
                                break
                        else:
                            print("course name not found!!!")
                            input("press any key:\t")
                            return False
                    else:
                        print("choice must be A or C or D !!!")
                        input("press any key!!!")
                        return False
                elif choice_edit == "G":
                        edit_temp4=input("enter course name you want to change its grade:\t")
                        try:
                            edit_temp5=int(input("enter the grade :\t"))
                            if edit_temp5>20:
                                print("grade must be 20 or less!!!")
                                input("press any key:\t")
                                continue
                        except(ValueError):
                            print("grade must be digit only!!")
                            input("press any key!!")
                            return False
                        for j in courses_list:
                            if j==edit_temp4:
                                index=courses_list.index(j)
                                grade_list.pop(index)
                                grade_list.insert(index,edit_temp5)
                                print("course has been changed sucessfully!")
                                break
                        else :
                            print("course name that you wanna change is wrong")
                else:
                    print("choice must be c or g!!!")
                    input("press any key:\t")
                    continue
                check_test=input("do you want to edit more y/n:\t").upper()
                if check_test=="Y":
                    continue
                elif check_test=="N":
                    break
                else:
                    print("choice must be y or n!!!")
            i['courses']=courses_list
            i['grades']=grade_list
            break
    else:
        print("student not found!!")
        input("press any key:\t")
    input("press any key:\t")
def list_student():
    clear()
    choice_list=input("which list do you want to see? \n for active_student enter A and for graduated_student enter G:  ").upper()
    if choice_list=="A":
        for i in active_students:
            print("=========================================")
            print(f"first name:\t     {i['first_name']}")
            print(f"last name:\t      {i['last_name']}")
            print(f"birthday:\t       {i['birthday']}")
            print(f"code melli:\t     {i['code_melli']}")
            print(f"student code:\t   {i['student_code']}")
            print(f"student courses:\t{i['courses']}")
            print(f"grades:\t         {i['grades']}")
            print("===========================================")
    elif choice_list == "G":
        for j in graduated_students:
            print("=========================================")
            print(f"first name:\t     {j['first_name']}")
            print(f"last name:\t      {j['last_name']}")
            print(f"birthday:\t       {j['birthday']}")
            print(f"code melli:\t     {j['code_melli']}")
            print(f"student code:\t   {j['student_code']}")
            print(f"student courses:\t{j['courses']}")
            print(f"grades:\t         {j['grades']}")
            print("===========================================")
    else:
        print("choice must be A or G!!!")
        input("press any key:\t")
        return False
    input("press any key:\t")
def more_information():
    clear()
    temp_grade=[]
    temp_courses=[]
    try:
        more_student=int(input("please enter student_code:\t"))
        if len(str(more_student))!=9:
            print("student code must be 9 digit!!!")
            input("press any key:\t")
            return False
    except(ValueError):
        print("student code must be digit only!!!")
        input("enter eny key:\t")
        return False
    for u in active_students:
        if  more_student == u['student_code']:
            print("student found !!!")
            print("=========================================")
            print(f"first name:\t     {u['first_name']}")
            print(f"last name:\t      {u['last_name']}")
            print(f"birthday:\t       {u['birthday']}")
            print(f"code melli:\t     {u['code_melli']}")
            print(f"student code:\t   {u['student_code']}")
            print(f"student courses:\t{u['courses']}")
            print(f"grades:\t         {u['grades']}")
            print("===========================================")
            temp_grade.append(u['grades'])
            temp_courses.append(u['courses'])
            grade_list=(temp_grade[0])
            courses_list=(temp_courses[0])
            courses_grades=dict(zip(courses_list,grade_list))
            input("press any key:\t")
            clear()
            print("student courses and grades are :\t",courses_grades)
            max_info=max(grade_list)
            min_info=min(grade_list)
            mean_info=mean(grade_list)
            time_now=dt.now().year
            time_user1=u['birthday']
            time_user2=time_user1.year
            time=time_now-time_user2
            print("=======================================")
            print("maximum os this student grades is:")
            print(max_info)
            print("=======================================")
            print("minimum of this student grades is:")
            print(min_info)
            print("=======================================")
            print("average grades of this student is:")
            print(round(mean_info,3))
            print("=======================================")
            print("age of the student is:")
            print(time)
            print("=======================================")
            break
    else:
        print("no student found in active_student !!!")
    input("press any key:\t")
def save_student():
    clear()
    try:
        with open("active_student.info","wb") as active_student:
            dump(active_students,active_student)
            print("active students saved succesfully!!!!")
        with open("graduated_student.info","wb") as graduated_student:
            dump(graduated_students,graduated_student)
            print("graduated students saved succesfully!!!!")
    except(PermissionError):
        print("select another place!!")
    input("press any key!!")