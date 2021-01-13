CUSTOMERS = [
    {

      "email": "test1@test1.com",
      "password": "yeety",
      "name": "test1 test1",
      "id": 1,
      "status": "Active"
    },
    {
      "email": "test2@test2.com",
      "password": "yeety2",
      "name": "test2 test2",
      "id": 2,
      "status": "Active"
    },
    {
      "email": "test3@test3.com",
      "password": "yeety3",
      "name": "test3 test3",
      "id": 3,
      "status": "Archived"
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

def create_customer(customer):
    #Get id of last customer on list
    max_id = CUSTOMERS[-1]["id"]

    #Add 1 to number
    new_id = max_id +1

    #Add "id" property to customer dictionary
    customer["id"] = new_id

    #Add Customer dictionary to list
    CUSTOMERS.append(customer)

    #Return dictionary with 'id' property added
    return customer

def delete_customer(id):
    #Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    #iterate the CUSTOMERS list. USe enumerate()
    #so you can access the index value of each
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            #Found customer, store the current index
            customer_index = index

    #If customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer): 
    #Iterate CUSTOMERS list
    #Use enumerate() so you can access index of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            #Found the customer, update the value
            CUSTOMERS[index] = new_customer
            break