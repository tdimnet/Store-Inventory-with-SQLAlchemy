from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///inventory.db", echo=True)

with engine.connect() as conn:
    result = conn.execute(text("Select 'hello world'"))
    print(result.all())