from stores import store1
from stores import store2
# Add ability to search Kroger for items

#Add instructions
#make this a function
def inventory():
    print ("These are the items we have available in our store:   ")

print("Hello and welcome to our online shopping store. For our inventory please type 'inventory', when you are finished shopping type 'done'.")

#Start with an empty grocery list.
grocery_list = []

#Function to add items to the grocery list.
def grocery_add(item, cost):
    grocery_list.append([item, cost])
    print("The list now has {} items".format(len(grocery_list)))




#While loop to add grocery items, with their cost to the list until finished. If/elif functions for inventory and exiting the loop.
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
    print (store_cost)
    grocery_add(new_item, store_cost)

#Print out grocery list
print (grocery_list)

#Create a function that adds the total of all items together. 