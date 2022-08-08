#A program that determines the largest numbers out of three numbers

Numero_UNO = int(input("Enter the first number"))
Numero_DOS = int(input("Enter the second number"))
Numero_TRES = int(input("Enter the third number"))

if Numero_UNO > Numero_DOS and Numero_UNO > Numero_TRES:
    print(Numero_UNO, "is the largest number")
elif Numero_DOS > Numero_UNO and Numero_DOS > Numero_TRES:
    print(Numero_DOS, "is the largest number")
else: print(Numero_TRES, "is the largest number")

#write a program that determines if its a leap year

year = int(input("Enter year:"))
if year % 4==0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

score = int(input("ENTER YOUR FINAL EXAM SCORE"))
if score >= 70:
    print("your grade is A")
elif score>= 60 and score <70:
    print("Your grade is B")
elif 50<= score <60:
    print("Your grade is C")
elif 45<= score <50:
    print("Your grade is D")
elif 40<= score < 45:
    print("Your grade is E")
else:
    print('Your grade is f')
#the code above looks funky yea? its not. try it.