from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    hotel_name = Column(String, index=True)
    hotel_address = Column(String, index=True)
    hotel_country = Column(String, index=True)
    hotel_province = Column(String, index=True)
    hotel_location = Column(String, index=True)
    hotel_rooms = Column(Integer)
    hotel_latitude = Column(Float)
    hotel_longitude = Column(Float)
    hotel_phone = Column(String)
    hotel_email = Column(String)
    hotel_contact_person = Column(String)
    hotel_contact_phone = Column(String)
    hotel_contact_email = Column(String)
    hotel_is_active = Column(Boolean, default=True)

    rooms = relationship("Room", back_populates="hotel")

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    room_name = Column(String, index=True)
    room_description = Column (String)
    room_min_occupancy = Column(Integer)
    room_max_occupancy = Column(Integer)
    room_min_adults = Column(Integer)
    room_max_adults = Column(Integer)
    room_max_children = Column(Integer)
    room_max_infants = Column(Integer)
    room_is_active = Column(Boolean, default=True)

    hotel = relationship("Hotel", back_populates="rooms")