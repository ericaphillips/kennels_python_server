import sqlite3
import json
from models import Location

LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike",
      "status": "Open"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive",
      "status": "Open"
    }
]

def get_all_locations():
    #open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #Write the SQL query to get info you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)

        #initialize an empty list to hold all locations
        locations = []

        #convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        #iterate the list of data returned from database
        for row in dataset:

            #create a location instance from the current row
            #The database fields are specifid in exact order
            #of the parameters defined in Location class
            location = Location(row['id'], row['name'], row['address'])
            locations.append(location.__dict__)
    #use json package to serialize list as JSON
    return json.dumps(locations)

def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #Use ? as parameter to inject a variable's value into SQL statement
        db_cursor.execute("""
        SELECT 
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, ( id, )) 

        #load the single result into memory
        data = db_cursor.fetchone()

        #Create location instance from the current row
        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)

def create_location(location):
    #Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    #Add 1 to that number
    new_id = max_id + 1

    #Add "id" property to location dictionary
    location["id"] = new_id

    #Add the location dictionary to the list
    LOCATIONS.append(location)

    #REturn the dictionary with the "id" property added
    return location

def delete_location(id):
    #Initial -1 value for location_index in case one isn't found
    location_index = -1

    #Iterate the list of LOCATIONS
    #use enumerate() so you can access the index value of each
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            #location found, store the current index
            location_index = index

    #If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    #Iterate LOCATIONS list
    #use enumerate() so you can access index or everry item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            #Found location, update the value
            LOCATIONS[index] = new_location
            break