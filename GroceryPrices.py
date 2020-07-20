from stores import store1
from stores import store2
# Add ability to search Kroger for items


print(store1)


grocery_list = []

#Function to add items to the grocery list.
def grocery_add(item):
    grocery_list.append(item)
    print("The list now has {} items".format(len(grocery_list)))

#Add instructions


#While loop to add grocery items to the list until finished.
while True:
    new_item =input("> ")
    if new_item == "DONE":
        break
    grocery_add(new_item)


#Printed out grocery list
print("Grocery List:")
for food_item in grocery_list:
    print(food_item)


#Create a function that adds the total of all items together. 


#Possibilities:
#Add second API to search through to compare prices.
