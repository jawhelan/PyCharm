'''
Created on Apr 16, 2015

@author: james_000
'''
shopping_list = list()

print("what should we pick out at the store")
print("Enter 'DONE' when finished")

while True:
    new_item = input(">>")
    
    if new_item.lower() == 'DONE'.lower():
        break
    
    shopping_list.append(new_item)
    print(" Added! List has {} items".format(len(shopping_list)) )
    continue

print("here is your list")
#for i in shopping_list:
print(shopping_list)


    
