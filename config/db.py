from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:Mysql2023ciotta,*@localhost:3306/db-sistema-pontos-ciotta")

meta = MetaData()

conn = engine.connect()
