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
    hotel_code = Column(String)
    hotel_chain_code = Column(String)
    hotel_brand_code = Column(String)
    hotel_city_code = Column(String)
    is_active = Column(Boolean, default=True)

    rooms = relationship('Room', back_populates='hotel')
    hotel_info = relationship('HotelInfo', back_populates='hotel')


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    room_name = Column(String, index=True)
    room_quantity = Column(Integer)
    room_description = Column (String)
    room_min_occupancy = Column(Integer)
    room_max_occupancy = Column(Integer)
    room_min_adults = Column(Integer)
    room_max_adults = Column(Integer)
    room_max_children = Column(Integer)
    room_max_infants = Column(Integer)
    min_rate = Column(Float)
    max_rate = Column(Float)
    fixed_rate = Column(Float)
    rate_time_unit =  Column(String)
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

class HotelInfo(Base):
    __tablename__ = "hotel_info"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), index=True)
    currency_code = Column(String, index=True)
    currency_code_decimal_places = Column(Integer)
    hotel_pms_system = Column(String)
    location_category = Column(String)
    segment_category = Column(String)
    hotel_category = Column(String)
    architectural_style = Column(String)
    
    hotel = relationship('Hotels', back_populates='hotel_info')

class HotelServiceAmenitY(Base):
    __tablename__ = "hotel_AMENITY"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), index=True)

class HotelServiceFacility(Base):
    __tablename__ = "hotel_facility"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), index=True)

class HotelServiceMeetingRoom(Base):
    __tablename__ = "hotel_meeting_room"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), index=True)
    service_name = Column(String)
    room_name = Column(String)
    room_capacity = Column(Integer)
    room_access = Column(String)
    room_level = Column(String)
    room_proximity = Column(String)
    room_type = Column(String)
    room_measure_unit = Column(String)
    room_width = Column(Integer)
    room_height = Column(Integer)
    room_area = Column(Integer)
    room_length = Column(Integer)
