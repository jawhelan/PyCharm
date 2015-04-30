#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        fh = open('lines.txt')
    except Exception as e:
        print("wtf that an't right",e)

    else:
         for line in fh:
             print(line.strip())    # the .strip() function removes the end line spacing

if __name__ == "__main__": main()
