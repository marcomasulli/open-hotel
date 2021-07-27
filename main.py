from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# users

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# agents

@app.post("/agents/", response_model=schemas.Agent)
def create_agent(agent: schemas.AgentCreate, db: Session = Depends(get_db)
):
    db_agent = crud.get_agent_by_name(db, agent_name=agent.agent_name)
    if db_agent:
        raise HTTPException(status_code=400, detail="Agent already exists")
    return crud.create_agent(db=db, agent=agent)


@app.get("/agents/", response_model=List[schemas.Agent])
def read_agents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    agents = crud.get_agents(db, skip=skip, limit=limit)
    return agents

@app.get("/agents/{agent_id}")
def read_agent(agent_id: int, db: Session = Depends(get_db)):
    db_agent = crud.get_agent(db, agent_id=agent_id)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_agent

# hotels

@app.post("/hotels/", response_model=schemas.Hotel)
def create_hotel(
    hotel: schemas.HotelCreate, db: Session = Depends(get_db)
):
    db_hotel = crud.get_hotel_by_name(db, hotel_name=hotel.hotel_name)
    if db_hotel:
        raise HTTPException(status_code=400, detail="Hotel already exists")
    return crud.create_hotel(db=db, hotel=hotel)


@app.get("/hotels/", response_model=List[schemas.Hotel])
def read_hotels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hotels = crud.get_hotels(db, skip=skip, limit=limit)
    return hotels


# rooms

@app.post("/hotels/{hotel_id}/rooms/", response_model=schemas.Room)
def create_room_for_hotel(
    hotel_id: int, room: schemas.RoomCreate, db: Session = Depends(get_db)
):
    return crud.create_hotel_room(db=db, room=room, hotel_id=hotel_id)

@app.get("/rooms/", response_model=List[schemas.Room])
def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return rooms

# rates

@app.post("/hotels/{hotel_id}/rooms/{room_id}/rateplans", response_model=schemas.RatePlan)
def create_rateplan(
    hotel_id: int, room_id: int, rateplan: schemas.RatePlan, db: Session = Depends(get_db)
):
    return crud.create_rateplan(db=db, rateplan=rateplan, room_id=room_id, hotel_id=hotel_id)

@app.get("hotels/{hotel_id}/rateplans/", response_model=List[schemas.RatePlan])
def read_rateplans_by_hotel_id(hotel_id: int, db: Session = Depends(get_db)):
    rateplans = crud.get_hotel_rateplan(db, hotel_id=hotel_id)
    return rateplans

@app.get("rooms/{room_id}/rateplans/", response_model=List[schemas.RatePlan])
def read_rateplans_by_room_id(room_id: int, db: Session = Depends(get_db)):
    rateplans = crud.get_room_rateplan(db, room_id=room_id)
    return rateplans

@app.get("/rateplans/", response_model=List[schemas.RatePlan])
def read_rateplans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rateplans = crud.get_rateplans(db, skip=skip, limit=limit)
    return rateplans

# availability
@app.post("/hotels/{hotel_id}/rooms/{room_id}/availability", response_model=schemas.RatePlan)
def set_availability(
    hotel_id: int, room_id: int, availability: schemas.Availability, db: Session = Depends(get_db)
):
    return crud.create_availability(db=db, availability=availability, room_id=room_id, hotel_id=hotel_id)

@app.get("rooms/{room_id}/availability/", response_model=List[schemas.Availability])
def read_availability_by_room_id(room_id: int, db: Session = Depends(get_db)):
    rateplans = crud.get_room_availability(db, room_id=room_id)
    return rateplans
