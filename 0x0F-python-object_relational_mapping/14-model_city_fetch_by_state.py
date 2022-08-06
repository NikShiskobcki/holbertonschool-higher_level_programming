#!/usr/bin/python3
"""update state module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    session = Session(bind=engine)
    for stat, cit in session.query(State, City).filter(
            State.id == City.state_id):
        print("{}: ({}) {}".format(stat.name, cit.id, cit.name))
