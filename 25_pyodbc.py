
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SIDDHARTH;'
                      'Database=HR_DB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM employees')
