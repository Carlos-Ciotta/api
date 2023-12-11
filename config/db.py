from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:a4effgddd5aFAbh4g4AbH3F1aheCfHGF@viaduct.proxy.rlwy.net:46618/railway/railway")

meta = MetaData()

conn = engine.connect()
