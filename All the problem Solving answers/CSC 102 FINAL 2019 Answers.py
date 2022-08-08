#If you're starting from here I advise you to go back and start from 2020 or "The questions he said would come out".
#It's by far the most difficult(2020 questions). Spending too much time here probably won't do you any good.

#v
#1
#a
# The power operator is **

#b
#Parenthesis, exponenents, Multiplication/division, Addition/Subtraction

#c
#the answer to 22%3 is 1. It question basically means "Whats the remainder of 22/3?"

#d
#Addition, multiplication

#e
#parenthesis

#f
#Example_list =[]
#Example_List =list()

#g
#:

#h
#False because recursion is when a statement in a function is repeatedly calling itself.
#Iteration is when a loop continuously executes until a condition becomes false.

#i
#the program will run continously until the system runs out of memory or the program crashes.

#j
#def

#2
#a
#dictionaries are unordered sets that store values using a key:value pair. Those values are accessed through the key:value pair.
#Lists are linear ordered sets that store values. They are accessed via their index position.

# #b
# ct = 0
# sum = 0
# def Stusum():
#     global ct, sum
#     while True:
#         x = int(input("Enter your score. Type '123' when done."))
#         sum += x
#         ct = ct + 1
#         if x == 123:
#             break
# Stusum()
# average = sum/ct

#3
#a
# def Factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * Factorial(n-1)
# print(Factorial(4))

#b
#a recursive function is a function that calls itself to repeat the code.
# Iterative function loops to repeat some part of the code until a condition is false.
#
#This is a recursive function
# def Factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * Factorial(n-1)
# print(Factorial(4))

#this is a iterative function
# def Factorial(n):
#     z = 1
#     for num in range(2, n + 1):
#         z *= num
#     return z

#5
#a
#A function is simply a block of reusable code that takes arguments and returns a result or results.

#b

# def FileWord():
#     infile = open("nile.txt", "r")
#     for lines in infile:
#         lines.rstrip()
#         for words in lines.split():
#             print(words)
# FileWord()

#6
even_lst = []
def max_even(lst):
     global even_lst
     for no in lst:
         if no%2==0:
             even_lst.append(no)
             print(max(even_lst))
     if no%2 not in lst:
         print('None')

max_even([3,3,3,3,3])

#Dedicate your heart.