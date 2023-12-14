from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:6E2-bF5aBc4g5AFHEGg15dhF6aGE2bDC@viaduct.proxy.rlwy.net:18325/railway")

meta = MetaData()

conn = engine.connect()
