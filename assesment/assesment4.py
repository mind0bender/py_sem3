inventory = [
    {"productId": "P001", "stock": 20, "location": "Aisle 1"},
    {"productId": "P002", "stock": 5, "location": "Aisle 2"},
    {"productId": "P003", "stock": 15, "location": "Aisle 3"},
    {"productId": "P004", "stock": 2, "location": "Aisle 4"},
    {"productId": "P005", "stock": 30, "location": "Aisle 5"},
]

LOW_STOCK_THRESHOLD = 10

lowStockItems = [item for item in inventory if item["stock"] < LOW_STOCK_THRESHOLD]


def bubbleSort(stocks):
    n = len(stocks)
    for i in range(n):
        for j in range(0, n - i - 1):
            if stocks[j]["stock"] > stocks[j + 1]["stock"]:
                stocks[j], stocks[j + 1] = stocks[j + 1], stocks[j]
    return stocks


sortedLowStockIitems = bubbleSort(lowStockItems)

for item in sortedLowStockIitems:
    print(
        f"Product ID: {item['productId']}, Stock: {item['stock']}, Location: {item['location']}"
    )

print("Yash Gupta\t23bcs11317")
