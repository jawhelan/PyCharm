#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        fh = open('klines.txt')

    except:
        print("wtf that an't right")

    else:
       for line in fh:

        print(line.strip())

if __name__ == "__main__": main()
