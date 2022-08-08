#You guys know the drill

#1
cents = float(input("Enter the amount of cents:"))
Quart= cents/25
dime = cents/10
dollar = cents/100
nickel = cents/5
penny = cents/1
print(" dollars:", dollar, '\n', "quarters:", Quart, '\n',"dimes:",  dime, '\n', "nickels:", nickel, '\n', "pennies:", penny)

#b
# A variable is a storage container for values.They represent values and can change. There are two types of variables :
# numeric variables which store numeric values and string variables which store strings.

#i invalid because it starts with a number
# ii. valid
# iii. valid
# iv. invalid because it contains spaces
# v. invalid because of the special character

# c
# i. customer_fname - str
# ii. NoOFApple_Pack- int
# iii. ClassAvrg - float
# iv. StuGrade - str
# v. STUDENTpin - int

#2
#a
# A function is simply a block of reusable code that takes arguments and returns a result or results.

#b
# def interest(r,t,p):
#     p = float(p)
#     SI = (p*r*t)/100
#     print(SI)
# interest(10,10,1)

#3
#a
#The if structure is important because it allows us to set and test conditions in python. It allows python to choose more
#than one path based on a condition set by the user. It allows for multiple instances.

#b
def Pensionsim():
     Name = input("Enter your name")
     Age = int(input("Enter your age"))
     Commodity = int(input("Enter price of the commodity:"))
     if Age >= 65:
         Discount = Commodity/2
         print(" Name:", Name, "\n", "Age:",Age, "\n", "Price to be paid", Discount )
     else:
         print(" Name:", Name, "\n", "Age:",Age, "\n", "Price to be paid", Commodity )

Pensionsim()

#4
#a
# 1.Identify the problem
# 2.Analyze the problem
# 3.Design a solution
# 4.coding
# 5.test the code
# 6.debug the code
# 7.Implement the code
# 8.document the code

#b(This question seems to be incomplete. SO, lets assume they want to be prompted anually for 5 years.
# for i in range(0,1830,366):
#     print("Alert! It's time to review the course content of every module in the Computer Department.")

#5
#a
#dictionaries are unordered sets that store values using a key:value pair. Those values are accessed through the key:value pair.
#Lists are linear ordered sets that store values. They are accessed via their index position.

#b
# def NTNUprospect():
#     Fname = input("Whats your firstname?")
#     Sname = input("Whats your surname?")
#     print("Length of surname:", len(Sname))
#     for i in Sname:
#         print(i)
#     SNAME = Sname.upper()
#     print(SNAME)
#     Z = Sname.replace(Sname,Fname)
#     print(Z)
#
# NTNUprospect()

#a
# from,return, import, True, False, if, elif, else, is, not

#b
#easier method but a tinsy bit ambigious towards the question. Go with this tho

# QuizList = [1,100,23,43,67,87,56,32,79,99,]
# print(QuizList)
# print("Avrg is:", sum(QuizList)/len(QuizList))

#what i would do(After asking if i could do it of course)
# from random import randint
# s = (randint(0,100) for i in range(10))
# Quizlist=list(s)
# print(Quizlist)
# print("Avrg is:", sum(Quizlist)/len(Quizlist))

#Dedicate your heart.
