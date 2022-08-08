#There are 4 solutions for no 1. Don't mind them. Just pick the easiest one for you then move on.

#solluton1 for no 1
#age1 = int(input("Enter the first age"))
#age2 = int(input("Enter the second age")) 
#age3= int(input("Enter the third age"))
#age4 = int(input("Enter the fourth age")) input("LOL HOW R U")
#age5 = int(input("Enter the fifth age"))
#
#sum = age1 + age2 + age3 + age4 + age5
#ageAVRG = sum/5
#
#print("The sum is", sum)
#print("And the avrg is", ageAVRG)

#solution2 for no 1
s = 0
ages = [1, 1, 1, 1]
for age in ages:
    s = s + age
print("da sum is", s)
print(s/len(ages))


#solution3 for no 1
c = 0
s = 0
while c<5:
        age = int(input("Enter age"))
        s = age + s
        c += 1
        if c==5:
            break
#print("sum is", s)
#print("class avrg is", s/c)

# solution 4 for no 1
#ages = [1, 1, 1, 1]
#print("The sum of ages is:", sum(ages))
#print("The class average is", sum(ages)/len(ages))

#no 2
#symp1 = input ("Enter the first symptom")
#symp2 = input("Enter the second symptom")
#symp3 = input("Enter the third symptom")

#print("The first symptom is",symp1)
#print("The second symp is", symp2)
#print("The third symp is", symp3)

#Don't mind the solution below. I was having a little too much fun in class.

#symp1 = input ("Enter the first symptom")
#symp2 = input("Enter the second symptom")
#symp3 = input("Enter the third symptom")
#
#if(symp1=="fever" and symp2=="headache" and symp3=="temperature"):
#    print("lol ur down bad fam. you have malaria. go get that checked out bro")
#elif(symp1 == "headache" and symp2=="sorethroat" and symp3=="cold"):
#    print("COVID! YOU HAVE COVID! RUN! THEY HAVE COVID!")
#else:
#    print("Sory fam. you're way beyond my help")

#no 3

# def Student_Info():
#     FName = input("Enter Your First Name")
#     LName = input("Enter your Last Name")
#     Gender = input("Enter your gender")
#     Age = int(input("Enter your age"))
#     Height = float(input("enter your height in meters")

#no 4
n =int(input("Enter no of students"))
counter = 0
agesum = 0
while(counter<n):
    age = int(input("Enter students age"))
    agesum = agesum + age
    counter += 1
print(agesum)

#print("The sum of the university students age is", agesum)
#print("\nintergers\tsquare\tCube")

#5
#for i in range (10):
#    square = pow(i,2)
#    cube = pow(i, 3)
#    print(i,"\t", square, "\t", cube)

#6
score = int(input("Enter the score"))
scoresum = 0
c = 0
while(score!=0):
    scoresum += score
    c += 2
    score = int(input("Enter the score"))
print("The sum is", scoresum)
print("the avrg is", scoresum/c)

##NO 7
#farenheitemp= float(input("Enter your temperature in farehnheit"))
#Celciustemp = (farenheitemp - 32) * 5/9
#print("your temperature in celcius is", Celciustemp)
#
##NO 8
##this will display all the odd and even numbers in a given set
#set = [1,2,3,4,5,6,7,8,9,10]
#print("List of evenNo.", "list of oddNo.")
#for numbers in set:
#    if numbers % 2==0:
#        print("\t" ,numbers)
#    else:
#        print( "\t", "\t", "\t", "\t", "\t",numbers)
#

#this will count all the odd and even numbers in the set
#Counteven = 0
#Countodd =0
#for numbers in set:
#    if numbers % 2==0:
#        Counteven += 1
#    else:
#        Countodd += 1
#print('Odd numbers occur', Countodd, "times")
#print('even numbers occur', Counteven, 'times')

#this will do both

set = [23232,323232,323233,45656,56465,354556,]
Counteven = 0
Countodd =0
print("List of evenNo.", "list of oddNo.")
for numbers in set:
    if numbers % 2==0:
        print("\t" ,numbers)
        Counteven += 1
    else:
       Countodd += 1
       print( "\t", "\t", "\t", "\t", "\t",numbers)

print('Odd numbers occur', Countodd, "times")
print('even numbers occur', Counteven, 'times')