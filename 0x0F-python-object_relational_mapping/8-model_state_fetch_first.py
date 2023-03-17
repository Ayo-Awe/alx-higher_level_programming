#!/usr/bin/python3
"""This module contains code to fetch first state in
states table from a database using an ORM.
This script takes the following positional arguments
Args:
    1: <database user>
    2: <user password>
    3: <database>
"""
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

    first = session.query(State).first()
    if first:
        print(f"{first.id}: {first.name}")
    else:
        print("Nothing")

    session.close()
