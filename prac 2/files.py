print("please enter your name")
name = input()
outfile = open("name.txt", 'w')
print("{}".format(name), file=outfile)
print("Your name has been stored {}".format(name))
outfile.close()


outfile = open("name.txt", "r")
person = outfile.readline()
print("your name is {}".format(person))
outfile.close()


numbers = open("numbers.txt").readlines()
print (numbers)
