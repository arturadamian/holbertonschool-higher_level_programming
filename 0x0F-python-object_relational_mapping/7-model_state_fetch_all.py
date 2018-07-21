#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
    pool_pre_ping=True)
Session = sessionmaker(bind=engine)

session = Session()

for state in session.query(
        State).order_by(State.id).all():  # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()