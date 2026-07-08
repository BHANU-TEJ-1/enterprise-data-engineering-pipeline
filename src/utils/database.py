'''It should only be responsible for creating and returning a database connection/engine.

It should not:

execute SQL
read tables
insert data
perform ETL logic

Single Responsibility Principle.'''
"""
database.py

Database utility functions for the Enterprise Data Engineering Pipeline.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def get_engine() -> Engine:
    """
    Create and return a SQLAlchemy engine.
    """

    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    database = os.getenv("POSTGRES_DATABASE")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")

    connection_url = (
        f"postgresql+psycopg2://"
        f"{user}:{password}@{host}:{port}/{database}"
    )

    return create_engine(connection_url)


def get_connection():
    """
    Return an active database connection.
    """
    return get_engine().connect()


def test_connection() -> bool:
    try:
        engine = get_engine()

        with engine.connect() as connection:
            print("PostgreSQL connection successful!")
            return True

    except Exception as exc:
        print("DATABASE ERROR")
        print(type(exc).__name__)
        print(exc)
        print("=====")
        return False