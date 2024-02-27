#!/usr/bin/python3
<<<<<<< HEAD
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if self.password:
            hashed_password = hashlib.md5(self.password.encode("utf-8"))
            self.password = hashed_password.hexdigest()
=======
'''
    Implementation of the User class which inherits from BaseModel
    '''
    from os import getenv
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship
    from models.base_model import BaseModel, Base


    class User(BaseModel, Base):
            '''
                    Definition of the User class
                        '''
                            __tablename__ = "users"
                                if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
                                            email = Column(String(128), nullable=False)
                                                    password = Column(String(128), nullable=False)
                                                            first_name = Column(String(128), nullable=True)
                                                                    last_name = Column(String(128), nullable=True)
                                                                            places = relationship("Place", backref="user",
                                                                                                                  cascade="all, delete, delete-orphan")
                                                                                    reviews = relationship("Review", backref="user",
                                                                                                                           cascade="all, delete, delete-orphan")
                                                                                        else:
                                                                                                    email = ""
                                                                                                            password = ""
                                                                                                                    first_name = ""
                                                                                                                            last_name = ""
>>>>>>> 6e7511263a25b22fb7180a2a53d1daa63c24a997
