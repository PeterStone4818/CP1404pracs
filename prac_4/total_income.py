"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for total_months in range(1, months + 1):
        income = float(input("Enter income for total_months " + str(total_months) + ": "))
        incomes.append(income)

    income_report(incomes, months)


def income_report(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for total_months in range(1, months + 1):
        income = incomes[total_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(total_months, income, total))


main()