EMPLOYEES = [
    {
      "name": "Daniel Smith",
      "locationId": 1,
      "animalId": 2,
      "id": 3
    },
    {
      "name": "yeety",
      "locationId": 1,
      "animalId": 2,
      "id": 5
    },
    {
      "name": "Newnew",
      "locationId": 1,
      "animalId": 2,
      "id": 6
    },
    {
      "name": "SCOTT",
      "locationId": 1,
      "animalId": 5,
      "id": 7
    },
    {
      "name": "south",
      "locationId": 2,
      "animalId": 4,
      "id": 8
    },
    {
      "name": "southstella",
      "locationId": 2,
      "animalId": 2,
      "id": 9
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