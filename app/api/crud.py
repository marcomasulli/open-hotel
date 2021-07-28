from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas

# Users

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Agents

def get_agent(db: Session, agent_id: int):
    return db.query(models.Agent).filter(models.Agent.id == agent_id).first()

def get_agent_by_name(db: Session, agent_name: int):
    return db.query(models.Agent).filter(models.Agent.agent_name == agent_name).first()

def get_agents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Agent).offset(skip).limit(limit).all()

def create_agent(db: Session, agent: schemas.AgentCreate):
    db_agent = models.Agent(**agent.dict())
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent


# Hotels

def get_hotel_by_name(db: Session, hotel_name: int):
    return db.query(models.Hotel).filter(models.Hotel.hotel_name == hotel_name).first()

def get_hotels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hotel).offset(skip).limit(limit).all()

def create_hotel(db: Session, hotel: schemas.HotelCreate):
    db_hotel = models.Hotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

# Rooms

def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()

def create_hotel_room(db: Session, room: schemas.RoomCreate, hotel_id: int):
    db_room = models.Room(**room.dict(), hotel_id=hotel_id)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

# Rates

def get_rateplans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RatePlan).offset(skip).limit(limit).all()

def get_hotel_rateplan(db: Session, hotel_id: int):
    return db.query(models.RatePlan).filter(models.RatePlan.hotel_id == hotel_id).all()

def get_room_rateplan(db: Session, room_id: int):
    return db.query(models.RatePlan).filter(models.RatePlan.room_id == room_id).all()

def create_rateplan(db: Session, rateplan: schemas.RatePlan, hotel_id: int, room_id: int):
    db_rateplan = models.RatePlan(**rateplan.dict(), hotel_id=hotel_id, room_id=room_id)
    db.add(db_rateplan)
    db.commit()
    db.refresh(db_rateplan)
    return db_rateplan

# Availability

def get_availability(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Availability).offset(skip).limit(limit).all()

def get_room_availability(db: Session, room_id: int):
    return db.query(
        models.Availability
        ).filter(
            models.Availability.room_id == room_id
        ).all()

def create_availability(db: Session, availability: schemas.Availability, hotel_id: int, room_id: int):
    db_availability = models.Availability(**availability.dict(), hotel_id=hotel_id, room_id=room_id)
    db.add(db_availability)
    db.commit()
    db.refresh(db_availability)
    return db_availability
