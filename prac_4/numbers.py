
numbers = []
for i in range(5):
    numbers.append(int(input("Please enter a number")))
current = 0
for i in range(5):
    print("Number: {:<3}".format(numbers[current]))
    current = current + 1
print("The first number is {}".format(numbers[0]))
print("the last number is {}".format(numbers[4]))
print("the smalles number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers {}".format(sum(numbers)/5))

