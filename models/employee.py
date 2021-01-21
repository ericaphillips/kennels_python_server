class Employee():
    #class initializer. Has 5 custom parameters and the 
    #self parametere that every method on a class
    #needs as the first parameter
    def __init__(self, id, name, location_id, animal_id, status):
        self.id = id
        self.name = name
        self.status = status
        self.locationId = location_id
        self.animalId = customer_id