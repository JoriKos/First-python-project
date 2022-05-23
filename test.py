import os
import cmd
import time

#function
def Function(x):
   print(x)

def sleep(x):
    time.sleep(x)

#print
print('Hello world')

#variables & input/output
while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number:"))
        break
    except:
        print("Enter a number!")

#if statement
if b > a:
    print('Number 2 is greater than number 1\n' + '2 has a value of: ' + str(b) + '\n' + '1 has a value of: ' + str(a))
elif a == b:
    print('The numbers are equal')
else:
    print('Number 1 is greater than number 2\n' + '1 has a value of: ' + str(a) + '\n' + '2 has a value of: ' + str(b))

sleep(1.5)
#for loop
for x in "Hello":
    sleep(0.3)
    print(x)

sleep(1.5)    
#list
testlist = ["test", 1, "help", 24, False]
testlist2 = [1, 2, 3, 4]

sleep(1.5)
#function
Function("test")

sleep(1.5)
#while loop, list printing
i = 0
while i < len(testlist2):
    sleep(0.3)
    print(testlist2[i])
    i += 1

sleep(1.5)
i = 0
while i < len(testlist):
    sleep(0.3)
    print(testlist[i])
    i += 1