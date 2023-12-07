from fastapi import APIRouter
from config.db import conn
from models.entregas import entregas
from schemas.entregas import Entrega
from sqlalchemy import select, insert
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from datetime import datetime

entrega = APIRouter()

@entrega.get('/entrega/',tags=["entregas"], response_model= List[Entrega])
def get():
    return conn.execute(entregas.select()).fetchall()

@entrega.get('/entrega/{id}', response_model=Entrega)
def get_by_id(id:int):
    response = conn.execute(entregas.select().where(entregas.c.id == id)).first()
    return response

@entrega.post('/entrega/post',tags=["entregas"])
def create(entrega_i: Entrega):
    data_hora_atual = datetime.now()
    date = data_hora_atual.strftime("%d-%m-%Y")
    hour = data_hora_atual.strftime("%H:%M:%S")

    conn.execute(entregas.insert().values(
        nome_cliente = entrega_i.nome_cliente,
        telefone = entrega_i.telefone,
        bairro = entrega_i.bairro,
        status = entrega_i.status,
        logradouro = entrega_i.logradouro,
        hora = hour,
        data = date
    ))
    conn.commit()
    return {"Cadastrado com sucesso"}

@entrega.put('/entregas/put/{id}', tags=["entregas"])
def update_doc(entrega_i: Entrega, id: int):
    conn.execute(
        entregas.update()
        .values(
        nome_cliente = entrega_i.nome_cliente,
        telefone = entrega_i.telefone,
        bairro = entrega_i.bairro,
        status = entrega_i.status,
        logradouro = entrega_i.logradouro
    )
        .where(entregas.c.id == id)
    )
    conn.commit()
    return {"Alterado com sucesso"}

@entrega.delete("/entregas/delete/{id}", tags=["entregas"], status_code=HTTP_204_NO_CONTENT)
def delete_user(id: int):
    conn.execute(entregas.delete().where(entregas.c.id == id))
    conn.commit()
    return {f"Dados do documento {id}, excluídos"}