from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import BaseSettings

from models.events import Event
from models.users import User

class Settings(BaseSettings):
    MONGODB_URL: Optional[str] = None
    

    async def init_db(self):
        client = AsyncIOMotorClient(self.MONGODB_URL)
        await init_beanie(database=client.get_default_database(), document_models=[Event, User]) 

    class Config:
        env_file = ".env"        