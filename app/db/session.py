from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Currently PostgreSQL is not running on my machine so using SQLite for testing purposes.
# DATABASE_URL = "postgresql://postgres:password@localhost:5432/newsfeed"
# engine = create_engine(DATABASE_URL)
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)