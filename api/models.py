from sqlmodel import SQLModel, Field, Relationship


class Product(SQLModel, table=True):
    id: int|None = Field(primary_key=True)
    name: str
    unit_price: int


class Order(SQLModel, table=True):
    id: int|None = Field(primary_key=True)
    customer_id: int|None = Field(foreign_key="customer.id")
    customer: Customer = Relationship(back_populates="orders")
    product_id: int
    # product: Product
    quantity: int
    # timestamp: TIMESTAMP # TODO


class CustomerStatus(SQLModel, table=True):
    id: int|None = Field(primary_key=True)
    status: str


class CustomerBase(SQLModel):
    email: str = Field(index=True, unique=True)
    surname: str
    firstname: str
    status_id: int = Field(foreign_key="customer_status.id")
    # status: CustomerStatus = Relationship(back_populates="customer")


class Customer(CustomerBase, table=True):
    id: int|None = Field(primary_key=True)
    orders: list[Order] = Relationship(back_populates="customer")


class CustomerResponse(CustomerBase):
    id: int
    # status: CustomerStatus
    orders: list[Order] = []
