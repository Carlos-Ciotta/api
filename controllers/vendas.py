from fastapi import APIRouter
from config.db import conn
from models.vendas import vendas
from schemas.vendas import Venda
from sqlalchemy import select, insert
from typing import List
from starlette.status import HTTP_204_NO_CONTENT


venda = APIRouter()


@venda.get('/index', response_model=List[Venda])
def index():
    return conn.execute(vendas.select()).fetchall()


@venda.get('/index/{num_doc}', response_model=Venda)
def get_by_num_doc(num_doc:int):
    response = conn.execute(vendas.select().where(vendas.c.num_doc == num_doc)).first()
    return response

@venda.post('/index/post')
def create(venda_i: Venda):
    conn.execute(vendas.insert().values(
        doc_cliente = venda_i.doc_cliente,
        num_doc = venda_i.num_doc,
        nome_cliente = venda_i.nome_cliente,
        status = venda_i.status,
        hora = venda_i.hora,
        data = venda_i.data,
        valor = venda_i.valor
    ))
    conn.commit()
    return {"Cadastrado com sucesso"}

@venda.put('/index/put/{num_doc}', tags=["vendas"])
def update_doc(venda_i: Venda, num_doc: int):
    conn.execute(
        vendas.update()
        .values(
        doc_cliente = venda_i.doc_cliente,
        num_doc = venda_i.num_doc,
        nome_cliente = venda_i.nome_cliente,
        status = venda_i.status,
        hora = venda_i.hora,
        data = venda_i.data,
        valor = venda_i.valor
    )
        .where(vendas.c.num_doc == num_doc)
    )
    conn.commit()
    return {"Alterado com sucesso"}


@venda.delete("/index/delete/{num_doc}", tags=["vendas"], status_code=HTTP_204_NO_CONTENT)
def delete_user(num_doc: int):
    conn.execute(vendas.delete().where(vendas.c.num_doc == num_doc))
    conn.commit()
    return {f"Dados do documento {num_doc}, excluídos"}