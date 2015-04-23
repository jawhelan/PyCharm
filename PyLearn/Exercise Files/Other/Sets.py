groceries = {"milk", "bread","bear","juice", "apples","bear"}   # sets will not print dups
groceries2 = ["milk", "bread","bear","juice", "apples","bear"]   # list will print all and are imutable
groceries3 = ("milk", "bread","bear","juice", "apples","bear")    # tupels will print are and is mutable

print(groceries)
print(groceries2)
print(groceries3)

if "milk" in groceries:          # since you can add dups to a set this if else can tell you if you got it or not
    print("you got milk hoss!")
else:
    print("you needed that")
