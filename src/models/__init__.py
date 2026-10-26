from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine(
    "mysql+pymysql://root:@localhost/facturapp_25t4",
    echo=True
)
