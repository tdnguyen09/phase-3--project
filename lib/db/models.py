#!/usr/bin/env python3
import os
import sys

sys.path.append(os.getcwd())


from datetime import datetime

from sqlalchemy import create_engine, desc
from sqlalchemy import (CheckConstraint, UniqueConstraint, Column, DateTime, Integer, String)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///albums.db')

Base = declarative_base()

class Album(Base):
    __tablename__='albums'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    artist = Column(String())
    release_date = Column(DateTime())

    def __repr__(self):
        return f"Album {self.id}:" \
            + f"{self.name}," \
            + f"Artist: {self.artist}," \
            + f"{self.release_date}" 


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
