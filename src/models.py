import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base

from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email= Column(String(20), nullable=False)
    tel = Column(String(10), nullable=False)
    


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_planet = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable= False)
    planet_gravity = Column(Integer, nullable= False)
    planet_climate = Column(Integer, nullable=False)
    planet_population = Column(Integer, nullable=False)
    planet_terrain = Column(String(250), nullable= False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Starship(Base):
    __tablename__ = 'starship'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_starship = Column(Integer, primary_key=True)
    starship_name = Column(String(250), nullable= False)
    starship_model = Column(String(250), nullable= False)
    starship_length = Column(Integer, nullable=False)
    starship_CostInCredit = Column(Integer, nullable=False)
    starship_manufacturer = Column(String(250), nullable= False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
