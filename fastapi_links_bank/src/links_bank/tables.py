from sqlalchemy import (
    Column,
    Date,
    Integer,
    Float,
    String,
    CheckConstraint,
    # ForeignKey,
)

from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship


Base = declarative_base()


class Films(Base):
    __tablename__ = 'films'

    id_4 = Column(Integer, primary_key=True)
    film_title = Column(String)
    year = Column(Integer, CheckConstraint("year BETWEEN 1900 AND 2100"))
    category = Column(String)
    my_rate = Column(Float)
