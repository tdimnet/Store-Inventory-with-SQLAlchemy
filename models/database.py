from sqlalchemy import create_engine, text


engine = create_engine("sqlite:///inventory.db", echo=True)


def hello_world():
    with engine.connect() as conn:
        result = conn.execute(text("Select 'hello world'"))
        print(result.all())


def create_table():
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))


def write_data():
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
        )
        conn.commit()


def read_data():
    with engine.connect() as conn:
        result = conn.execute(text("Select * from some_table"))
        print(result.all())