from store_inventory.models import Base, engine
from store_inventory.csv import add_csv
from store_inventory.commands import (
    add_new_product,
    display_all_products,
    display_one_product,
    exit_program,
    make_backup
)

from store_inventory.utils import handle_product_price_input


MENU = [
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


def display_menu():
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

        if choice.upper() in [option["option_letter"] for option in MENU]:
            return choice
        else:
            print("""
                \nWrong input.
                \rPlease try again.
            """)


def app():
    add_csv()

    while True:
        menu_option = display_menu()
    
        # Retrieve the function in the MENU matching the letter choese by the user
        option_group = filter(
            lambda option: option["option_letter"] == menu_option.upper(),
            MENU
        )
        option_function = list(option_group)[0]["func"]
        option_function()


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    app()
