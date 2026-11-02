import csv

FILE_NAME = "sales.csv"


def load_sales():
    sales = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["Quantity"] = int(row["Quantity"])
                row["CostPrice"] = float(row["CostPrice"])
                row["SellingPrice"] = float(row["SellingPrice"])

                sales.append(row)

    except FileNotFoundError:
        print("Sales file not found!")

    return sales


def display_sales(sales):
    if not sales:
        print("No sales records available.")
        return

    print("\n--- Product Sales ---")

    for item in sales:
        print(
            item["Product"],
            "| Quantity:", item["Quantity"],
            "| Selling Price:", item["SellingPrice"]
        )


def calculate_revenue(sales):
    revenue = sum(
        item["Quantity"] * item["SellingPrice"]
        for item in sales
    )

    print("Total Revenue: Rs.", round(revenue, 2))


def calculate_profit(sales):
    profit = sum(
        item["Quantity"] *
        (item["SellingPrice"] - item["CostPrice"])
        for item in sales
    )

    print("Total Profit: Rs.", round(profit, 2))


def best_selling_product(sales):
    if not sales:
        print("No sales records available.")
        return

    product_totals = {}

    for item in sales:
        name = item["Product"]

        product_totals[name] = (
            product_totals.get(name, 0) + item["Quantity"]
        )

    best = max(product_totals, key=product_totals.get)

    print("Best Selling Product:", best)
    print("Quantity Sold:", product_totals[best])


def search_product(sales):
    name = input("Enter product name: ").strip().lower()

    found = False

    for item in sales:
        if item["Product"].lower() == name:
            revenue = item["Quantity"] * item["SellingPrice"]

            print("Product:", item["Product"])
            print("Quantity:", item["Quantity"])
            print("Revenue: Rs.", round(revenue, 2))

            found = True

    if not found:
        print("Product not found!")


sales = load_sales()

while True:
    print("\n===== SALES ANALYZER =====")
    print("1. Display Sales")
    print("2. Calculate Revenue")
    print("3. Calculate Profit")
    print("4. Best Selling Product")
    print("5. Search Product")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_sales(sales)

    elif choice == "2":
        calculate_revenue(sales)

    elif choice == "3":
        calculate_profit(sales)

    elif choice == "4":
        best_selling_product(sales)

    elif choice == "5":
        search_product(sales)

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice!")
