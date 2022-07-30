from cProfile import label
import os
import time
from turtle import goto
from tabulate import tabulate
import pyodbc

con = pyodbc.connect('Driver={SQL SERVER}; SERVER=DESKTOP-AVT89QG; DATABASE=students; Trusted_Connection:yes;')
cursor = con.cursor()

# Creating table using sql queries 
def CreateTable():
    stmt = "select TABLE_NAME from INFORMATION_SCHEMA.TABLES"
    cursor.execute(stmt)
    check = cursor.fetchall()
    if check:
        print("Table existed!")
        
    else:
        print("Do you want to create Student Table? -> (y/n): ")
        choice = str(input(""))
        if(choice == "y"):
            print("Creating table.....")
            print("Command completed successfully")
            print("Table is created!")
            cursor.execute("create table Student(\
                student_id int primary key,\
                student_name varchar(55),\
                student_age varchar(55),\
                student_address varchar(55),\
                student_phone_number varchar(55),\
                student_father_name varchar(55),\
                student_roll_number varchar(55) not null UNIQUE,\
                student_city varchar(55),\
                student_registrationNo varchar(55) not null UNIQUE);")
            cursor.commit()
        else:
            print("exiting program........please wait")
            time.sleep(0.5)
            exit()
# get data from user to fill-up table in sql server
def getTableData():
            # os.system("cls")
            student_id = int(input("1. Enter StudentID: "))
            checkID = "select student_id from Student"
            cursor.execute(checkID)
            row = [items[0] for items in cursor.fetchall()]
            if student_id in row: 
                print("This student id is already existed!, try to add another-one")
                getTableData()
            else:
                student_name = str(input("2. Enter StudentName: ")) 
                student_age = str(input("3. Enter StudentAGE: "))
                student_address = str(input("4. Enter Home_Address: "))
                student_phone_number = str(input("5. Enter Phone-Number: "))
                student_father_name =str(input("6. Enter FatherName: "))
                student_roll_number = str(input("7. Enter StudentROLL#: "))
                student_city =str(input("8. Enter City: "))
                student_registrationNo = str(input("9. Enter Registration#: "))
                # cursor.execute("select student_registrationNo from Student")
                # regis = [items[0] for items in cursor.fetchall()]
                # print(regis)
                # label .begin
                # if student_registrationNo in regis:
                #             print("This student Registraton_NO# is already existed!, try to add another-one")
                #             goto .begin
                # else:
                cursor.execute("INSERT INTO Student VALUES(?, ?, ?, ?, ?, ?,?,?,?)", student_id, student_name, student_age
                            ,student_address, student_phone_number, student_father_name, student_roll_number, student_city, student_registrationNo)
                cursor.commit()
                print("\nRow effected!\n")
# Display all record to check data of a paticular student
def ShowData():
            os.system("cls")
            table_data = cursor.execute("SELECT * FROM Student")
            table_field_name = ["Student_ID",
                                "Student_Name", "Student_Age", "Student_Address", "Phone-Number",
                                "Father-Name", "StudentRoll#", "Student_City", "Registration-No#"]
            print(tabulate(table_data, headers=table_field_name, tablefmt="grid", showindex="always", numalign="left", disable_numparse=True))
#Update student record to facilitate the admin
def UpdateTable():
            os.system("cls")
            ShowData()
            student_id = int(input("1. Enter StudentID to update his/her data: "))
            checkID = "select student_id from Student"
            cursor.execute(checkID)
            row = [items[0] for items in cursor.fetchall()]
            if student_id in row:
                print("\n Note: our administration system allows only these attributes to update such as:\n")
                print("1. Student Re-Name")
                print("2. Student Phone-Number#")
                print("3. Student ID-Number#\n")
                choice = int(input("+> Choice : "))
                if(choice == 1):
                    student_name = str(input("Re-Name Student: "))
                    cursor.execute("UPDATE Student SET student_name= ? WHERE student_id = ?", student_name, student_id)
                    cursor.commit()
                    ShowData()
                    print("\n Student name has been updated successfully (s)\n")
                elif(choice == 2):
                    student_number = str(input("New Phone-Number: "))
                    cursor.execute("UPDATE Student SET student_phone_number= ? WHERE student_id = ?", student_number, student_id)
                    cursor.commit()
                    ShowData()
                    print("\n Student Phone-Number# has been updated successfully (s)\n")
                elif(choice == 3):
                    student_new_id = str(input("Assigning-New ID of Student: "))
                    cursor.execute("UPDATE Student SET student_id= ? WHERE student_id = ?", student_new_id, student_id)
                    cursor.commit()
                    ShowData()
                    print("\n Student ID# has been updated successfully (s)\n")
            else:
                    print("\nNo record found against this student_id, please try to enter relevent ID, contact administrator!.\n")
# Truncate table will remove all the data from Table
def TruncateTable():
    cursor.execute("TRUNCATE TABLE Student")
    cursor.commit()
    print("\nAll the data in server has been deleted successfully (s)\n")
# Search a specific studet in a database
def SearchByID():
            os.system("cls")
            student_id = int(input("1. Enter StudentID to search his/her data: "))
            checkID = "select student_id from Student"
            cursor.execute(checkID)
            row = [items[0] for items in cursor.fetchall()]
            if student_id in row:
                        print("Success!!")
                        table_data = cursor.execute("SELECT * FROM Student WHERE student_id = ?", student_id)
                        table_field_name = ["Student_ID",
                                            "Student_Name", "Student_Age", "Student_Address", "Phone-Number",
                                            "Father-Name", "StudentRoll#", "Student_City", "Registration-No#"]
                        print(tabulate(table_data, headers=table_field_name, tablefmt="grid", showindex="always", numalign="left", disable_numparse=True))
            else:
                print("\nNo record found against this student_id, please try to enter relevent ID, contact administrator!.\n")
def DeleteByID():
            os.system("cls")
            ShowData()
            student_id = int(input("1. Enter StudentID to delete his/her data: "))
            checkID = "select student_id from Student"
            cursor.execute(checkID)
            row = [items[0] for items in cursor.fetchall()]
            if student_id in row:
                    print("Success!!")
                    cursor.execute("DELETE FROM Student WHERE student_id = ?", student_id)
                    cursor.commit()
                    ShowData()
                    print("\nStudent has been removed from our administration system!\n")
            else:
                print("\nNo record found against this student_id, please try to enter relevent ID, contact administrator!.\n")

def DropTable():
    cursor.execute("DROP TABLE Student")
    cursor.commit()
    # DropTable()
def main():
    os.system("cls")
    CreateTable()
    while 1:
        print("\n <+ Student Management Panel +> \n")
        print(" +>  1. Add Student Record")
        print(" +>  2. Show All Record")
        print(" +>  3. Update Student Records")
        print(" +>  4. Delete Records by ID")
        print(" +>  5. Search Record by ID")
        print(" +>  6. Truncate Table/Erase all data")
        print(" +>  7. Drop Table in DataBase")
        choice = int(input("==> Choice: "))
        if(choice == 1):
            os.system("cls")
            getTableData()
            os.system("pause")
        elif choice == 2:
            ShowData()
            os.system("pause")
        elif choice == 3:
            UpdateTable()
            os.system("pause")
        elif choice == 4:
            DeleteByID()
            os.system("pause")
        elif choice == 5:
            SearchByID()
            os.system("pause")
        elif choice == 6:
            TruncateTable()
            os.system("pause")
        elif choice == 7:
            DropTable()
            os.system("pause")
        else:
            print("ERROR: server connection has been expired!")
main()
