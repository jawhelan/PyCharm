def add_numbers (*args):
    total=0
    for a in args:
        total += a     # the += will add up each argument like args+args+args as in run through the loop
        print (total)

add_numbers(3,6,10)