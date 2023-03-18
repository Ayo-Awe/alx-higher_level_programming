#!/usr/bin/python3
"""This module contains code fetch cities and their
associated states
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


def fetch_states_and_cities():
    try:
        user, pwd, db = sys.argv[1:]
        engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}")
        engine.connect()
        Base.metadata.create_all(engine)
        session = Session(bind=engine)

        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")

        session.close()
    except Exception as e:
        pass


if __name__ == "__main__":
    fetch_states_and_cities()
