#!/usr/bin/python3
"""adds state"""
from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    session = Session(bind=engine)
    session.execute(
            update(State).
            where(State.id == 2)
            values(name="New Mexico"))
    session.commit()
