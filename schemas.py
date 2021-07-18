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

# Hotels

class HotelBase(BaseModel):
    hotel_name: str
    hotel_address: str
    hotel_country: str
    hotel_province: str
    hotel_location: str
    hotel_rooms: Optional[str] = None
    hotel_latitude: str
    hotel_longitude: str
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