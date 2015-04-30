#!/usr/bin/python3
# iterators.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    my_string = 'this is a string '
    item = 0
    while(item < len(my_string)):
        print(my_string[item], end='')
        item += 1
    else:
        print("this is else 1")



if __name__ == "__main__": main()
