from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    agent_name  = Column(String, index=True)
    agent_address = Column(String)
    agent_country = Column(String)
    agent_province = Column(String)
    agent_location = Column(String)
    agent_phone = Column(String)
    agent_email = Column(String)
    agent_contact_person = Column(String)
    is_active = Column(Boolean, default=True)
    agent_type = Column(String)
    agent_model = Column(String)
    agent_commission = Column(Float)
    agent_discount = Column(Float)

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    hotel_name = Column(String, index=True)
    hotel_address = Column(String)
    hotel_country = Column(String)
    hotel_province = Column(String)
    hotel_location = Column(String)
    hotel_rooms = Column(Integer)
    hotel_latitude = Column(Float)
    hotel_longitude = Column(Float)
    hotel_phone = Column(String)
    hotel_email = Column(String)
    hotel_contact_person = Column(String)
    hotel_contact_phone = Column(String)
    hotel_contact_email = Column(String)
    is_active = Column(Boolean, default=True)

    rooms = relationship('Room', back_populates='hotel')

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
    is_active = Column(Boolean, default=True)

    hotel = relationship('Hotel', back_populates='rooms')
    rateplans = relationship('RatePlan', back_populates='room')
    availability = relationship('Availability', back_populates='room')
class RatePlan(Base):
    __tablename__ = "rateplans"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), index=True)
    valid_from = Column(DateTime)
    valid_to = Column(DateTime)
    rate = Column(Float)
    is_active = Column(Boolean, default=True)
    
    room = relationship('Room', back_populates='rateplans')

class Availability(Base):
    __tablename__ = "availability"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), index=True)
    valid_from = Column(DateTime)
    valid_to = Column(DateTime)
    total_rooms = Column(Integer)
    remaining_rooms = Column(Integer)
    is_open = Column(Boolean, default=False)

    room = relationship('Room', back_populates='availability')