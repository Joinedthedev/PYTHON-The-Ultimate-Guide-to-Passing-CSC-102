# count = 0
# charsum = 0
hmm = open("My School.txt", "r")
#for e in hmm:
    #if e.startswith("Nile" or "NILE"):
   #     print(e)

    #charsum+= len(e)
    #print("This line contains", len(e), "characters")
    #count += 1
#print("Tot charrs r", charsum)
#print("The number of lines in the file is", count)

unt = 0
Jount = 0
file = input("Choose your character!")
path="C:/Users/salim/Documents/"+file
Gamer = open(path, "r")
for line in Gamer:
    unt +=1
    Jount += len(line)
print("no of lines", unt)
print("no of chars", Jount)