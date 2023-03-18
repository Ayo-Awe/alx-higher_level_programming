#!/usr/bin/python3
"""This module contains a class definition for
a city model in the database"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """State is an object representation of
    a state entity in a mysql database
    """
    __tablename__ = "cities"
    id = Column(Integer,  primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
