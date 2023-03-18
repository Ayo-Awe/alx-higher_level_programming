#!/usr/bin/python3
"""This module contains code to fetch the state whose name
matches the query string  using an ORM.
This script takes the following positional arguments
Args:
    1: <database user>
    2: <user password>
    3: <database>
    4: <search string>
"""
from model_state import State, Base
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    user, pwd, db, search_string = sys.argv[1:]
    engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}")
    engine.connect()
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    match = session.query(State).filter(
        State.name == search_string).one_or_none()

    if match:
        print(match.id)
    else:
        print("Not found")

    session.close()
