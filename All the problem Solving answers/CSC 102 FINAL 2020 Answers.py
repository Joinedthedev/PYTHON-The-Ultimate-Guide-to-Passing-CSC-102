

#if you're confused at any point Text me(07032699407). Please don't call me. I probably won't answer.♡
#Courtesy of your fav class rep, Salim B. ♡♡♡♡♡♡

#QUESTION 1(COMPULSORY TO ALL SOFTWARE ENGINEERING STUDENTS) BUT REAL NIGGAS(COMPUTER SCIENCES STUDENTS) STILL GONNA DO IT ANYWAY


#a
#First of all, for clarity I should mention that the missing parenthesis regarding the print statement is actually not
#the issue(s) here. In some older python versions(The highly Inferior python 2) you can actually use the print function without the parenthesis. I'm
# guessing in the exam Mr.Yusuf will clarify which python version it is. And if he doesn't, use the method that we've
# been taught in class(PYTHON 3.7).

#x=1; print 'sin(%g)=%g' % (x, sin(x)) Problem with this is the quotation is over the sin(%g)=%g. Python will read it as
#a string.
#C = A + B; A = 3; B = 2; print C: Problem with this is that variable A & B are used before they are defined.
#C = 21.0; F = 9.*(C/5.0) + 32; print F: Problem with this is supposed 9.0 otherwise(Just 9 not 9.), convert F into a float.
#t = (2, 4, 6, 'temp.pdf'); t[1]=4; print t: Problem with this is t[1] is already equal to 4 so there's no logical reason to
#declare such again.

#b
# You can use whatever method/function of your choice but i'll be using random
#1. import random
#2. from random import randint
#3. ???

#c

#LISTS
#Lists are storage containers for a collection of values in python. They store their values in order(linear) and can be changed,
#added to or reversed.
#Examplelist = list() or Example_list = [1,2,3,4,5,43,45,4]

#Check lists in a nutshell for more clarity

#TUPLES
#tuples are similar to lists in the sense they are also storage containers for a collection of values except they can't be changed or
# altered in anyway. You can also do some fancy variable assignments,
#Exampletuple = tuple() or Example_Tuple= ("Hatred", "Envy", "Greed")
#(Fancy_VarA, Fancy_VarB) = ("A", "B")

#Check Tuples in a nutshell for more clarity

#DICTIONARIES
#Similar to lists and tuples, dictionaries are also storage containers for values. They store values using
#a key:value pair. like this:

#ExmpleDict = dict() or Exmple_Dict = {'Boy':1, 'Girl':2}
#check dict in a nutshell for more info

#d
#The try statement lets you check for errors in python. Where an error message would usually occur, you can use the try & except
#statements to test it. Basically, if the argument you pass through the try block creates an error, the except block will be executed.
#And since our x is undefined "An error has occurred" will be printed.


#try:
#    print(x)
#except:
#    print("An error has occurred")

#e
# def checkspeed(speed):
#     demerit_points = (speed - 70) / 5
#     if speed < 70 or speed == 70:
#         print("Ok")
#     elif demerit_points > 12:
#         print("License suspended")
#     else:
#         print("demerit points are", demerit_points)
# checkspeed(75)

#damn that took a while. Anyway, onwards to no 2. Btw Hall of Fame, Culture III is hella fire. Check it out

#2 COMPULSORY FOR COMPUTER SCIENCE STUDENTS(Pay close attention people)

#a

#Open_Seaseme = open("Nile.txt", "r")
# LineCount = 0
#
# for line in Open_Seaseme:
#     LineCount+=1
# print("The no of lines in the passage are", LineCount)

#b

#To count the no of words in the passage we create an empty list to contain the words. Then we create a for loop that will strip the
#spaces from each line. Then we create another for loop within that for loop to split all the words. We then append those
# words to our empty list, then take the length of that list.

# inFile = open("Nile.txt", "r")
# Steal_Ur_Heart=[]   #This is our empty list where the words will be stored
# for line in inFile:
#      line.rstrip()
#      for StrippedLines in line.split():
#          Steal_Ur_Heart.append(StrippedLines)
# print(len(Steal_Ur_Heart))

#c
Open_Seaseme = open("Nile.txt", "r")
LineCount = 0
for line in Open_Seaseme:
      LineCount+=1
      if (LineCount==3):
          break
print(line)

#d
# Lwords=[]
# for line in Open_Seaseme:
#     line.rstrip()
#     for StrippedLines in line.split():
#        if StrippedLines.startswith('L'):
#            Lwords.append(StrippedLines)
# print(Lwords)

#e
#Lwords=[]
#for line in Open_Seaseme:
#     line.rstrip()
 #    for StrippedLines in line.split():
  #      if StrippedLines.startswith('c') or StrippedLines.startswith('C'):
   ##         print(StrippedLines)

#3 COMPULSORY FOR ALL INFORMATION TECHNOLOGY STUDENTS (and by far the easiest of the three)

# def Student_Info():
#     Name = input("Enter Your Full Name")
#     StudentID = input("Enter your student ID No.")
#     Department = input("Enter your department")
#     CGPA = input("Enter your CGPA")
#     Age = input("Enter your age")
#     Shobbies= input("What is your hobby?")
#     print("NAME:", Name,)
#     print("ID NO:", StudentID,)
#     print("Deparment:", Department,)
#     print("CPGA",CGPA)
#     print("AGE:",Age)
#     print("HOBBIES:", Shobbies)
# Student_Info()

