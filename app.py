import csv
import datetime

from models import Base, engine, Product, session


def clean_price(price_str):
    parse_to_float = float(price_str.replace("$", ""))

    return int(parse_to_float * 100)


def clean_date(date_str):
    split_date = date_str.split("/")

    month = int(split_date[0])
    day = int(split_date[1])
    year = int(split_date[2])

    return datetime.date(year, month, day)


def add_csv():
    with open("inventory.csv") as csv_file:
        products_data = list(csv.DictReader(csv_file))

        for product in products_data:
            name = product["product_name"]
            price = clean_price(product["product_price"])
            quantity = int(product["product_quantity"])
            date = clean_date(product["date_updated"])

            product_in_db = session.query(Product).filter(Product.name == name).one_or_none()

            if product_in_db == None:
                new_product = Product(
                    name=name,
                    price=price,
                    quantity=quantity,
                    date=date
                )
                session.add(new_product)
        
        session.commit()


def display_menu():
    menu_options = ["V", "A", "B", "L", "E"]

    print("""
        \nSTORE INVENTORY
        \rV) View a single product's inventory
        \rA) Add a new product to the database
        \rB) Make a backup of the entire inventory
        \rL) List all the products
        \rE) Exit the program
    """)

    while True:
        choice = input("What would you like to do?  ")

        if choice.upper() in menu_options:
            return choice
        else:
            print("""
                \nWrong input.
                \rPlease try again.
            """)


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
    product_price = input("Please enter the product price:  ")
    product_quantity = input("Please enter the product quantity:  ")
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


def exit_program():
    print("GoodBye")
    exit(0)


menu = [
    {
        "option_letter": "V",
        "func": display_one_product
    },
    {
        "option_letter": "A",
        "func": add_new_product
    },
    {
        "option_letter": "B",
        "func": make_backup
    },
    {
        "option_letter": "L",
        "func": display_all_products
    },
    {
        "option_letter": "E",
        "func": exit_program
    }
]


def app():
    add_csv()

    while True:
        menu_option = display_menu()
    
        option_group = filter(
            lambda option: option["option_letter"] == menu_option.upper(),
            menu
        )
        option_function = list(option_group)[0]["func"]

        option_function()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    
    app()