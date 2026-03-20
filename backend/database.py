import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./sql_app.db")

# Neon provides postgres://, SQLAlchemy requires postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args=connect_args)
else:
    engine = create_engine(DATABASE_URL, connect_args=connect_args, pool_size=5, max_overflow=0)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
