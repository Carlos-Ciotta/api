from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta, engine

vendas = Table(
    "vendas",
    meta,
    Column("num_doc", Integer, primary_key=True),
    Column("nome_cliente",String(255)),
    Column("valor", Float),
    Column("doc_cliente", Float),
    Column("status", Integer),
    Column("hora", String(255)),
    Column("data", String(255))
)

meta.create_all(engine)