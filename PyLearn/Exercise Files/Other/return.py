def allowed_dating_are(myage):
    girls_age = myage/2 + 7
    return girls_age

def askFloat(prompt):
    return float(input(prompt))
x = askFloat("Enter a floating-point number: ")
james_limit = allowed_dating_are(x)
print("James'  can only date girls over", james_limit)