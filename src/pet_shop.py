# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop,cash):
     total_cash = pet_shop["admin"]["total_cash"]
     final_cash = float(total_cash) + float(cash) 
     pet_shop["admin"]["total_cash"] = final_cash
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    total_sold = pet_shop["admin"]["pets_sold"]
    final_sold = float(total_sold) + float(sold) 
    pet_shop["admin"]["pets_sold"] = final_sold
    
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, shorthair):
    mylist = []
    for x in pet_shop["pets"]:
        if x["breed"]== shorthair:
            mylist.append(x)   
    return mylist
    
def find_pet_by_name(pet_shop, petname):
    # print(pet_shop)
    for pet in pet_shop["pets"]:
        if pet["name"] == petname:
           return pet

    
    
def remove_pet_by_name(pet_shop,p_name):
    # mylist = []
    for x in pet_shop["pets"]:
        if x["name"]==p_name:
            pet_shop["pets"].remove(x)
    
    return pet_shop
               
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    return pet_shop

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, cash ):
    total_cash = customers["cash"]
    final_cash = float(total_cash) - float(cash) 
    customers["cash"] = final_cash
    

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(cutomer, new_pet):  
    return cutomer["pets"].append(new_pet)

def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]
   
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)
        
    
        
    
    
    
    
    
    


    
    











# def add_or_remove_cash(pet_shop, num):

# def get_stock_count(pet_shop):
    #  return len(pet_shop['pets'])


# def get_pets_by_breed(pet_shop, selected_breed):
#         breed_count = breed_count =+ 1
# for breed in pet_shop["pets"]:
#         if breed == selected_breed:
#             breed_count += 1