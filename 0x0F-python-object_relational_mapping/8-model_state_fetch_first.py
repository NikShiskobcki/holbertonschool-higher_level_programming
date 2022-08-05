#!/usr/bin/python3

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
    ans = session.query(State).order_by(State.id).first()
    if (ans is not None):
        print('{}: {}'.format(ans.id, ans.name))
    else:
        print("Nothing")
    session.close()
