from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

# sqlite work in one thread - so trick settings amd accurate using
# each request in new thread and close it after.
engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False},
)

# we have to commit `by hands` 
Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session() -> Session:
    session = Session()
    try:
        return session
    finally:
        session.close()
