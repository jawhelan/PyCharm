def main():
    func(1)
    func()
    func(3)
    
    
def func(a=7):
    # for each x in the range print to before 10 and end with space
    for X in range(a, 11):
        print(X, end=" ")
    # add a print line
    print()

if __name__ == "__main__": main()


    
