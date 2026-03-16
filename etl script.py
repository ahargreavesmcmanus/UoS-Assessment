#!/usr/bin/env python3
# ETL script
import datetime
import os

import db
import pandas as pd

OUTPUT_DIRECTORY = "output"


def extract():
    with db.cnx() as cnx, cnx.cursor() as cursor:
        cnx.database = db.SCHEMA
        cursor.execute(
            """
            SELECT customer.id,
                   email,
                   surname,
                   firstname,
                   customer_status.status,
                   `order`.id   AS order_id,
                   product.name AS product,
                   product.unit_price,
                   `order`.quantity,
                   `order`.timestamp
            FROM customer
                     INNER JOIN customer_status ON customer_status.id = customer.status_id
                     LEFT JOIN (`order` INNER JOIN product ON product.id = `order`.product_id)
                               ON `order`.customer_id = customer.id
            ORDER BY customer.id
            """
        )
        return cursor.column_names, cursor.fetchall()


def transform(columns: list[str], rows: list):
    df = pd.DataFrame(columns=columns, data=rows)
    df["name"] = df.apply(lambda row: row["firstname"] + " " + row["surname"], axis=1)
    df["value"] = df.apply(lambda row: row["unit_price"] * row["quantity"] if pd.notna(row["quantity"]) else None,
                           axis=1)
    return df


def load(df):
    filename = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + ".csv"
    filepath = os.path.join(os.path.dirname(__file__), OUTPUT_DIRECTORY, filename)
    with open(filepath, "xb") as file:
        df.to_csv(file, index=False)
    print("Saved to", filepath)


def main():
    columns, rows = extract()
    df = transform(columns, rows)
    load(df)


if __name__ == "__main__":
    main()
