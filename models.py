"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from database import Base

# TODO: Complete your models


class Voter(Base):
    __tablename__ = "voters"

    # Columns
    username = Column("username", TEXT, primary_key=True)
    password = Column("password", TEXT, nullable=False)
    # grade = Column("grade", INTEGER, nullable=False)


class Food(Base):
    __tablename__ = "foods"

    # Column
    name = Column("name", TEXT, primary_key=True)
    genre = Column("genre", TEXT, nullable=False)

    votes = relationship("Vote")

    def __repr__(self):
        return self.name + ": " + str(len(self.votes)) + " votes"


class Vote(Base):
    __tablename__ = "votes"

    # Columns
    id = Column("id", INTEGER, primary_key=True)
    voter_id = Column("voter_id", TEXT, ForeignKey('voters.username'))
    food_name = Column("food_name", TEXT, ForeignKey('foods.name'))
