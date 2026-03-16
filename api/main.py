from fastapi import FastAPI, Depends, HTTPException

from sqlmodel import Session, create_engine, select, col

from sqlalchemy.engine import URL

from typing import Annotated

import db
from api.models import Product, Order, Customer, CustomerResponse

url_object = URL.create(
    "mysql",
    username=db.get_user(),
    password=db.get_password(),
    host=db.get_host(),
    database=db.SCHEMA,
)
engine = create_engine(url_object)
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/customer/{customer_id}")
def read_customer(
        session: SessionDep,
        customer_id: int,
    ) -> CustomerResponse:
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.get("/orders/{customer_id}")
def read_customer(
        session: SessionDep,
        customer_id: int,
    ) -> list[Order]:
    orders = session.exec(select(Order).where(col(Order.customer_id) == customer_id))
    return orders

@app.get("/order/{order_id}")
def read_order(
        session: SessionDep,
        order_id: int,
    ) -> Order:
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/product/{product_id}")
def read_product(
        session: SessionDep,
        product_id: int,
    ) -> Product:
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

