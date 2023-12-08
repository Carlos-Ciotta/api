from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:AA-FCeC6eH4feEg1d61GB-3a3ff1g-hf@monorail.proxy.rlwy.net:31935/railway")

meta = MetaData()

conn = engine.connect()
