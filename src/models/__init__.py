from sqlalchemy import create_engine
import pymysql
from sqlalchemy.orm import sessionmaker, declarative_base

#Create a SQLAL1chemy engine 
 
engine = create_engine("mysql+pymysql://root:@localhost/facturapp_25t4?charset=utf8mb4",echo=True)
connection = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

Base.metadata.bind = engine
