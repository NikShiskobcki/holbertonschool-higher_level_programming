#!/usr/bin/python3
"""city module"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
