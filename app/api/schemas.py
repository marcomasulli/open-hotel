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
    hotel_rooms: Optional[int] = None
    hotel_latitude: Optional[str] = None
    hotel_longitude: Optional[str] = None
    hotel_phone: str
    hotel_email: str
    hotel_contact_person: Optional[str] = None
    hotel_contact_phone: Optional[str] = None
    hotel_contact_email: Optional[str] = None
    hotel_code: Optional[str] = None
    hotel_chain_code: Optional[str] = None
    hotel_brand_code: Optional[str] = None
    hotel_city_code: Optional[str] = None


class HotelCreate(HotelBase):
    pass


class Hotel(HotelBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True

# HotelInfo

class HotelInfoBase(BaseModel):
    currency_code: Optional[str] = None
    currency_code_decimal_places: Optional[int] = None
    hotel_pms_system: Optional[str] = None
    location_category: Optional[str] = None
    segment_category: Optional[str] = None
    hotel_category: Optional[str] = None
    architectural_style: Optional[str] = None

class HotelInfoCreate(HotelInfoBase):
    pass

class HotelInfo(HotelInfoBase):
    id: int
    hotel_id: int

    class Config:
        orm_mode = True


# HotelServiceAmenity
class HotelAmenityBase(BaseModel):
    description: Optional[str]

class HotelAmenityCreate(HotelAmenityBase):
    pass

class HotelAmenity(HotelAmenityBase):
    id: int
    hotel_id: int

    class Config:
        orm_mode = True

# HotelServiceFacility
class HotelFacilityBase(BaseModel):
    description: Optional[str]
    
class HotelFacilityCreate(HotelFacilityBase):
    pass

class HotelFacility(HotelFacilityBase):
    id: int
    hotel_id: int

    class Config:
        orm_mode = True


# Hotel Meeting Rooms
class HotelMeetingRoomBase(BaseModel):
    service_name: str
    room_name: str
    room_capacity: int
    room_access: Optional[str] = None
    room_level: Optional[str] = None
    room_proximity: Optional[str] = None
    room_type: Optional[str] = None
    room_measure_unit: Optional[str] = None
    room_width: Optional[int] = None
    room_height: Optional[int] = None
    room_area: Optional[int] = None
    room_length: Optional[int] = None

class HotelMeetingRoomCreate(HotelMeetingRoomBase):
    pass

class HotelMeetingRoom(HotelMeetingRoomBase):
    id: int
    hotel_id: int

    class Config:
        orm_mode = True

# Hotel Cancellation Policies
class HotelCancelPolicyBase(BaseModel):
    date_start: datetime 
    date_end: datetime 
    weekdays: str 
    penalty_basis: str 
    penalty_deadline_type: str 
    penalty_deadline_value: int 
    penalty_amount_type: str 
    penalty_amount_value: int 


class HotelCancelPolicyCreate(HotelCancelPolicyBase):
    pass

class HotelCancelPolicy(HotelCancelPolicyBase):
    id: int
    hotel_id: int

    class Config:
        orm_mode = True

# Hotel GDS Info

class HotelGDSInfoBase(BaseModel):
    master_chain_code: str
    gds_property_code: str
    gds_name: str
    chain_code: str
    gds_status_value: str

class HotelGDSInfoCreate(HotelGDSInfoBase):
    pass

class HotelGDSInfo(HotelGDSInfoBase):
    id: int
    hotel_id: int

    class Config:
        orm_mode = True

# Rooms

class RoomBase(BaseModel):
    room_name: str
    room_quantity: int = None
    room_description: Optional[str] = None
    room_min_occupancy: int = None
    room_max_occupancy: int = None
    room_min_adults: int = None
    room_max_adults: int = None
    room_max_children: int = None
    room_max_infants: int = None
    standard_bed_quantity: Optional[int] = None
    max_rollaways: Optional[int] = None
    room_size: Optional[float] = None
    room_count: Optional[int] = None
    room_type_code: Optional[str] = None
    gds_room_type_code: Optional[str] = None
    floor: Optional[int] = None
    inventory_block_code: Optional[str] = None
    room_configuration: Optional[str] = None
    size_measurement: Optional[str] = None
    room_gender: Optional[str] = None
    max_cribs: Optional[int] = None
    non_smoking: Optional[bool] = True
    composite_ind: Optional[bool] = True
    share_room_ind: Optional[bool] = True
    room_category: Optional[str] = None
    room_location_code: Optional[str] = None
    room_view: Optional[str] = None
    bed_type: Optional[str] = None
    min_rate: Optional[float] = None
    max_rate: Optional[float] = None
    fixed_rate: Optional[float] = None
    rate_time_unit: Optional[str] = None


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    id: int
    hotel_id: int
    is_active: bool

    class Config:
        orm_mode = True

class RoomAmenityBase(BaseModel):
    amenity_name: str
    amenity_code: str
    amenity_description: str
    amenity_quantity: int = 0
    included_in_rate: bool = True
class RoomAmenityCreate(RoomAmenityBase):
    pass

class RoomAmenity(RoomAmenityBase):
    id: int
    hotel_id: int
    
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
    is_active: bool

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