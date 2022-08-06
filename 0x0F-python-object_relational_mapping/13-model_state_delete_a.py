#!/usr/bin/python3
"""deletes state"""
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    engine.execute(delete(State).where(State.name.like('%a%')))
