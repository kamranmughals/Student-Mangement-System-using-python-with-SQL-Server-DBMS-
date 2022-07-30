student_id = int(input("1. Enter StudentID: "))
            checkID = "select student_id from Student"
            cursor.execute(checkID)
            row = [items[0] for items in cursor.fetchall()]
            print(row)
            if student_id in row: 
                print("This student id is already existed!, try to add another-one")
                student_id = int(input("1. Enter StudentID: "))
            else:
                student_name = str(input("2. Enter StudentName: ")) 
                student_age = str(input("3. Enter StudentAGE: "))
                student_address = str(input("4. Enter Home_Address: "))
                student_phone_number = str(input("5. Enter Phone-Number: "))
                student_father_name =str(input("6. Enter FatherName: "))
                student_roll_number = decimal.Decimal(input("7. Enter StudentROLL#: "))
                student_city =str(input("8. Enter City: "))
                student_registrationNo = decimal.Decimal(input("9. Enter Registration#: "))
                cursor.execute("INSERT INTO Student VALUES(?, ?, ?, ?, ?, ?,?,?,?)", student_id, student_name, student_age
                ,student_address, student_phone_number, student_father_name, student_roll_number, student_city, student_registrationNo)
                cursor.commit()
                print("Row effected!")