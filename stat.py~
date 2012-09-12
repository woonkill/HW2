# ECE 2524 Homework 2 Problem 3 Daniel Kim
from sys import argv

script, filename = argv

print "ACCOUNT SUMMARY"
Amount = 0
Total = 0
Max = 0
MaxName = "[nobody]"
Min = float("inf")
MinName = "[nobody]"

with open(filename, 'r') as f:
    read_data = f.read() # Read the whole file at once
    FileLines = read_data.split('\n')
    for i in range(0, len(FileLines)-1):
        LineSplit = FileLines[i].split()
        Amount = float(LineSplit[2])
        Total += Amount
        if(Amount > Max):
            Max = Amount
            MaxName = LineSplit[1]
        elif(Amount < Min):
            Min = Amount
            MinName = LineSplit[1]
    Average = Total / (len(FileLines) - 1)

print "Total amount owed = " + repr(Total)
print "Average amount owed = " + repr(Average)
print "Maximum amount owed = " + repr(Max) + " by " + MaxName
print "Minimum amount owed = " + repr(Min) + " by " + MinName
print

f.closed

