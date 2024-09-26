from typing import Tuple, Literal, List

type Book = Tuple[str, int]

type OperationEnum = Literal["checkout", "return"]
type Operation = Tuple[OperationEnum, str]

booksList: List[Book] = [("Book1", 4), ("Book2", 3), ("Book3", 1)]
operationsList: List[Operation] = [
    ("checkout", "Book3"),
    ("checkout", "Book3"),
    ("return", "Book3"),
    ("return", "Book2"),
    ("checkout", "Book3"),
]


def checkoutBook(books: List[Book], title: str):
    for i in range(len(books)):
        book: Book = books[i]
        if book[0] == title and book[1] > 1:
            books[i] = (book[0], book[1] - 1)
            return


def returnBook(books: List[Book], title: str):
    for i in range(len(books)):
        book: Book = books[i]
        if book[0] == title:
            books[i] = (book[0], book[1] + 1)
            return
    books.append((title, 1))


def manage_library(books: List[Book], operations: List[Operation]):
    for operation in operations:
        match operation[0]:
            case "checkout":
                checkoutBook(books, operation[1])
            case "return":
                returnBook(books, operation[1])
            case _:
                print("Invalid Operation!")
    return books


final_state: List[Book] = manage_library(booksList, operationsList)

print(final_state)
