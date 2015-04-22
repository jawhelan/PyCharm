numberstaken = [1,2,12,14,19,]

print ("here are all the available numbers")

for n in range(1,20):
    if n in numberstaken:
       print(n, "taken")   # if I had print here it would print out the numbers taken
       continue
    print(n, "available")   # this prints out the available

