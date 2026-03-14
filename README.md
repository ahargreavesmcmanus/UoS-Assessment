# UoS-Assessment
## Usage
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

For customer status, for simplicity, I decided to use an ENUM column. However, in a more complicated situation I would usually choose to use a reference table.


## Application flow
<!-- TODO -->


## Improvements
<!-- TODO -->