from sqlalchemy import create_engine
from config import DB_HOST,DB_NAME,DB_PASSWORD,DB_PORT,DB_USER
from urllib.parse import quote_plus

DB_PASSWORD = quote_plus(DB_PASSWORD)

print(DB_PASSWORD)

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print(DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)

print(engine)