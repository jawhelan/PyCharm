def f_r (x):
    return x + 3  # a return value sets the value of the function


def f_p(x):
    print(x + 3)

#f_r(7)

#f_p(7)

def p_r(x):
    print(f_r(x))

p_r(7)

revar = f_r(6)   #revaar is now taking the vaule or 6 + 3


print (revar + 3)