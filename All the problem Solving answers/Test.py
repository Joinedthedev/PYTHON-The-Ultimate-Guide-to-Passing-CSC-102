Infile = open("Friend_Essay.txt", "r")
count = 0
for line in Infile:
     count+= 1
     if count == 2:
         print(line)
         s = line.split()
         print(s)
