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
    return EMPLOYEES

#Function with a single parameter
def get_single_employee(id):
    #Variable to hold the found employee if it exists
    requested_employee = None

    #Iterate the EMPLOYEES list
    #like for...of loops in JS

    for employee in EMPLOYEES:
        #Dictionaries in Python use [] instead of dot notation
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

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