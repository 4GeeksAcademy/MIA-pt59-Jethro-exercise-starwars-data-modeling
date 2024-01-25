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
    
class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    favorite_id = Column(Integer, primary_key=True)
    id_planet = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet")
    id_characters = Column(Integer, ForeignKey('characters.id'))
    characters = relationship("Characters")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    id_starship = Column(Integer, ForeignKey('starship.id'))
    starship = relationship("Starship")
    

    


    user = relationship(User)
    
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
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)


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
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)




class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_characters = Column(Integer, primary_key=True)
    characters_name = Column(String(250), nullable= False)
    characters_height = Column(Integer, nullable= False)
    characters_hair_color = Column(String(20), nullable=False)
    characters_eye = Column(String(20), nullable=False)
    characters_birth_Year = Column(String(30), nullable= False)    
    id_starship= Column(Integer, ForeignKey('starship.id'))
    id_planet= Column(Integer, ForeignKey('planet.id'))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
