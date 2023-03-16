#Adding numbers from the list
num1 = int(input("Please enter the first number: \n"))
num2 = int(input("Please enter the second number: \n"))
num3 = int(input("Please enter the third number: \n"))
num4 = int(input("Please enter the fourth number: \n"))

list = [num1, num2, num3, num4]

sum = 0
for item in list: 
    sum += item

print ("\nThe sum of the numbers in the list is", sum)

