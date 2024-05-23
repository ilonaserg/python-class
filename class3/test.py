#!workspace/bin/python

# Logic 
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# if NUMBER1 is NUMBER2:
#     print("They are equal")
# else:
#     print("They are not equal")



# NUMBER1 = 10
# NUMBER2 = 10 

# # if sentence
# if NUMBER1 == NUMBER2:
#     print("They are equal")
# elif NUMBER2 == NUMBER1:
#     print("Of course they are equal")  
# else:
#     print("They are not equal")
   
# Nested if sentence

# FRUIT = "apple"
# COLOR = "red"
# SIZE  = "big"

# if FRUIT == "apple":
#     print("the fruit is apple")
#     if COLOR == "red":
#         print("the color is red")
#         if SIZE == "big":
#             print("the fruit is big")


# import os  

# FILENAME = os.path.isfile("/etc/passwd")

# if FILENAME:
#     print("The file exists")
# else:
#     print("The file does not exist")


# FOLDERNAME = os.path.isdir("/tmp")

# if FOLDERNAME:
#     print("Folder exists")
# else: 
#     print("Folder does not exist")



# RESPONSE = int()

# try:
#     RESPONSE = int(input("When were you born: "))
# except ValueError:
#     print("Only digits are accepted. Please type number e.g 2000")

# if RESPONSE >= 2025:
#     print("You are not born yet")

# elif RESPONSE >= 2000 and RESPONSE <= 2024:
#     print("You were born in 21st century")

# elif RESPONSE <= 1999 and RESPONSE >= 1990:
#     print("You are in your 30th")

# elif RESPONSE <= 1989 and RESPONSE >= 1980:
#     print("You are in your 40th")

# else:
#     print("try again")


# in operator 
# HIDDEN_FRUIT = "banana"

# FRUIT_LIST1 = ["apple", "mango", "banana"]
# FRUIT_LIST2 = ["pear", "melon", "apricot"]
# FRUIT_LIST3 = ["peach", "grape", "kiwi"]

# if HIDDEN_FRUIT in FRUIT_LIST1:
#     print("%s is in List1" % HIDDEN_FRUIT)
# elif HIDDEN_FRUIT in FRUIT_LIST2:
#     print("%s is in List2" % HIDDEN_FRUIT)
# elif HIDDEN_FRUIT in FRUIT_LIST3:
#     print("%s is in list3" % HIDDEN_FRUIT)
# else: 
#     print("Hidden fruit is not found")


# %s   string 
# %d   digit




# RESPONSE = input("Please enter your name: ")
# GREETING = "Hello"

# print("%s %s" % (GREETING,RESPONSE))