import sqlite3
from sqlite3 import Error
'''
Pre-requisites -
Download SQLLite and install it --> http://www.sqlitetutorial.net/download-install-sqlite/
Download the sample database 'Chinook' and store is locally --> http://www.sqlitetutorial.net/sqlite-sample-database/
This script connect to the Chinook DB , runs a query on the emplyees table and prints the number of rows returned
'''

def list_employees_and_count(db_file_location):
    try:
        new_connection = sqlite3.connect(db_file_location)
        cursor = new_connection.cursor()
        sql = ''' INSERT INTO employees(EmployeeID,LastName,FirstName,Title)
        VALUES('123345843','Khokhar','Sunjeet','Novice')
        '''
        cursor.execute(sql)
        print(cursor.lastrowid)
        new_connection.commit()
        sql1 = 'select * from employees'
        cursor.execute(sql1)
        result = cursor.fetchall()
        for row in result:
            print(row)
        print(f'The total nmber of rows in the employee table are {len(result)}')
    except Error as e:
        print(e)
    finally:
        new_connection.close()

if __name__ =='__main__':
    list_employees_and_count('C:\SQLite\sqlite-tools\chinook\chinook.db')