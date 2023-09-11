#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy_sandbox import Base, Student

# Create the SQLite database and tables
engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
