from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta, engine

entregas = Table(
    "entregas",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nome_cliente",String(255)),
    Column("logradouro", String(255)),
    Column("telefone", Float),
    Column("bairro", String(255)),
    Column("status", String(255)),
    Column("data", String(255)),
    Column("hora", String(255))
)

meta.create_all(engine)