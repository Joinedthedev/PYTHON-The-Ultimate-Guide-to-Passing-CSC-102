#A function that determines the sum of three elements
#def add(a,b,c):
#    return a+b+c
#x = 10
#y = 20
#z = 30
#
#result = add(x, y, z)
#print("The sum of three numbers is", result)

#def bigger(a, b, c):
#    if (a>b) and (a>c):
#        return a
#    elif (b>a) and (b>c):
#        return b
#    else: return c
#
#x = int(input("Enter a number mortal"))
#y = int(input("Enter a number mortal"))
#z = int(input("Enter a number mortal"))
#
#print("The largest of three numbers is", bigger(x,y,z))
#print("Da biggest of tem all is", max(x,y,z))

#You are presented with the scores of 4 students in your department. Among the tasks that is expected of you
#on the students scores is as follows
#1. get the score from the students
#2. compute the sum of the student scores
#3. display the students avrg score
x = 8
def getscore():
    a = int(input("Enter the first students score"))
    b = int(input("Enter the second students score"))
    c = int(input("Enter the third students score"))
    d = int(input("enter the fourth students score"))
    s = a+b+c+d + x
    print("The sum is", s)
    return s

#def displayAVG():
#    print("The score AVG is", getscore()/4)
#
#displayAVG()
#
#alt ending
#a = int(input("Enter the first students score"))
#b = int(input("Enter the second students score"))
#c = int(input("Enter the third students score"))
#d = int(input("enter the fourth students score"))
#
#def getScore():
#    print(a,b,c,d)
#
#def Addscore():
#   sum = a + b + c+ d
#   return sum
#def Avg():
#    avgg= Addscore()/4
#    print(avgg)
#getScore()
#Addscore()
#Avg()

def getScore():
    n = int(input())
    x = sum(n)
    return x

getScore()