#!/usr/bin/python3
"""This module contains code create a city
with a states
This script takes the following positional arguments
Args:
    1: <database user>
    2: <user password>
    3: <database>
"""
from relationship_state import State, Base
from relationship_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def create_city_with_state():
    try:
        user, pwd, db = sys.argv[1:]
        engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}")
        engine.connect()
        Base.metadata.create_all(engine)
        session = Session(bind=engine)

        state = State(name="California")
        city = City(name="San Francisco")
        state.cities = [city]

        session.add(state)
        session.commit()
        session.close()
    except Exception as e:
        pass


if __name__ == "__main__":
    create_city_with_state()
