import datetime
import mysql.connector

DB_NAME = 'employees'
HOST = '127.0.0.1'
LOGGED_ON = False
while not LOGGED_ON:
    credentials = {
        "user": "root",
        "password": "Parker112!"
    }
    # USER = input('Username: ')
    # PASSWORD = input('Password: ')
    try:
        cnx = mysql.connector.connect(user=credentials['user'], password=credentials['password'],
                                        host=HOST,
                                        database=DB_NAME)
    except mysql.connector.Error as err:
        print("Incorrect Login")
        pass
    else:
        LOGGED_ON = True

cursor = cnx.cursor()
today = datetime.date.today()
query = ("SELECT first_name, last_name, salary FROM employees, salaries "
         "WHERE employees.emp_no = salaries.emp_no "
         "AND salary  > 22000 AND salary < 60000 "
         "ORDER BY first_name "
         "LIMIT 10 ")

print(query)
cursor.execute(query)

for (first_name, last_name, salary) in cursor:
  print("{}, {} has the salary of {}".format(
    last_name, first_name, salary))


cursor.close()
cnx.close()
