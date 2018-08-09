"""Peter Stone"""


def main():
    password = get_password()
    censoring(password)


def censoring(password):
    for char in password:
        print("*", end="")


def get_password():
    password = input("password: ")
    while len(password) < 5:
        password = input("invalid password ")
    return password


main()
