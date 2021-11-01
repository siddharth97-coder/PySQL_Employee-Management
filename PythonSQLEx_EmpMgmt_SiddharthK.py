import csv
import yaml
from ntpath import join
from os import path
from pprint import pprint
class InfoMissingException(Exception): pass
class EmployeeAgeException(Exception): pass
#This script allows you to read in employee data for an Employee 
# Management System and import it to a .csv file

#Employees
employees = []
while True:
    try:
        num = int(input("How many employees will be entered?: "))
    except ValueError: print("Please enter a number.") 
    else: break

for i in range(num):
    emp = {}
    try:
            #Checking if Department, Manager & Address ID exist
            dept_id = int(input(f"Enter Department ID for Employee {i+1}: "))
            a_id = int(input(f"Enter Address ID for Employee {i+1}: " ))
            m_id = int(input(f"Enter Manager ID (Enter 0 if no manager)\n for Employee {i+1}: "))
            if ((dept_id is None) or (a_id is None) or (m_id is None)):
                 raise InfoMissingException
            age = int(input(f'Enter the age of Employee {i+1}:  '))
            if (age < 18): raise EmployeeAgeException
    except InfoMissingException:
             print("Must provide Dept ID, Address ID and Manager ID!")
    except EmployeeAgeException: 
            print('Employee is too young to work here.')
    except ValueError: print("Please enter a number.")
    else:
        emp["id"] = i+1
        name = input(f"Enter Employee {i+1}'s name: ")
        emp["name"] = name 
        emp['age'] = age
        salary = float(input(f"Enter Employee {i+1}'s salary: \n"))
        emp['salary'] = salary
        emp['department id'] = dept_id
        emp['address id'] = a_id
        emp['maanger id'] = m_id
        global header #Ensuring header has global definition
        header = emp.keys() 
        employees.append(emp)

# Creating employees.csv file
with open("employees.csv", "wt") as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(employees)

#Addresses
addresses = []
while True:
    try:
        num_a = int(input("How many addresses will be entered: "))
    except ValueError: print("Please enter a number.") 
    else: break

for i in range(num_a):
    address = {}
    try:    
        street = input(f"Enter street name for {i+1}th address :")           
    except NameError: print("Variable is used but not defined.")
    else:
        address["id"] = i+1
        address["street"] = street
        city = input(f"Enter city name for {i+1}th address: ")
        state = input(f"Enter state name for {i+1}th address: \n")
        address["city"] = city
        address['state'] = state
        global header2 #Ensuring header has global definition
        header2 = address.keys() 
        employees.append(emp)
        
# Creating addresses.csv file 
with open("addresses.csv", "wt") as file:
    writer = csv.DictWriter(file, fieldnames=header2)
    writer.writeheader()
    writer.writerows(addresses)

#Departments
departments = []
while True:
    try:       
        num_d = int(input("How many departments will be entered: "))
    except ValueError: print("Please enter a number.") 
    else: break

for i in range(num_d):
    department = {}
    try:    
        name = input(f"Enter department name for {i+1}th department: ") 
    except NameError: print("Variable is used, but not defined.")
    else:
        a_id = int(input(f"Enter Headquarters address ID for {i+1}th department :\n"))
        department["id"] = i+1
        department["name"] = name
        department["headquarters address id"] = a_id
        global header3 #Ensuring header has global definition
        header3 = department.keys() 
        departments.append(department)
        
# Creating departments.yml file
with open("departments.yml", "wt") as file:
    data = yaml.dump(departments)  
    file.write(data)

#BONUS: Creating a addresses.yml file, where the the records are 
# grouped by state and city
with open("addresses.yml", "wt") as file:
    data = yaml.dump(address, sort_keys = True)  
    file.write(data)

