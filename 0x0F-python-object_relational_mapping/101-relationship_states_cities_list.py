#!/usr/bin/python3
"""This module contains code create a states and their
related cities using relationships
This script takes the following positional arguments
Args:
    1: <database user>
    2: <user password>
    3: <database>
"""
from relationship_state import State, Base
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

        states = session.query(State).order_by(State.id).all()

        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")

        session.close()
    except Exception as e:
        pass


if __name__ == "__main__":
    fetch_states_and_cities()
