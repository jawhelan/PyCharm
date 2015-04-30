#!/usr/bin/python3
# conditionals.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a, b = 5, 3
    if a > b:
        print("This is the true")
    elif a < b:
        print("this is false.")
    else:
        print("that is equal")

if __name__ == "__main__": main()
