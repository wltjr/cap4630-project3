#!/usr/bin/python3

import re

def main():

#    filename = input()
#    if filename == None:
#       print("filename missing, please pass a filename")
    filename = "../files/attributes1.txt"
    attributes = {}
    count = 0

    try:
        file = open(filename, "r")
    except IOError:
        print ("The file %s was not found, aborting." % filename)
        exit()

    for line in file:
        if line[0] == '\n' or line[0] == '#':
            continue
        values = re.split(r'[:,]', line[:-1])
        attributes[values[0]] = (values[1], values[2])
        print(values)
        count = count + 1


    count = count**2
    print(attributes)
    print(count)

    for i in range(0,count):
        binary = format(i,'b').zfill(4)
        print(binary)
        menu = ""
        for j in range(0,4):
            menu = menu + list(list(attributes.items())[j])[1][int(binary[j])]
            if j < 3:
                menu = menu + ' '
        print("menu: %s" % menu)

if __name__ == "__main__":
    main()
