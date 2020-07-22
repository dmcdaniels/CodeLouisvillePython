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
#make this a function

#While loop to add grocery items, with their cost to the list until finished.

while True:
    new_item =input("> ").lower()
    store_item = store1.get(new_item)
    print (store_item)
    if new_item == "done":
        break
    grocery_add(new_item)


#Printed out grocery list
print("Grocery List:")
for food_item, value in store1.items():
    print(food_item, ':', value)

values = food_item.value()

total = sum(values)
print(total)



#Create a function that adds the total of all items together. 
#total = 0
#for total_cost in new_item:
#    total = total + new_item(total_cost)



