#!workspace/bin/python
import time 
# Reserved words by python 
# if, in, for, not, while, continue, break



# FRUIT = ["apple", "pear", "banana"]

# for items in FRUIT: 
#     print(items)



# for items in range(10):
#     print(items + 1)


# chmod +x  filename.py 

# #!workspace/bin/python

# ./filename.py 


# python filename


# FILE1 = open("/etc/passwd")

# for lines in FILE1:
#     time.sleep(0.1)
#     print(lines.strip())

# FILE1.close()

# import string 

# # dir = ls 
# print(dir(string))

# # for letters in string.ascii_lowercase:
# #     print(letters)

# for letters in string.ascii_uppercase:
#     print(letters)

USERLIST = ["john", "smith", "3121233213", "a@gmail.com"]


# Prints out everything
# for items in USERLIST:
#     print(items)


# for items in USERLIST:
#     if items.isnumeric():
#         print(items)

# for items in USERLIST:
#     if items.isalpha():
#         print(items)

# for items in USERLIST:
#     if items.endswith(".com"):
#         print(items)

# for items in USERLIST:
#     if items.isalpha():
#         print(items.capitalize())


# for items in USERLIST:
#     if items == "smith":
#         break

#     print(items)

# TOTAL_PRODUCTS = ["bread", "meat", "cheese", "carrot", "rice", "potato"]
# WE_HAVE = ["bread", "meat"]

# for items in TOTAL_PRODUCTS:
#     if items not in WE_HAVE:
#         print("We need to buy %s" % items)

# LIST_OF_NUMBERS = [1,2,3,4,5,6,7]

# for items in LIST_OF_NUMBERS:
#     # find even number 
#     if items % 2 == 0:
#         print(items)

# for items in LIST_OF_NUMBERS:
#     # find odd number 
#     if items % 2 != 0:
#         print(items)



# NUMBER = 0

# while  NUMBER != 5:
#     time.sleep(0.2)
#     NUMBER = NUMBER + 1 
#     print(NUMBER)


# RESPONSE = int()
# while True:
#     try:
#         RESPONSE = int(input("When were you born: "))
#         if RESPONSE >= 2025:
#             print("You are not born yet")

#         elif RESPONSE >= 2000 and RESPONSE <= 2024:
#             print("You were born in 21st century")

#         elif RESPONSE <= 1999 and RESPONSE >= 1990:
#             print("You are in your 30th")

#         elif RESPONSE <= 1989 and RESPONSE >= 1980:
#             print("You are in your 40th")

#         else:
#             print("try again")
            
#     except ValueError:
#         print("Only digits are accepted. Please type number e.g 2000")


ANSWER = "no"

while ANSWER != "yes":
    ANSWER = str(input("Are you crazy?: "))
    if ANSWER == "yes":
        print("I knew that")




boto3 


["sec-ioio","sec-ioio","sec-ioio","sec-ioio","sec-ioio","sec-ioio"]
