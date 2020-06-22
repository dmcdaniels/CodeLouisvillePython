grocery_list = []

def grocery_add(item):
    grocery_list.append(item)
    print("The list now has {} items".format(len(grocery_list)))


while True:
    new_item =input("> ")
    if new_item == "DONE":
        break
    grocery_add(new_item)


print("Grocery List:")
for food_item in grocery_list:
    print(food_item)