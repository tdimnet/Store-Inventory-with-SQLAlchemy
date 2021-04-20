import csv
import datetime


from store_inventory.models import Product, session
from store_inventory.utils import handle_product_input


def display_all_products():
    index = 0
    for product in session.query(Product):
        print(product)
        
        index += 1

        # In a real project, I would add LIMIT and OFFSET
        if index % 10 == 0:
            input("\nPress enter to see the next ten objets")


def display_one_product():
    is_choosing = True

    while is_choosing:
        try:
            product_id = input("Please enter a product id?  ")
            product = session.query(Product).filter(Product.id == int(product_id)).one_or_none()
            print(product)
            is_choosing = False
        except:
            print("""
                \nAn error occurs.
                \rPlease try again
            """)

    input("Please press enter to continue...")


def add_new_product():
    product_name = input("Please enter the product name:  ")
    product_price = handle_product_input("Please enter the product price:  ")
    product_quantity = handle_product_input("Please enter the product quantity:  ")
    product_date = datetime.datetime.now().date()

    try:
        new_product = Product(
            name=product_name,
            price=product_price,
            quantity=product_quantity,
            date=product_date
        )
        session.add(new_product)
        
        session.commit()
    except:
        print("Failed when inserting new product")

    input("Please press enter to continue...")


def make_backup():
    print("Make backup")

    now = datetime.datetime.now().date()

    backup_csv_file = open(f"./store_inventory/backups/{now}.csv", "w")
    out = csv.writer(backup_csv_file)
    out.writerow(["name", "price", "quantity", "date"])

    for product in session.query(Product):
        out.writerow([
            product.name,
            product.price,
            product.quantity,
            product.date,
        ])
    
    backup_csv_file.close()


def exit_program():
    print("GoodBye")
    exit(0)
