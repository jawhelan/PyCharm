def allowed_dating_are(myage):
    girls_age = myage/2 + 7
    return girls_age

def askFloat(prompt):   # create a method funtion called ask float and create an argument called prompt
    return float(input(prompt))   # return promt as an input and convert to float
x = askFloat("Enter a floating-point number: ")   # create a varible called x and
james_limit = allowed_dating_are(x)
print("James'  can only date girls over", james_limit)