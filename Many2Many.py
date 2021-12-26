from sqlalchemy import Table, Column, BigInteger,Integer, String, DateTime, REAL, Date, ForeignKey, UniqueConstraint
from db_config import Base
from sqlalchemy.orm import relationship, backref

association_table = Table('orders_products', Base.metadata,
                          Column('order_id', ForeignKey('orders.id'), primary_key = True),
                          Column('product_id', ForeignKey('products.id'), primary_key = True)
                          )

class MixOrdersProducts(Base):
    __tablename__ = 'mix_orders_products'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    order = relationship("Order", backref=backref("mix_orders_products", uselist=True))
    product = relationship("Product", backref=backref("mix_orders_products", uselist=True))

    def __str__(self):
        return f'<MixOrdersProducts> id:{self.id} order_id:{self.order_id} product_id:{self.product_id} quantity:{self.quantity}\n'

    def __repr__(self):
        return f'<MixOrdersProducts> id:{self.id} order_id:{self.order_id} product_id:{self.product_id} quantity:{self.quantity}\n'

class Order(Base):
    __tablename__ = 'orders'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(50), nullable=True)

    def __str__(self):
        return f'<orders> id:{self.id} name:{self.name}'

    def __repr__(self):
        return f'<orders> id:{self.id} name:{self.name}'

class Product(Base):
    __tablename__ = 'products'
    id = Column(BigInteger, primary_key=True)
    product = Column(String(50), nullable=False)
    price = Column(REAL, nullable=False)

    def __str__(self):
        return f'<products> id:{self.id} product:{self.product} price:{self.price}'

    def __repr__(self):
        return f'<products> id:{self.id} product:{self.product} price:{self.price}'
