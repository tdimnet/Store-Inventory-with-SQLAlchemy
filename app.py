import csv

from models import Base, engine


def app():
    print("====")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    
    app()
