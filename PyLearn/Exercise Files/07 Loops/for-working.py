#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    fh = open('lines.txt')
    for line in fh.readlines(): # the for works with iterator. here readlines is an itorator for the file object
                                # also all container types and strings are itroators
        print(line, end='')    # the end='' cuts the new line of the end

if __name__ == "__main__": main()
