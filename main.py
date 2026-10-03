import os
import csv

# CSV FILE

file_nam = "Data.csv"
if not os.path.exists(file_nam):
    with open(file_nam, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Product Name",
            "Product ID",
            "Product Price",
            "Product Quantity",
            "Sold Quantity"
        ])

# ADD PRODUCT

def add_product():
    product_name = input("Enter Product Name = ").title()
    product_id = input("Enter Product ID = ").upper()
    product_price = float(input("Enter Product Price = "))
    product_quantity = int(input("Enter Product Quantity = "))
    with open(file_nam, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            product_name,
            product_id,
            product_price,
            product_quantity
        ])
    print("Product Added Successfully!")

# VIEW PRODUCTS

def view_product():
    with open(file_nam, "r", newline="") as f:
        reader = csv.DictReader(f)
        found = False
        for prd in reader:
            found = True
            print("Product Name =", prd["Product Name"])
            print("Product ID =", prd["Product ID"])
            print("Product Price =", prd["Product Price"])
            print("Product Quantity =", prd["Product Quantity"])
            print("Sold Quantity =", prd["Sold Quantity"])
            print("----------------------------")

        if not found:
            print("No Products Available!")

# SEARCH PRODUCT

def search_product():
    user_id = input("Enter Product ID = ").upper()
    with open(file_nam, "r", newline="") as f:
        reader = csv.DictReader(f)
        found = False
        for prd in reader:
            if prd["Product ID"] == user_id:
                found = True
                print("----------------------------")
                print("Product Name =", prd["Product Name"])
                print("Product ID =", prd["Product ID"])
                print("Product Price =", prd["Product Price"])
                print("Product Quantity =", prd["Product Quantity"])
                print("Sold Quantity =", prd["Sold Quantity"])

        if not found:
            print("Product Not Found!")

# UPDATE PRODUCT

def update_product():
    user_id = input("Enter Product ID To Update = ").upper()
    products = []
    found = False
    with open(file_nam, "r", newline="") as f:
        reader = csv.DictReader(f)
        for prd in reader:
            if prd["Product ID"] == user_id:
                found = True
                print("Product Found!")

                new_name = input("Enter New Product Name = ").title()
                new_price = float(input("Enter New Product Price = "))
                new_quantity = int(input("Enter New Product Quantity = "))

                prd["Product Name"] = new_name
                prd["Product Price"] = new_price
                prd["Product Quantity"] = new_quantity
            products.append(prd)
    if found:
        with open(file_nam, "w", newline="") as f:
            fieldnames = [
                "Product Name",
                "Product ID",
                "Product Price",
                "Product Quantity",
                "Sold Quantity"
            ]
            writer = csv.DictWriter(
                f,
                fieldnames=fieldnames
            )
            writer.writeheader()
            writer.writerows(products)
        print("Product Updated Successfully!")

    else:
        print("Product ID Not Found!")

# DELETE PRODUCT

def delete_product():

    user_id = input("Enter Product ID To Delete = ").upper()

    products = []
    found = False
    with open(file_nam, "r", newline="") as f:
        reader = csv.DictReader(f)
        for prd in reader:
            if prd["Product ID"] == user_id:

                found = True

            else:
                products.append(prd)

    if found:
        with open(file_nam, "w", newline="") as f:
            fieldnames = [
                "Product Name",
                "Product ID",
                "Product Price",
                "Product Quantity",
                "Sold Quantity"
            ]

            writer = csv.DictWriter(
                f,
                fieldnames=fieldnames
            )
            writer.writeheader()
            writer.writerows(products)

        print("Product Deleted Successfully!")

    else:
        print("Product ID Not Found!")


# MANAGE STOCK

def manage_stock():
    user_id = input("Enter Product ID = ").upper()
    products = []
    found = False
    with open(file_nam, "r", newline="") as f:
        reader = csv.DictReader(f)
        for prd in reader:
            if prd["Product ID"] == user_id:
                found = True
                print("1. Add Stock")
                print("2. Sell Product")
                choice = int(input("Enter Choice = "))
                quantity = int(input("Enter Quantity = "))
                current_quantity = int(prd["Product Quantity"])
                sold_quantity = int(prd["Sold Quantity"])

                if choice == 1:

                    prd["Product Quantity"] = (
                        current_quantity + quantity
                    )

                    print("Stock Added Successfully!")

                elif choice == 2:

                    if quantity <= current_quantity:

                        prd["Product Quantity"] = (
                            current_quantity - quantity
                        )

                        prd["Sold Quantity"] = (
                            sold_quantity + quantity
                        )

                        print("Product Sold Successfully!")

                    else:
                        print("Not Enough Stock!")

                else:
                    print("Invalid Choice!")

            products.append(prd)

    if not found:
        print("Product ID Not Found!")

    else:

        with open(file_nam, "w", newline="") as f:

            fieldnames = [
                "Product Name",
                "Product ID",
                "Product Price",
                "Product Quantity",
                "Sold Quantity"
            ]

            writer = csv.DictWriter(
                f,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(products)

# TOTAL INVENTORY VALUE

def calculate_total_price():
    total = 0
    with open(file_nam, "r", newline="") as f:
        reader = csv.DictReader(f)
        for prd in reader:
            price = float(prd["Product Price"])
            quantity = int(prd["Product Quantity"])
            total = total + (price * quantity)

    print("----------------------------")
    print("Total Inventory Value =", total)

# STOCK INFORMATION

def stock_information():

    total_products = 0
    total_stock = 0
    total_sold = 0
    total_sales = 0
    low_stock = 0
    out_of_stock = 0

    with open(file_nam, "r", newline="") as f:

        reader = csv.DictReader(f)

        for prd in reader:

            total_products += 1

            price = float(prd["Product Price"])
            quantity = int(prd["Product Quantity"])
            sold = int(prd["Sold Quantity"])

            total_stock += quantity
            total_sold += sold
            total_sales += price * sold

            if quantity == 0:

                out_of_stock += 1

            elif quantity <= 5:

                low_stock += 1

    print(" INVENTORY REPORT")

    print("Total Products =", total_products)
    print("Total Stock =", total_stock)
    print("Total Sold Quantity =", total_sold)
    print("Total Inventory Value =", total_stock)
    print("Total Sales =", total_sales)
    print("Low Stock Products =", low_stock)
    print("Out Of Stock Products =", out_of_stock)

# MAIN MENU

def main_interface():

    while True:

        print("PRODUCT MANAGEMENT SYSTEM")

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Manage Stock")
        print("7. Calculate Total Price")
        print("8. Stock Information")
        print("9. Exit")

        user_choice = int(input("Enter Your Choice = "))
        if user_choice == 1:
            add_product()
        elif user_choice == 2:
            view_product()
        elif user_choice == 3:
            search_product()
        elif user_choice == 4:
            update_product()
        elif user_choice == 5:
            delete_product()
        elif user_choice == 6:
            manage_stock()
        elif user_choice == 7:
            calculate_total_price()
        elif user_choice == 8:
            stock_information()
        elif user_choice == 9:
            print("Program Closed!")
            break
        else:
            print("Invalid Choice!")
main_interface()