"""Peter Stone"""

password = input("password: ")
while len(password) < 5:
    password = input("invalid password ")
char = len(password)
print ("*" * char)