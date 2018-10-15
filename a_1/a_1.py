"""
Peter Stone. jc389014, 28/08/2018. This programm manages a simple csv list file of books, both read and unread for
a user. GitHub: https://github.com/PeterStone4818/CP1404pracs/tree/master/a_1
"""
import csv

MENU_CHOICES = ['L', 'A', 'C', 'Q']


def main():
    book_list = file_read()
    menu_choice = 'L'
    print("Reading Tracker 1.0 - by Peter Stone\n" + str(len(book_list)) + " books loaded")
    while menu_choice.upper() != 'Q':
        print("L - list books\nA - Add new book\nC - Complete a book\nQ - Quit")
        menu_choice = str(input())
        while menu_choice.upper() not in MENU_CHOICES:
            try:
                menu_choice = input(print("Please enter a valid option."))
            except ValueError:
                print("invalid option")
        if menu_choice.upper() in 'L':
            printing_books(book_list)
        elif menu_choice.upper() in 'C':
            complete = complete_book(book_list)
            book_list[complete][4] = 'y'
        elif menu_choice.upper() in 'A':
            book_list.append(add_book())
    file_writer(book_list)
    print("you have quit the program.")


#  open file
#  read file
#  for each row save as a list of lists
#  add a book position to list of list
#  return book list.


def file_read():
    books = 0
    position = 0
    with open('books.csv') as f:
        reader = csv.reader(f)
        book_list = list(reader)
    for row in book_list:
        books = books + 1
        row.insert(position, books)
    return book_list


#   request for book completion
#   set options parameters
#   input for request
#   check input against options list
#   send valid input back to main function.
def complete_book(book_list):
    print("Enter the number of the completed song.")
    options = []
    for row in book_list:
        if str(row[3]) is 'r':
            options.append(int(row[0]))
    complete = int(input())
    while complete not in options:
        int(input("invalid option."))
    return complete


def printing_books(book_list):
    for row in book_list:
        if str(row[3]) in 'y':
            print('{}. * {} by {} with {} pages, {} '.format(*row))
        else:
            print('{}.   {} by {} with {} pages, {}'.format(*row))
    print("\n\n\n")


def add_book():
    title = input("Title:")
    while len(title) < 1:
        title = input("Error, Field cannot be blank")
    author = input("Author:")
    while len(author) < 1:
        author = input("Error, Field cannot be blank")
    num_pages = int(input("pages:"))
    while num_pages <= 0:
        num_pages = int(input(""))
    print("{} {} {} was added to your list.".format(title, author, num_pages))
    new_book = [title, author, num_pages, 'r']
    return new_book


def file_writer(book_list):
    iteration = -1
    for row in book_list:
        iteration = iteration + 1
    with open('books.csv', 'w', newline='') as l:
        writer = csv.writer(l)
        writer.writerows(book_list)


main()
