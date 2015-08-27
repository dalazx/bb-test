#!/usr/bin/env python

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql://root@localhost/bb_test', echo=True)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'dedsert_test'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    age = Column(Integer)
    role = Column(String(64))
