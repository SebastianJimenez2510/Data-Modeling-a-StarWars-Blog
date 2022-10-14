import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    terrain = Column(String(50), nullable=True)
    population = Column(String(50), nullable=True)
    url_imagen = Column(String(200),nullable=True)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    user = Column(String(50), nullable=True)
    email = Column(String(200), nullable=True, unique=True)
    password = Column(String(50), nullable=True)
    
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    birth_year = Column(String(50), nullable=True)
    gender = Column(String(50), nullable=True)
    height = Column(String(50), nullable=True)
    skin_color = Column(String(50), nullable=True)
    eye_color = Column(String(50), nullable=True)
    url_imagen = Column(String(200),nullable=True)

class User_Favorite_PLanets(Base):
    __tablename__ = 'user_favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(String(50), ForeignKey('planets.id'))

class Favorite_Characters(Base):
    __tablename__ = 'Favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(String(50), ForeignKey('characters.id'))
    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')