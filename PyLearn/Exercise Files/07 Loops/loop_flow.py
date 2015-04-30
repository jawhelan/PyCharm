#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    my_list = [2, 4, 6, 8]
    for item in my_list:
        print(item)
        if item == 4: continue  # this skips all the s #think of continue to mean break and start over
       #if c == "s' break    # this will stop at the first s
        print(item)

if __name__ == "__main__": main()
