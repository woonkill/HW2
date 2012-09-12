# ECE 2524 Homework 2 Problem 1 Daniel Kim
with open('/etc/passwd', 'r') as f:
    read_data = f.read() # Read the whole file at once
    FileLines = read_data.split('\n')
    for i in range(0, len(FileLines)-1):
        LineSplit = FileLines[i].split(':')
        username = LineSplit[0]
        path = LineSplit[len(LineSplit) - 1]
        print username + '\t' + path
f.closed

