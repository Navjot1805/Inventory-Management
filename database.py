from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

SessionLocal = sessionmaker(bind = engine,autoflush=False,autocommit=False)
#autoflush=False → “Don’t send my work-in-progress automatically”
# autocommit=False → “Don’t finalize/save until I say so”
Base = declarative_base()

#Base → tells SQLAlchemy “this is a database table class”