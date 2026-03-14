# ETL script
import datetime

import db
import pandas as pd


def extract():
    with db.cnx() as cnx, cnx.cursor() as cursor:
        cnx.database = db.SCHEMA
        cursor.execute(
            """
            SELECT customer.id,
                   email,
                   surname,
                   firstname,
                   status,
                   `order`.id   AS order_id,
                   product.name AS product,
                   product.unit_price,
                   `order`.quantity,
                   `order`.timestamp
            FROM customer
                     LEFT JOIN (`order` INNER JOIN product ON product.id = `order`.product)
                               ON `order`.customer = customer.id
            ORDER BY customer.id
            """
        )
        return cursor.column_names, cursor.fetchall()


def transform(columns: list[str], rows: list):
    df = pd.DataFrame(columns=columns, data=rows)
    df["name"] = df["firstname"] + " " + df["surname"]
    df["value"] = df.apply(lambda row: row["unit_price"] * row["quantity"] if pd.notna(row["quantity"]) else None, axis=1)
    return df


def load(df):
    filename = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + ".csv"
    with open("output/" + filename, "xb") as file:
        df.to_csv(file, index=False)


def main():
    columns, rows = extract()
    df = transform(columns, rows)
    load(df)


if __name__ == "__main__":
    main()
