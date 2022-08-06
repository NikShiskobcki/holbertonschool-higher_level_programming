#!/usr/bin/python3
"""fetchall module"""
from sys import argv
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine, MetaData


if __name__ == "__main__":
    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    session = Session(bind=engine)
    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
    session.close()
