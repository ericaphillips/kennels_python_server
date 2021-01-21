class Location():
    #class initializer. Has 5 custom parameters and the 
    #self parametere that every method on a class
    #needs as the first parameter
    def __init__(self, id, name, address, status):
        self.id = id
        self.name = name
        self.address = address
        self.status = status