CUSTOMERS = [
    {

      "email": "test1@test1.com",
      "password": "yeety",
      "name": "test1 test1",
      "id": 1
    },
    {
      "email": "test2@test2.com",
      "password": "yeety2",
      "name": "test2 test2",
      "id": 2
    },
    {
      "email": "test3@test3.com",
      "password": "yeety3",
      "name": "test3 test3",
      "id": 3
    }
]

def get_all_customers():
    return CUSTOMERS

#Function with a single parameter
def get_single_customer(id):
    #variable to hold found customer
    requested_customer = None
    #iterate CUSTOMERS list
    #like for... of loops in JS

    for customer in CUSTOMERS:
        #Dicgtionaries in Python use [] notation instead of dot
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer