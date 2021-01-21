class Animal():

    #class initializer. Has 5 custom parameters and the 
    #self parametere that every method on a class
    #needs as the first parameter
    def __init__(self, id, name, breed, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.locationId = location_id
        self.customerId = customer_id

