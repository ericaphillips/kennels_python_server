LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    #Variable to hold the found location if it exists
    requested_location = None

    #iterate through LOCATIONS
    ##like for...of loops in javascript

    for location in LOCATIONS:
        #Dictionaries in Python use [] notation to find key
        if location["id"] == id:
            requested_location = location

    return requested_location

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