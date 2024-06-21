#!/usr/bin/env python3
import os
import sys

sys.path.append(os.getcwd())


from datetime import datetime

from sqlalchemy import create_engine, desc
from sqlalchemy import (CheckConstraint, UniqueConstraint, Column, DateTime, Integer, String, ForeignKey)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('sqlite:///albums.db')

Base = declarative_base()

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

class Artist (Base):
    __tablename__="artists"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    albums = relationship('Album', backref='artist')

    def __repr__(self):
        return f'Artist {self.id}:' \
            + f'{self.name}' \
             


class Album(Base):
    __tablename__='albums'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    artist_name = Column(String())
    release_date = Column(DateTime())

    artist_id = Column(Integer(), ForeignKey('artists.id'))

    def __repr__(self):
        return f"Album {self.id}:" \
            + f"{self.name}, " \
            + f"Artist: {self.artist_name}, " \
            + f"{self.release_date}, "  \
            + f"Artist id: {self.artist_id}"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