#4
# from random import randint
# OgDict = {}
# InputFile = open("One of these presidents is not a real president.txt")
# for Presidents in InputFile:
#     Presidents = Presidents.strip()
#     if Presidents not in OgDict:
#         OgDict[Presidents] = randint(0,22)
# z = list(OgDict.items())
# print(z)
# #Not gonna lie to you, im too lazy to write the code required to make this into a proper table(which we haven't been taught btw)
# #so i'm not gonna do that.
#
# #b
# def DoubleList(A, B, C):
#     DUB_A= A*2; DUB_B= B*2; DUB_C=C*2
#     print(DUB_A)
#     print(DUB_B)
#     print(DUB_C)
# DoubleList(2,4,6)

#5
#Since the no of subjects is unknown and not given, it is up to us to decide how many subjects #there will be.
Grade_Storage = []
# while True:
#      Grades = input("Enter your grades for your WAEC Subjects in capital letters E.G A, B, C etc. Type 'STOP' when finished")
#      if Grades == 'A':
#          Grade_Storage.append(5)
#      elif Grades == 'B':
#          Grade_Storage.append(4)
#      elif Grades == 'C':
#          Grade_Storage.append(3)
#      elif Grades == 'D':
#          Grade_Storage.append(2)
#      elif Grades == 'E':
#          Grade_Storage.append(1)
#      elif Grades == 'F':
#          Grade_Storage.append(0)
#      if Grades == "STOP":
#          break
print(Grade_Storage)
WeightedS=sum(Grade_Storage) #The weighted sum
WeightedA = WeightedS/(len(Grade_Storage)) # the weighted average
print("Weighted Sum:", WeightedS, "Weighted Average:", WeightedA)
#6
# I'm actually really bad at CSC 102 standardized pseudo code. Pseudo code is originally supposed to be subjective, but since
# this is a class, that needs a grade, there has to be a standard that everyone follows. If its subjective I can write it
# easy peasy. But I can't guarantee what I write will be acceptable in the exams. Only in real world scenarios.
# Therefore i won't answer b,c,d,e. The rest should be applicable in exams tho.

#a
# 1. START
# 2. INPUT X, Y, Z
# 3. LET A = SQR X + SQR Y + SQR Z
# 4. END
#b
#c
#d
# 1.START
# 2. INPUT A,B,C,D,E
# 3. LET Z = A+B+C+D+E
# 4.END
#e

#7

#A
#Selection because the students will be split based on the condition "if" the last digit of their number is even or odd

#b
# Student_No_Last_Digit=[]
# def last_digi_sum():
#     while True:
#         Student_No = input("Enter Student no. Type 'STOP' to terminate.")
#         if Student_No == "STOP":
#             break
#         Student_No_Last_Digit.append(Student_No[-1])
# last_digi_sum()
# sum(Student_No_Last_Digit)
#
# #c
# if n%2==0:
#     Even_list.append(n)
# #d
# max(Even_list)

#e
# max(Student_No_Last_Digit)

#f
#What code below???

# #8
# ii.for loop
# Celcior_List= []
# Farenhior_List = []
# for temperatures in range(0,110,10):
#     Celcior_List.append(temperatures)
# for newTemp in Celcior_List:
#     newTemp= (9.0/5) *newTemp + 32
#     Farenhior_List.append(newTemp)
#
# print(Celcior_List)
# print(Farenhior_List)
#
# i.while loop
# While_CelciorL=[]
# While_FarenhiorL=[]
# counter = 0
# x = 0
# z = 0
# while counter < 11:
#     counter += 1
#     z = x * (9.0 / 5) + 32
#     While_CelciorL.append(x)
#     While_FarenhiorL.append(z)
#     x += 10
#
# print(While_CelciorL)
# print(While_FarenhiorL)

# def CelciorConverter(celcs):
#     Faren = celcs*(9.0/5) + 32
#     print("Your temp in faren is", Faren, "degrees")
# CelciorConverter(62)

#I prefer to use this method instead of using the return within the function because if you want to see this function's return
#value you must explicitly use print outside the function. So, its much more practical to use the print inside the function,
#for me atleast.

#iv Dictionary
# Celcior_List= []
# Celcior_FarenDict = {}
# for temperatures in range(0,110,10):
#     Celcior_List.append(temperatures)
# for temp in Celcior_List:
#     Celcior_FarenDict[temp]= temp*(9.0/5) + 32
# print(Celcior_FarenDict)


#v Weather Warning

# def Weather_Warning():
#     Celcior_Input = float(input("Enter your value in celsius"))
#     Faren_Convertor = Celcior_Input*(9.0/5) + 32
#     if Faren_Convertor < 30:
#         print("ALERT! WEATHER IS VERY COLD")
#     elif Faren_Convertor > 90:
#         print("ALERT! WEATHER IS VERY HOT")
# Weather_Warning()

#9
#a
#infile = open("Cgpa.txt", "r")
#infile.write("") #append whatever cgpa you please inbewteen the quotes

#b
# count = 0
# for lines in infile:
#     count += 1
# print("The no of lines in the file is ", count)

#c
#Average = s/count
# #I highly doubt that this is feasible in just one line of code, as you'd need atleast two. One to define
#the sum(s) and the other to define the average.

#d
# outfile = open("cgpaOUT.txt", "w")
#
# #e
# outfile.write(str(Average), str(count))
#If you made it this far, I am proud of you. Random stranger. Strive harder, and harder,

#All praise is due to Allah, the Lord of The Worlds. May he allow us to dedicate our hearts to the things we love.
#May he steal our hearts.