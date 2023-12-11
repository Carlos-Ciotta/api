from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta, engine

vendas = Table(
    "vendas",
    meta,
    Column("Id", Integer, primary_key=True),
    Column("num_doc", Integer),
    Column("nome_cliente",String(255)),
    Column("valor", Float),
    Column("doc_cliente", String(255)),
    Column("status", String(255)),
    Column("hora", String(255)),
    Column("data", String(255))
)

meta.create_all(engine)