


s_age = input("How old are you?") # the input will be strin so you need to covert it to int
age =int(s_age)  # here i'm converting the string to an int.
if age < 21:
    print("no beer for you")
    
elif age > 21:
    print("let's get some beer")  # you can do lots of elifs
else:
    print("hey you just made it") # you can do this one to catch the rest of the possible inputs
    