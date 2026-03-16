# UoS-Assessment
## Usage
### Requirements
* Python 3 (developed with 3.14)
  * Required packages in `requirements.txt` for pip installation.
* MySQL Server (developed with 8.4.8)
  * Requires account with privileges to create schema and tables and to CRUD data.

### Configuration
Can be configured with environment variables or .env in the project root. This is used for MySQL connection parameters. 

### Running
This will require the [virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work) or equivalent to be active.

To run the database setup (create tables and mock data), execute `$ python database setup.py`.

To run the ETL script, execute `$python etl script.py`.

To run the FastAPI instance, run `$ fastapi run` from the command line. See [FastAPI CLI documentation](https://fastapi.tiangolo.com/fastapi-cli/) for more details. The API is self documenting; documentation can be found at <http://127.0.0.1:8000/docs>

## Choices and reasoning
### Database
I chose to use MySQL as it is a popular free RDBMS that I have much experience using and widely supported for integrations.

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
I decided to use the pandas library as I have experience using it for ETL and found it useful.

### API
I decided to use the FastAPI library as I have some exposure of it in a production environment and it simplifies creation of a functional API, including by providing HTTP, serialisation etc. This proved to be more complicated than anticipated; if I was doing this again I would investigate other options more thoroughly.

## Application data flow
1. The database setup script inserts data. 
2. The API retrieves data and serialises it into JSON for HTTP responses to requests.
3. The ETL script takes the data and transforms it before encoding it and saving it as CSV.


## Improvements
My ETL script loads all records from the database into memory. If there were much larger number of records, this could be a problem and I instead iterate through the records or work in chunks instead of performing three distinct steps on the whole dataset. For these simple transformations, I would also consider doing them in the SQL query itself.

With more time, I would like to expand the API to allow creating, updating and deleting records. I would also include options for searching and pagination. Finally, I would implement some kind of authentication.

Finally, I would create a test suite for each part including unit tests and HTTP requests to the API.