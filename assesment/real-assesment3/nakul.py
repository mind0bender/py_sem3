booksList = [("Book1", 4), ("Book2", 3), ("Book3", 1)]
operationsList = [
    ("checkout", "Book3"),
    ("checkout", "Book3"),
    ("return", "Book3"),
]


def manage_library(books, operations):
    for i in range(len(operations)):
        if operations[i][0] == "checkout":
            for i in range(len(books)):
                if books[i][0] == operations[i][1] and books[i][1]:
                    books[i] = (books[i][0], books[i][1] - 1)
        if operations[i][0] == "return":
            for i in range(len(books)):
                if books[i][0] == operations[i][1]:
                    books[i] = (books[i][0], books[i][1] + 1)
            books.append((operations[i][1], 1))
    return books


print(manage_library(booksList, operationsList))
