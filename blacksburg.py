# ECE 2524 Homework 2 Problem 2 Daniel Kim
from sys import argv

script, filename = argv

print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"

with open(filename, 'r') as f:
    read_data = f.read() # Read the whole file at once
    FileLines = read_data.split('\n')
    for i in range(0, len(FileLines)-1):
        LineSplit = FileLines[i].split()
        if LineSplit[3] == "Blacksburg":
            print LineSplit[4] + ", " + LineSplit[1] + ", " + LineSplit[0] + ", " + LineSplit[2]
    print
f.closed

