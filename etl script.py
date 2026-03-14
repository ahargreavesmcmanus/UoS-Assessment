# ETL script
import db

def main():
    with db.cnx() as cnx:
        cnx.database = db.SCHEMA
        cursor = cnx.cursor()
        cursor.execute(
        """
        SELECT customer.id, email, surname, firstname, status, `order`.id AS order_id, product.name, product.unit_price, `order`.quantity, `order`.timestamp
        FROM customer
            LEFT JOIN (`order` INNER JOIN product ON  product.id = `order`.product)
                  ON `order`.customer = customer.id
        ORDER BY customer.id
        """
        )
        extract = cursor.fetchall()




if __name__ == "__main__":
    main()
