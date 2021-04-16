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

            new_product = Product(
                name=name,
                price=price,
                quantity=quantity,
                date=date
            )
            session.add(new_product)
        
        session.commit()



def app():
    print("====")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    
    add_csv()
    