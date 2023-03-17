#A question about def

num1 = int(input("Please enter the first number: \n"))
num2 = int(input("Please enter the second number: \n"))
num3 = int(input("Please enter the third number: \n"))
num4 = int(input("Please enter the fourth number: \n"))

list1 = [num1, num2, num3, num4]

def sum (list): 
    total = 0
    for item in list: 
        total += item
    print ("\nThe sum of the numbers in the list is", total)
    return total
    
sum(list1)