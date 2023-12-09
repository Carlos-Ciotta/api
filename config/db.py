from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:b6-BGe6dc14f-3bCe35ceADEg51-e5E5@roundhouse.proxy.rlwy.net:49436/railway")

meta = MetaData()

conn = engine.connect()
