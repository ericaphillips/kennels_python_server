import sqlite3
import json
from models import Animal

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]


# def get_all_animals():
#     return ANIMALS

#Function with a single parameter
# def get_single_animal(id):
#     #Variable to hold the found animal, if it exists
#     requested_animal = None

#     #Iterate the ANIMALS list above, 
#     #very similar to the for...of loops in JavaScript

#     for animal in ANIMALS:
#         #Dictionaries in Python use [] notation to find a key
#         #instead of the dor notation in JavaScript
#         if animal["id"] == id:
#             requested_animal = animal

#     return requested_animal

def create_animal(animal):
    #Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    #Add 1 to whatever that number is
    new_id = max_id + 1

    #Add an "id" property to the animal dictionary
    animal["id"] = new_id

    #Add the animal dictionary to the list
    ANIMALS.append(animal)

    #Return the dictionary with 'id' property added
    return animal

# def delete_animal(id):
#     #Initial -1 value for animal index, in case one isn't found
#     animal_index = -1

#     #iterate the ANIMALS list, but use enumerate()
#     #so you can access the index value of each
#     for (index, animal) in enumerate(ANIMALS):
#         if animal["id"] == id:
#             #Found the animal. Store the current index
#             animal_index = index

#     #If the animal was found, use pop(int) to remove it from list
#     if animal_index >= 0:
#         ANIMALS.pop(animal_index)

def update_animal(id, new_animal):
    #Iterate the ANIMALS list
    #Use enumerate() so you can access index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            #Found the animal, update the value
            ANIMALS[index] = new_animal
            break

def get_all_animals():
    #Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        #Use these, it's a black box
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #Write the SQL query to get info you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        """)

        #Initialize an empty list to hold all animal representations
        animals = []

        #Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        #Iterate the list of data returned from database
        for row in dataset:

            #create an animal instance from the current row.
            #Note that the database fields are specified
            #in exact order of the parameters defined
            #In Animal class above
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'])

            animals.append(animal.__dict__)
    #Use json package to properly serialize list as JSON
    return json.dumps(animals)

def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #Use a ? parameter to inject a variable's value
        #into the SQL statement
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        #Load the single result into memory
        data = db_cursor.fetchone()

        #Create animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'], data['status'],
                        data['location_id'], data['customer_id'])
    
        return json.dumps(animal.__dict__)

def get_animals_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #Write SQL query to get info wanted
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.location_id = ?
        """, ( location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)

def get_animals_by_status(status):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #Write SQL query to get info wanted
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.status = ?
        """, ( status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)
            
    return json.dumps(animals)

def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Animal
        WHERE id =?
        """, ( id, ))
