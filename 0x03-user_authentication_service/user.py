#!/usr/bin/env python3
'''Base module for sql'''
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
import logging

logging.getLogger('sqlalchemy').setLevel(logging.WARNING)
Base = declarative_base()


class User(Base):
    '''User table class for mapping
    '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
