
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql+psycopg2://awantikachauhan:your_new_password@localhost:5432/postgres_fastapi"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # we need session to connect app with server



