import utils.database
import sqlite3

USER_CHOICE = """
Enter:
- 'a' to add a book.
- 'l' to list all books.
- 'r' to mark a book as read.
- 'd' to delete a book.
- 'q' to quit.

Your choice : """

def menu():
    user_input = input(USER_CHOICE).lower()

    while user_input != 'q':
        if user_input == 'a':
            user_book = input("Type in the name of the book here:  ").title()
            user_author = input("Type in the author of the book here:  ").title()
            user_input = input("Now what?:  ")
            utils.database.create_book_table()
            utils.database.book_adder(user_book, user_author)


        elif user_input == 'l':
            print(utils.database.book_displayer())
            user_input = input("Now what?:  ")

        elif user_input == 'r':
            input1 = input("Which book did you read?:  ").title()
            utils.database.book_marker(input1)
            print('Done!')
            user_input = input("Now what?:  ")

        elif user_input == 'd':
            input2 = input("Which book do you want to delete?:  ").title()
            utils.database.books = utils.database.book_deleter(input2)
            print("Done!")
            user_input = input("Now what?:  ")


        else:
            user_input = input("User input not correct please try again :")


menu()
print("Exiting program....")






