from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

# Users

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True
# Agents

class AgentBase(BaseModel):
    agent_name: str
    agent_address: str
    agent_country: str
    agent_province: str
    agent_location: str
    agent_phone: str
    agent_email: str
    agent_contact_person: str
    agent_type: str
    agent_model: str
    agent_commission: float
    agent_discount: float

class AgentCreate(AgentBase):
    pass


class Agent(AgentBase):
    id: int
    agent_is_active: bool
    
    class Config:
        orm_mode = True


# Hotels

class HotelBase(BaseModel):
    hotel_name: str
    hotel_address: str
    hotel_country: str
    hotel_province: str
    hotel_location: str
    hotel_rooms: Optional[str] = None
    hotel_latitude: Optional[str] = None
    hotel_longitude: Optional[str] = None
    hotel_phone: str
    hotel_email: str
    hotel_contact_person: Optional[str] = None
    hotel_contact_phone: Optional[str] = None
    hotel_contact_email: Optional[str] = None


class HotelCreate(HotelBase):
    pass


class Hotel(HotelBase):
    id: int
    hotel_is_active: bool
    
    class Config:
        orm_mode = True

# Rooms

class RoomBase(BaseModel):
    room_name: str
    room_description: Optional[str]
    room_min_occupancy: int
    room_max_occupancy: int
    room_min_adults: int
    room_max_adults: int
    room_max_children: int
    room_max_infants: int


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    id: int
    hotel_id: int
    room_is_active: bool

    class Config:
        orm_mode = True

# Rates

class RatePlanBase(BaseModel):
    valid_from: datetime
    valid_to: datetime
    rate: float

class RatePlanCreate(RatePlanBase):
    pass

class RatePlan(RatePlanBase):
    id: int
    hotel_id: int
    room_id: int
    rate_is_active: bool

    class Config:
        orm_mode = True

# Availability

class AvailabilityBase(BaseModel):
    hotel_id: int
    room_id: int
    valid_from: str
    valid_to: str
    total_rooms: int
    remaining_rooms: int
    is_open: Optional[bool] = False

class AvailabilityCreate(AvailabilityBase):
    pass

class Availability(AvailabilityBase):
    id: int

    class Config:
        orm_mode = True