# Add ability to search dictionary for store inventory. 
from stores import store1
from stores import store2

# Add instructions
def inventory():
    print ("These are the items we have available in our store:   ")

def outofstock():
    print ("Oh sorry. It looks like we are currently out of the item you are looking for. Would you like to purchase something else instead?  ")

print("Hello and welcome to our online shopping store. For our inventory please type 'inventory', when you are finished shopping type 'done'. To add an item to the cart, just enter the name of the item")

# Start with an empty grocery list.
grocery_list = []

# Function to add items to the grocery list.
def grocery_add(item, cost):
    grocery_list.append([item, cost])
    print("The list now has {} items".format(len(grocery_list)))


# While loop to add grocery items, with their cost to the list until finished. If/elif functions for inventory and exiting the loop.
while True:
    new_item =input("What would you like to purchase? ").lower()
    store_cost = store1.get(new_item)
    if new_item == "inventory":
        inventory()
        for item, cost in store1.items():
            print(item, ':', cost)
        continue
    elif new_item == "done":
        break
    #Fix if not in stock.
    if new_item not in store1:
        outofstock()
        continue
    
    print (store_cost)
    grocery_add(new_item, store_cost)

#Print out grocery list
print ("Your grocery list is", *grocery_list, sep = "\n")

#Create a function that adds the total of all items together. 
total_cost = 0

for grocery_item in grocery_list:
    total_cost = total_cost + grocery_item[1]
print ("The total cost of your groceries today is:   ", total_cost)