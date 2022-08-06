#!/usr/bin/python3
"""module"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

from sqlalchemy import create_engine

USER = argv[1]
PASS = argv[2]
DB = argv[3]

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(USER, PASS, DB))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ans =  session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for row in ans:
        print(f"{row.id}: {row.name}")
    session.close()
