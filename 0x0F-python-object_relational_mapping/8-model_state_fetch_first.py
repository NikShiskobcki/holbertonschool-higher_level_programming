#!/usr/bin/python3
"""module"""
from sys import argv
from sqlalchemy.orm import Session
from model_state import Base, State

from sqlalchemy import create_engine



if __name__ == "__main__":
    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    session = Session(bind=engine)
    ans = session.query(State).order_by(State.id).first()
    if (ans is not None):
        print('{}: {}'.format(ans.id, ans.name))
    else:
        print("Nothing")
    session.close()
