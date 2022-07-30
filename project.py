
import time
import pyodbc

con = pyodbc.connect('Driver={SQL SERVER}; SERVER=DESKTOP-AVT89QG; DATABASE=students; Trusted_Connection:yes;')
cursor = con.cursor()


def CreateTable():
    cursor.execute("create table Student(int id primary key, name varchar(55));")
    cursor.commit()

def main():
    CreateTable()

main()
