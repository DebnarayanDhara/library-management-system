#region program start







#region add book
def add_book(books):

    title = input("Enter Book Title: ").strip().title()
    author = input("Enter Author Name: ").strip().title()

    if not title or not author:
        print("Title and Author cannot be empty!")
        return

    books.append({
        "title": title,
        "author": author,
        "issued": False
    })

    print("Book Added Successfully!")
#endregion

#region View Books
def view_books(books):

    if not books:
        print("No Books Found!")
        return

    print("\n--------Books--------")

    for i, book in enumerate(books, start=1):

        status = "Issued" if book["issued"] else "Available"

        print(
            f"{i}. {book['title']} - "
            f"{book['author']} [{status}]"
        )

#endregion

#region Search Book

def search_book(books):

    keyword = input("Enter Book Title: ").strip().lower()

    found = False

    for book in books:

        if keyword in book["title"].lower():

            status = "Issued" if book["issued"] else "Available"

            print(
                f"{book['title']} - "
                f"{book['author']} [{status}]"
            )

            found = True

    if not found:
        print("Book Not Found!")

#endregion

#region Issue Book

def issue_book(books):

    view_books(books)

    if not books:
        return

    try:

        book_num = int(input("Enter Book Number: "))

        if 1 <= book_num <= len(books):

            if books[book_num - 1]["issued"]:
                print("Book Already Issued!")

            else:
                books[book_num - 1]["issued"] = True
                print("Book Issued Successfully!")

        else:
            print("Invalid Book Number!")

    except ValueError:
        print("Please Enter a Valid Number!")

#endregion

#region Return Book

def return_book(books):

    view_books(books)

    if not books:
        return

    try:

        book_num = int(input("Enter Book Number: "))

        if 1 <= book_num <= len(books):

            if not books[book_num - 1]["issued"]:
                print("Book Is Already Available!")

            else:
                books[book_num - 1]["issued"] = False
                print("Book Returned Successfully!")

        else:
            print("Invalid Book Number!")

    except ValueError:
        print("Please Enter a Valid Number!")

#endregion

#region Delete Book

def delete_book(books):

    view_books(books)

    if not books:
        return

    try:

        book_num = int(input("Enter Book Number to Delete: "))

        if 1 <= book_num <= len(books):

            removed = books.pop(book_num - 1)

            print(f"Deleted: {removed['title']}")

        else:
            print("Invalid Book Number!")

    except ValueError:
        print("Please Enter a Valid Number!")

#endregion

#region Statistics

def show_statistics(books):

    total = len(books)

    issued = sum(book["issued"] for book in books)

    available = total - issued

    print("\n----- STATISTICS -----")
    print(f"Total Books     : {total}")
    print(f"Available Books : {available}")
    print(f"Issued Books    : {issued}")

#endregion

#region Main Function
books = []

while True:

        print("\n" + " LIBRARY MANAGEMENT SYSTEM ".center(50, "="))
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Statistics")
        print("8. Exit")

        choice = input("Choose Option: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            view_books(books)

        elif choice == "3":
            search_book(books)

        elif choice == "4":
            issue_book(books)

        elif choice == "5":
            return_book(books)

        elif choice == "6":
            delete_book(books)

        elif choice == "7":
            show_statistics(books)

        elif choice == "8":
            print("Thanks for using Library Management System!")
            break

        else:
            print("Invalid Choice!")

#endregion
#region End Of Program
