# Distributing candy with a while loop

jar_of_candy = 10
number_of_friends = 0

while jar_of_candy > 0:
    if number_of_friends < 5:
        print("Giving candy to friend", number_of_friends + 1)
        candy_given = min(jar_of_candy, 3)
        jar_of_candy -= candy_given
        print(candy_given, "pieces of candy given")
        number_of_friends += 1
    else:
        print("Too many friends!")
        break

print("No more candy left!")
