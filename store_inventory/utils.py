import datetime


def clean_price(price_str):
    parse_to_float = float(price_str.replace("$", ""))
    return int(parse_to_float * 100)


def clean_date(date_str):
    split_date = date_str.split("/")

    month = int(split_date[0])
    day = int(split_date[1])
    year = int(split_date[2])

    return datetime.date(year, month, day)


def handle_product_input(sentence):
    # Keep asking for product name if something went wrong
    while True:
        try:
            return int(input(sentence))
        except:
            print("Failed when entering input...")
