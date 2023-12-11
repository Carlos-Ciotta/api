from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:5cA54CGfcbE1GbDG3A1ge3c3h1-4E-3g@roundhouse.proxy.rlwy.net:22854/railway")

meta = MetaData()

conn = engine.connect()
