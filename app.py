import csv


def hello_world():
    with open('inventory.csv', 'r') as csv_file:
        inventory = list(csv.DictReader(csv_file, delimiter=','))
        
        first_product = inventory[0]
        
        print("====")
        print(first_product["product_name"])
        print(first_product["product_price"])
        print(first_product["product_quantity"])
        print(first_product["date_updated"])
        print("====")

if __name__ == "__main__":
    hello_world()