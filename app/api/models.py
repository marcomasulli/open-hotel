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
    agent_type = Column(String)
    agent_model = Column(String)
    agent_commission = Column(Float)
    agent_discount = Column(Float)
    is_active = Column(Boolean, default=True)

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    hotel_name = Column(String, index=True)
    hotel_address = Column(String)
    hotel_country = Column(String)
    hotel_province = Column(String)
    hotel_location = Column(String)
    hotel_rooms = Column(Integer)
    hotel_latitude = Column(String)
    hotel_longitude = Column(String)
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
    hotel_meeting_rooms = relationship('HotelServiceMeetingRoom', back_populates='hotel')
    hotel_cancel_policies = relationship('HotelCancelPolicy', back_populates='hotel')
    hotel_gds_info = relationship('HotelGDSInfo', back_populates='hotel')
    hotel_amenity = relationship('HotelServiceAmenity', back_populates='hotel')
    hotel_facility = relationship('HotelServiceFacility', back_populates='hotel')

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
    
    hotel = relationship('Hotel', back_populates='hotel_info')

class HotelServiceAmenity(Base):
    __tablename__ = "hotel_amenities"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), index=True)
    description = Column(String)

    hotel = relationship('Hotel', back_populates='hotel_amenity')

class HotelServiceFacility(Base):
    __tablename__ = "hotel_facilities"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), index=True)
    description = Column(String)

    hotel = relationship('Hotel', back_populates='hotel_facility')

class HotelServiceMeetingRoom(Base):
    __tablename__ = "hotel_meeting_rooms"

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

    hotel = relationship('Hotel', back_populates='hotel_meeting_rooms')

class HotelCancelPolicy(Base):
    __tablename__ = "hotel_cancel_policies"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), index=True)
    # guaranteed_room_via_gds = Column(Boolean, default=True)
    # guaranteed_room_via_crc = Column(Boolean, default=True)
    # guaranteed_room_via_property = Column(Boolean, default=True)
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    weekdays = Column(String)
    penalty_basis = Column(String, default='Hours')
    penalty_deadline_type = Column(String, default='BeforeArrival')
    penalty_deadline_value = Column(Integer, default=24)
    penalty_amount_type = Column(String, default='Percent')
    penalty_amount_value = Column(Integer, default=100)

    hotel = relationship('Hotel', back_populates='hotel_cancel_policies')

class HotelGDSInfo(Base):
    __tablename__ = "hotel_gds_info"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), index=True)
    master_chain_code = Column(String)
    gds_property_code = Column(String)
    gds_name = Column(String)
    chain_code = Column(String)
    gds_status_value = Column(String, default='Closed')

    hotel = relationship('Hotel', back_populates='hotel_gds_info')

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    room_name = Column(String, index=True)
    room_quantity = Column(Integer)
    room_description = Column(String)
    room_min_occupancy = Column(Integer)
    room_max_occupancy = Column(Integer)
    room_min_adults = Column(Integer)
    room_max_adults = Column(Integer)
    room_max_children = Column(Integer)
    room_max_infants = Column(Integer)
    standard_bed_quantity = Column(Integer)
    max_rollaways = Column(Integer)
    room_size = Column(Float)
    room_count = Column(Integer)
    room_type_code = Column(String)
    gds_room_type_code = Column(String)
    floor = Column(Integer)
    inventory_block_code = Column(String)
    room_configuration = Column(String)
    size_measurement = Column(String)
    room_quantity = Column(Integer)
    room_gender = Column(String)
    max_cribs = Column(Integer)
    non_smoking = Column(Boolean, default=True)
    composite_ind = Column(Boolean)
    share_room_ind = Column(Boolean)
    room_category = Column(String)
    room_location_code = Column(String)
    room_view = Column(String)
    bed_type = Column(String)
    min_rate = Column(Float)
    max_rate = Column(Float)
    fixed_rate = Column(Float)
    rate_time_unit = Column(String)
    is_active = Column(Boolean, default=True)

    hotel = relationship('Hotel', back_populates='rooms')
    rateplans = relationship('RatePlan', back_populates='room')
    availability = relationship('Availability', back_populates='room')
    room_amenity = relationship('RoomAmenity', back_populates='room')

class RoomAmenity(Base):
    __tablename__ = "room_amenities"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), index=True)
    amenity_name = Column(String)
    amenity_code = Column(String)
    amenity_description = Column(String)
    amenity_quantity = Column(Float)
    included_in_rate = Column(Boolean, default=True)

    room = relationship('Room', back_populates='room_amenity')
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

    