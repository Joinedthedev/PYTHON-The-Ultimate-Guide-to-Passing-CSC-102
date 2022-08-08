#Check the problem solving questions for a more comprehensive background of lists.

# Llist = ["yo hey hello higoodday"]
# print(Llist[0])
#
# print(Llist[:4])
# LlistSPLIT = [words.split() for words in Llist]
# x = LlistSPLIT
# print(x)
count = dict()
names = ['Goku','Vegeta','Gohan','Piccolo', 'jiren', 'Goku', 'Goku']
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] += 1

print(count)

kk=[1,2,3,4,3,32,2,3,3,3]