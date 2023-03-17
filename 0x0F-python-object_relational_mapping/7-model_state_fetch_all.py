#!/usr/bin/python3
"""This module contains code to fetch states from a
database using an ORM"""
from model_state import State, Base
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    user, pwd, db = sys.argv[1:]
    engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}")
    engine.connect()
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
