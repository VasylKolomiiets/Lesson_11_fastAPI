from links_bank.database import engine
from links_bank.tables import Base

Base.metadata.create_all(engine)