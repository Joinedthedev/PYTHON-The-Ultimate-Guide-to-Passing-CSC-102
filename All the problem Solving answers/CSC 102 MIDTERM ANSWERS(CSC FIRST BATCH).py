#1."Sequence, computer programs run instructions in sequence, one after another, in the order in which they are written.
#The order in which instructions are executed in a program is called the flow of control.Selection when a computer is
# asked to make a choice, it carries out a process known as selection. Your job as the programmer is to provide:The
# statement that will be evaluated as either true or false.The code that will be executed if the statement is true.
# The code that will be executed if the statement is false.The flow of control is altered because some program
# statements will be skipped, depending on whether the statement evaluates to true or false.
#Iteration,To repeat instructions in a program multiple times, you can create a loop.
# There are two ways to determine how many times a loop will repeat.
#Count-controlled loops
#This type of loop will repeat instructions a specific number of times.
#Condition-controlled loops
#This type of loop will repeat until a specified condition is met. Just as with selection, a statement is evaluated
#and either found to be true or false. A while loop will run while the statement is true, and until it becomes false.

#1b
#a=int(input("enter a random radius"))
#b=int(input("enter a random radius"))
#c=int(input("enter a random radius"))
#
#max(a,b,c)
#min(a,b,c)
#
##2
#def my_function(v = 5):
#    myfuncsum=v +10
#    return myfuncsum
#print(my_function())
#
##3
#for intergers in range(1,100,1):
#    if (intergers%3==0) and (intergers%5==0):
#        print("FizzBuzz")
#    elif (intergers%3==0):
#        print("FIZZ")
#    elif (intergers%5==0):
#        print("Buzz")
#    else:
#        print(intergers)
#
#4

#x = input("Press d to convert dollar to naira or press n to convert naira to dollar")
#if (x == "d"):
#    USA = float(input("Enter the dollar amount"))
#    print("Your amount in naira is" , USA*480)
#elif (x == "n"):
#    Africa = float(input("Enter the naira amount"))
#    print("your amount in dollars is", Africa/500)

#5

#for val in "string":
#    if val == "i":
#        break
#    print(val)
#print("The end")
#The break statement in Python terminates the current loop and resumes execution at the next statement, therefore it
# prints s t r the end

for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")
#The continue statement in Python returns the control to the beginning of the while loop.
#therefore it prints s t r n g the end





