import json
import sqlite3
from models import Employee

EMPLOYEES = [
    {
      "name": "Daniel Smith",
      "locationId": 1,
      "animalId": 2,
      "id": 3,
      "status": "Employed"
    },
    {
      "name": "yeety",
      "locationId": 1,
      "animalId": 2,
      "id": 5,
      "status": "Fired"
    },
    {
      "name": "Newnew",
      "locationId": 1,
      "animalId": 2,
      "id": 6,
      "status": "Retired"
    },
    {
      "name": "SCOTT",
      "locationId": 1,
      "animalId": 5,
      "id": 7,
      "status": "Employed"
    },
    {
      "name": "south",
      "locationId": 2,
      "animalId": 4,
      "id": 8,
      "status": "Demoted"
    },
    {
      "name": "southstella",
      "locationId": 2,
      "animalId": 2,
      "id": 9,
      "status": "Employed"
    }
  ]


def get_all_employees():
  #Open a xonnection to the database
  with sqlite3.connect("./kennel.db") as conn:

    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    #Write SQL query to get info wanted
    db_cursor.execute("""
    SELECT
      e.id,
      e.name,
      e.address,
      e.location_id
    FROM employee e
    """)

    #Initialize an empty list to hold all employee representations
    employees = []

    #Convert rows of data into a Python list
    dataset = db_cursor.fetchall()

    #Iterate the list of data returned
    for row in dataset:

      #Create an employee instance from the current row
      #Database fields are specified in exact order
      #of parameters defined in Employee class
      employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
      employees.append(employee.__dict__)
  #USe json package to serialize list as JSON
  return json.dumps(employees)

#Function with a single parameter
def get_single_employee(id):
  with sqlite3.connect("./kennel.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    #Use a ? parameter to inject a variable's value 
    #into a SQL statement
    db_cursor.execute("""
    SELECT
      e.id,
      e.name,
      e.address,
      e.location_id
    FROM employee e
    WHERE e.id = ?
    """, ( id, ))

    #Load the single result into memory
    data = db_cursor.fetchone()

    #Create employee instance from the current row
    employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

    return json.dumps(employee.__dict__)

def create_employee(employee):
    #Get the id value of the last employee on list
    max_id = EMPLOYEES[-1]["id"]

    #Add 1 to that number
    new_id = max_id + 1

    #Add an "id" property to the employee dictionary
    employee["id"] = new_id

    #Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    #Return the dictionary with 'id' property added
    return employee

def delete_employee(id):
    #Initial -1 value for employee index in case one isn't found
    employee_index = -1

    #iterate the EMPLOYEES list, use enumerate()
    #so you can access index value of each
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            #found the employee, store the current index
            employee_index = index
    #If employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    #Iterate the EMPLOYEES list
    #use enumerate() so you can access index of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            #Found employee, update the value
            EMPLOYEES[index] = new_employee
            break