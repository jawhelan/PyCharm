#!/usr/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# in python they use dictionary fucntion to do switching

def main():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'thrid',)
    v = 'one'
   # print(choices[v])               # this works but it will error on a choise not in the dictionary
    print(choices.get(v, "other"))  # here we use the get method of the dictionary object to select "other" for and
                                    # choise not in the dictionary.   a try and except could also work

if __name__ == "__main__": main()
