# coding=utf-8

from sqlalchemy import Column, String, Integer, Date
from base import Base


class Feature(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    client = Column(String)
    client_priority = Column(String)
    target_date = Column(Date)
    product_area = Column(String)

    def __init__(self, title, description, client, client_priority, target_date, product_area):
        self.title = title
        self.description = description
        self.client = client
        self.client_priority = client_priority
        self.target_date = target_date
        self.product_area = product_area
