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
    ans = session.query(
            State).filter(State.name.like('%a%')).order_by(State.id)
    for row in ans:
        print(f"{row.id}: {row.name}")
    session.close()
