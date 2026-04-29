from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
engine = create_engine(settings.POSTGRES_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
