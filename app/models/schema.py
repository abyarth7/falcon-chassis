from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from config.base import Base


class OrderCart(Base):
    __tablename__ = 'order_cart'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    order_detail = relationship("OrderDetails")
    phlebo_detail = relationship(
        "PhleboDetails", uselist=False, back_populates='order')
    pickup_address = relationship(
        "PickupAddress", uselist=False, back_populates="order")
    payment_detail = relationship(
        "PaymentDetails", uselist=False, back_populates="order")

    def __init__(self, patient_id):
        self.patient_id = patient_id


class OrderDetails(Base):
    __tablename__ = 'order_details'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order_cart.id'), nullable=False)
    order_type = Column(String)


class PhleboDetails(Base):
    __tablename__ = 'phlebo_details'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order_cart.id'), nullable=False)
    phlebo_id = Column(Integer, nullable=False)
    phlebo_name = Column(String)
    phlebo_phone = Column(String, nullable=False)
    order = relationship("OrderCart", back_populates='phlebo_detail')


class PickupAddress(Base):
    __tablename__ = 'pickup_address'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order_cart.id'), nullable=False)
    house_no = Column(String)
    street = Column(String)
    area = Column(String)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    pincode = Column(Integer, nullable=False)
    landmark = Column(String)
    lat_lng = Column(String)
    order = relationship("OrderCart", back_populates="pickup_address")


class PaymentDetails(Base):
    __tablename__ = 'payment_details'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order_cart.id'), nullable=False)
    order_net_price = Column(Integer, nullable=False)
    discount = Column(Integer)
    wallet_credits = Column(Integer)
    promo_applied = Column(Boolean, default=False)
    promo_code = Column(String)
    total_billed_amount = Column(Integer, nullable=False)
    balance_payable = Column(Integer, nullable=False)
    payment_id = Column(String)
    refund_id = Column(String)
    order = relationship("OrderCart", back_populates="payment_detail")
