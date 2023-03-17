#!/usr/bin/python3
"""This module contains a class definition for
a state model in the database"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State is an object representation of
    a state entity in a mysql database
    """
    __tablename__ = "states"
    id = Column(Integer,  primary_key=True)
    name = Column(String(128), nullable=False)
