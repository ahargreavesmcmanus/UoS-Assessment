# UoS-Assessment
## Usage
### Requirements
* Python 3 (developed with 3.14)
  * Required packages in `requirements.txt`
* MySQL Server (developed with 8.4.8)
  * Requires account with privileges to create schema and tables and to CRUD data.

### Configuration
Can be configured with environment variables or .env in the project root.

### Running
To run the database setup (create tables and mock data), execute `database setup.py`.

To run the ETL script, execute `etl script.py`.

<!-- TODO -->

## Choices and reasoning
### Database
I chose to use MySQL as it is a free RDBMS that I have much experience using.

In a production situation, I would use different users with more limited privileges for creating the schema and for the day-to-day CRUD tasks.
Here, for simplicity, I have used an account ('root') with all privileges needed for altering the schema and inserting and reading data.

#### Schema decisions
I decided to include email addresses in the customer table and make them unique as email addresses are often used to identify users during authentication. Of course, they also allow communication about orders.

For better normalisation, I decided to create a product table to be referenced by the order table.

Currency amounts are stored in pence to ensure no precision issues from using decimals.

For unique identifiers, I used integers with auto increment. This is simple and efficient. However, if records were being created by distributed systems or if there were security concerns about sequential identifiers, UUID could be used instead.

#### Record creation
I decided to use the Faker library as I have used a similar library before and it creates realistic data randomly.

### ETL
I decided to use the pandas library as I have experience using it for ETL and it is effective for such operations.


## Application flow
<!-- TODO -->


## Improvements
<!-- TODO -->

My ETL script loads all records from the database into memory. If there were much larger number of records, this could be a problem and I instead iterate through the records or work in chunks instead of performing three distinct steps on the whole dataset. For these simple transformations, I would also consider doing them in the SQL query itself.