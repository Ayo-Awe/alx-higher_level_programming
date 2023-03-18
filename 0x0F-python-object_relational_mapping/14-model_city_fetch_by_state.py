#!/usr/bin/python3
"""This module contains code fetch cities
by their states
This script takes the following positional arguments
Args:
    1: <database user>
    2: <user password>
    3: <database>
"""
from model_state import State, Base
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    user, pwd, db = sys.argv[1:]
    engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}")
    engine.connect()
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    cities = session.query(State.name, City.id, City.name).join(
        City).order_by(City.id)

    for city in cities:
        print(f"{city[0]}: ({city[1]}) {city[2]}")

    session.close()
