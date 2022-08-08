Wheezy_Outta_Here = {"drake" : 1,  "Juice Wrld" : 999, "Migos" : 3,  "Young Thug":  9}
print(Wheezy_Outta_Here["drake"])

ShinzouOpen = open("My School.txt")
count = dict()
for line in ShinzouOpen:
    words = line.split()
    for EachWord in words:
        count[EachWord] =count.get(EachWord,0)+1
        print(count)

# from random import randint
# OgDict = {}
# InputFile = open("One of these presidents is not a real president.txt")
# for Presidents in InputFile:
#     Presidents = Presidents.strip()
#     if Presidents not in OgDict:
#         OgDict[Presidents] = randint(0,22)
# z = list(OgDict.items())
# print(z)