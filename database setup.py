# Create database tables and fake data
import db
from faker import Faker
from random import randint, choice

RECORD_COUNT = 50

def main():
    with db.cnx() as cnx, open("schema.sql") as schema:
        print("Create tables")
        cnx.cmd_query(schema.read())

    with db.cnx() as cnx, cnx.cursor() as cursor:
        print("Create data")
        cnx.database = db.SCHEMA

        print("\tCreate people")
        faker = Faker("en_GB")
        people = [
            (faker.unique.email(), faker.last_name(), faker.first_name())
            for _ in range(RECORD_COUNT)
        ]
        cursor.executemany(
            "INSERT INTO customer (email, surname, firstname) VALUES (%s, %s, %s)", people
        )
        cnx.commit()

        print("\tCreate products")
        products = [
            ("Widget", 100),
            ("Apple", 40),
            ("Arts Tower poster", 500),
            ("Stainless steel cutlery set", 4500),
            ("Henderson's Relish (1l)", 600)
        ]
        cursor.executemany(
            "INSERT INTO product (`name`, unit_price) VALUES (%s, %s)", products
        )
        cnx.commit()

        print("\tCreate orders")
        cursor.execute("SELECT id FROM customer")
        customer_ids = [x[0] for x in cursor.fetchall()]
        cursor.execute("SELECT id FROM product")
        product_ids = [x[0] for x in cursor.fetchall()]
        orders = [ # Create random orders
            (choice(customer_ids), choice(product_ids), randint(1,100)) for _ in range(RECORD_COUNT)
        ]
        cursor.executemany(
            "INSERT INTO `order` (customer_id, product_id, quantity) VALUES (%s, %s, %s)", orders
        )
        cnx.commit()


if __name__ == "__main__":
    main()
