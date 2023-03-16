# find the password game

# password = "thisisthepassword"
passwd = [i^0x214 for i in [608, 636, 637, 615, 637, 615, 608, 636, 625, 612, 629, 615, 615, 611, 635, 614, 624]]

password = input("here is my locker, what's my password? ")
if passwd == password:
    print("you got it!")
else:
    print("wrong password")

