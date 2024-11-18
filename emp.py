from os import system
import re
import mysql.connector
con=mysql.connector.connect(
    host="localhost",user="root",password="anitha",database="Employee")
#make a regular expression
#for validating an Email
regax=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
Pattern=re.compile(r"(0|91)?[7-9][0-9]{9}")
#function to Add_Employ
def Add_Employ():
    print("{:>60}".format("-->> Add Employee Record <<--"))
    Id=input("Enter Employee Id:")
    if(check_employee(Id)==True):
        print("Employee ID Already Exists\nTry Again..")
        press=input("Press Any Key To Continue..")
        Add_Employ()
    #checking if employee name is exit or not
    Name=input("Enter Employee Name:")
    if(check_employee_name(Name)==True):
        print("Employee Already Exists\n Try Again..")
        press=input("Press Any Key To Continue..")
        Add_Employ
    Email_Id=input("Enter Employee Email ID:")
    if(re.fullmatch(regax,Email_Id)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press=input("Press Any Key To Continue..")
        Update_Employ()
    Phone_no=input("Enter Employee Phone No:")
    if(Pattern.match(Phone_no)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press=input("Press Any Key To Continue..")
        Update_Employ()
    Address=input("Enter Employee Address:")
    Post=input("Enter Employee Post:")
    Salary=input("Enter Employee Salary:")
    data=(Id,Name,Email_Id,Phone_no,Address,Post,Salary)

    sql="insert into empdata values(%s,%s,%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Successfully Added Employee Record")
    press=input("Press Any key To Continue..")
    menu()
# Funtion to Check if Employee with given Name Exist or not
def check_employee_name(employee_name):
    sql='select * from empdata where Name=%s'
    c=con.cursor(buffered=True)
    data=(employee_name,)
    c.execute(sql,data)
    r=c.rowcount
    if r==1:
        return True
    else:
        return False
#Function To check if Employee With
#given Id Exist or not
def check_employee(employee_id):
    sql='select * from empdata where Id=%s'
    c=con.cursor(buffered=True)
    data=(employee_id,)
    c.execute(sql,data)
    r=c.rowcount
    if r==1:
        return True
    else:
        return False
#Function to display_employ
def Display_Employ():
    print("{:>60}".format("-->> Display Employee Record <<--"))
    sql='select * from empdata'
    c=con.cursor()
    c.execute(sql)
    r=c.fetchall()
    for i in r:
        print("Employee Id: ",i[0])
        print("Employee Name: ",i[1])
        print("Employee Email Id: ",i[2])
        print("Employee Phone No: ",i[3])
        print("Employee Address: ",i[4])
        print("Employee Post: ",i[5])
        print("Employee Salary: ",i[6])
        print("\n")
    press=input("Press Any key To Continue..")
    menu()
# Function to update employ
def Update_Employ():
    print("{:>60}".format("-->>Update Employee Record <<--"))
    Id=input("Enter Employee Id:")
    if(check_employee(Id)==False):
        print("Employee ID not Exists\nTry Again..")
        press=input("Press Any Key To Continue..")
        menu()
    else:
        Email_Id=input("Enter Employee Email ID:")
        Phone_no=input("Enter Employee Phone No:")
        Address=input("Enter Employee Address:")
        #updating Employee details in the empdata table
        sql='UPDATE empdata set Email_Id=%s,Phone_no=%s,Address=%s where Id=%s'
        data=(Email_Id,Phone_no,Address,Id)
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Update Employee Record")
        press=input("Press Any key To Continue..")
        menu()
def Promote_Employ():
    print("{:>60}".format("-->>Promote Employee Record <<--"))
    Id=input("Enter Employee Id:")
    if(check_employee(Id)==False):
        print("Employee ID Already Exists\nTry Again..")
        press=input("Press Any Key To Continue..")
        menu()
    else:
        Amount=int(input("Enter Increase Salary"))
        sql='select salary from empdata where Id=%s'
        data=(Id,)
        c=con.cursor()
        c.execute(sql,data)
        r=c.fetchone()
        t=r[0]+Amount
        sql='update empdata set Salary=%s where Id=%s'
        d=(t,Id)
        c.execute(sql,d)
        con.commit()
        print("Employee Promoted")
        press=input("Press Any key To Continue..")
        menu()
# Function to Remove Employ
def Remove_Employ():
    print("{:>60}".format("-->>Promote Employee Record <<--"))
    Id=input("Enter Employee Id:")
    if(check_employee(Id)==False):
        print("Employee ID Not Exists\nTry Again..")
        press=input("Press Any Key To Continue..")
        menu()
    else:
        sql='delete from empdata where Id=%s'
        data=(Id,)
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Employee Removed")
        press=input("Press Any key To Continue..")
        menu()
# Function to search employee
def Search_Employ():
    print("{:>60}".format("-->>Search Employee Record <<--"))
    Id=input("Enter Employee Id:")
    if(check_employee(Id)==False):
        print("Employee Record Not Exists\nTry Again..")
        press=input("Press Any Key To Continue..")
        menu()
    else:
        sql='select * from empdata where Id=%s'
        data=(Id,)
        c=con.cursor()
        c.execute(sql,data)
        r=c.fetchall()
        for i in r:
            print("Employee Id: ",i[0])
            print("Employee Name: ",i[1])
            print("Employee Email Id: ",i[2])
            print("Employee Phone No: ",i[3])
            print("Employee Address: ",i[4])
            print("Employee Post: ",i[5])
            print("Employee Salary: ",i[6])
            print("\n")
    press=input("Press Any key To Continue..")
    menu()
#Menu function to display menu
def menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))
    ch=int(input("Enter your Choice:"))
    if ch==1:
        system("cls")
        Add_Employ()
    elif ch==2:
        system("cls")
        Display_Employ()
    elif ch==3:
        system("cls")
        Update_Employ()
    elif ch==4:
        system("cls")
        Promote_Employ()
    elif ch==5:
        system("cls")
        Remove_Employ()
    elif ch==6:
        system("cls")
        Search_Employ()
    elif ch==7:
        system("cls")
        print("{:>60}".format("Have A Nice Day:"))
        exit(0)
    else:
        print("Invalid Choice")
        press=input("Press Any key To Continue..")
        menu()
menu()