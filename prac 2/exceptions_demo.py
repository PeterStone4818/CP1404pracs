"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? if either numerator or denominator values are not an integer
2. When will a ZeroDivisionError occur? if the denominator value is set to 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? yes by adding in an errorchecking loop.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Please provide a valid denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")