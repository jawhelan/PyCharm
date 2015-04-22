shopping_list = list()   # [] could also be used to start the list

print( "what should we pickup at the store?")
print ("Enter 'DONE' to stop adding items")

while True:
    new_item = input(">").lower() # here i set the input to conver to lower so you wont miss done DONE
    
    if new_item == 'done':
        break
    
    shopping_list.append(new_item)
    print ("Added list has {} items".format(len(shopping_list)))
    continue

print("here is your list:")

for item in shopping_list:  # the syntax is like for x in list: Print(x)
    print(item)