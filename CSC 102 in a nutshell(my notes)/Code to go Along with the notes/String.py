
#Fname = "Salim"
#
#for characters in Fname:
#    print(characters)
#print("The length of my first name is" , len(Fname))

#fruit = "pineapple"
#index = 0
#while index < len(fruit):
#    letter = fruit[index]
#    print(index, letter)
#    index += 1
def namecount():
    name = input("You there! What's your name?")
    index = 0
    for characters in name:
        if index < len(name):
            print(index, characters)
            index += 1

namecount()
def letterOccurence():
    count = 0
    word ='racecar'
    for letters in word:
        if letters == "r":
            count += 1
    print("The letter r occurs", count, "times")

def Nameshenanigans():
    UrFname = input("What is your name mortal?")
    UrLname = input("And your fathers?")
    print("Ah I see. So your first name is:" , UrFname)
    print("the last three letters of your first name are", UrFname[2:5])
    print('And it would seem the last two letters of your first name are:', UrFname[3:5])
    print("The last two letters of your last name are", UrLname[4:6])
    print("i SHALL COMBINE THEM, YOUR WARRIOR NAME IS:", UrFname[3:5]+UrLname[4:6])

def ASKEYYYYYYYYYYYYYYYYYYYYYYYYYYY():
    st = "Salim Babaji"
    if (st == 'Salim'):
        print('your', st, "comes at the same time as salim")
    elif(st<'salim'):
        print('your', st, "comes before salim")
    elif(st>'salim'):
        print('your', st, "comes after salim")
    print(st.lower())
    print(st.upper())
    print(st.replace('Salim', 'james'))
    print(st.replace("","replace"))

