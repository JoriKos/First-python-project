import os
import cmd

#function
def Function(x):
   print(x)

#print
print('Hello world')

#variables
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

#for loop
for x in "Hello":
    print(x)

#list

Function("test")