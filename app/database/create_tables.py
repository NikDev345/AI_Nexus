from app.database.connection import engine
from app.database.models import Base


def create_tables():
    Base.metadata.create_all(bind=engine)

    print("Tables Created Successfully")


if __name__ == "__main__":
    create_tables()