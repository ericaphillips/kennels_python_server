class Customer():
    
    #class initializer. Has 5 custom parameters and the 
    #self parametere that every method on a class
    #needs as the first parameter
    def __init__(self, id, name, email, password, status):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.status = status