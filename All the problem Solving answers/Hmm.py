Nile= input("Enter file name")
f = open(Nile, "r")
num_lines = 0
for line in f:
    num_lines+=1
print("The no of lines in the file is:", num_lines)