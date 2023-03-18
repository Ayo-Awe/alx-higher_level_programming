#!/usr/bin/python3
"""This module contains code to update the state
where id=2
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

    state = session.get(State, 2)

    if state:
        state.name = "New Mexico"
        session.add(state)
        session.commit()

    session.close()
