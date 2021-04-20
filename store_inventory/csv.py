import csv

from store_inventory.models import session, Product

from store_inventory.utils import clean_date, clean_price


def add_csv():
    with open("./store_inventory/inventory/inventory.csv") as csv_file:
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
