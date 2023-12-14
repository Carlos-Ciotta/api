from fastapi import APIRouter, HTTPException
from config.db import conn
from models.entregas import entregas
from schemas.entregas import Entrega
from sqlalchemy import select, insert
from typing import List
from datetime import datetime
import re

entrega = APIRouter()

@entrega.get('/entregas/',tags=["entregas"], response_model= List[Entrega])
def get():
    return conn.execute(entregas.select()).fetchall()

@entrega.get('/entregas/{id}',tags=["entregas"], response_model=Entrega)
def get_by_id(id:int):
    response = conn.execute(entregas.select().where(entregas.c.id == id)).first()
    if response is None:
       return HTTPException(status_code=404, detail="Entrega não encontrada no banco de dados")
    else:
        return response

@entrega.post('/entregas/post',tags=["entregas"])
def create(entrega_i: Entrega):
    data_hora_atual = datetime.now()
    date = data_hora_atual.strftime("%d-%m-%Y")
    hour = data_hora_atual.strftime("%H:%M:%S")
    telefone_numerico = re.sub(r'\D', '', entrega_i.telefone)
    try:
        if (entrega_i.telefone == telefone_numerico) and (len(entrega_i.telefone) == 11):
            conn.execute(entregas.insert().values(
                nome_cliente = entrega_i.nome_cliente,
                telefone = entrega_i.telefone,
                bairro = entrega_i.bairro,
                status = "Aguardando",
                logradouro = entrega_i.logradouro,
                hora = hour,
                data = date,
                previsao = entrega_i.previsao
            ))
            conn.commit()
            return {"Cadastrado com sucesso"}
    except ValueError:
        return HTTPException(status_code=422, detail="Dados inválidos")

@entrega.put('/entregas/put/{id}', tags=["entregas"])
def update_doc(entrega_i: Entrega, id: int):
    response = get_by_id(id)
    if response == None:
        print("Entrega não cadastrada no banco de dados")
    else:
        telefone_numerico = re.sub(r'\D', '', entrega_i.telefone)
        try:
            if (entrega_i.telefone == telefone_numerico) and (len(entrega_i.telefone) == 11):
                conn.execute(
                entregas.update()
                .values(
                nome_cliente = entrega_i.nome_cliente,
                telefone = entrega_i.telefone,
                bairro = entrega_i.bairro,
                status = entrega_i.status,
                logradouro = entrega_i.logradouro,
                previsao = entrega_i.previsao
            )
                .where(entregas.c.id == id)
            )
            conn.commit()
            return {"Cadastrado com sucesso"}
        except ValueError:
            return HTTPException(status_code=422, detail="Dados inválidos")
    
@entrega.put('/entregas/put/s/{id}', tags=["entregas"])
def update_status(status:str, id:int):
    response = get_by_id(id)
    if response == None:
        print("Entrega não cadastrada no banco de dados")
    else:
        try:
            conn.execute(
                entregas.update()
                .values(
                status = status,
            )
                .where(entregas.c.id == id)
            )
            conn.commit()
            return {"Status alterado"}
        except ValueError:
            return HTTPException(status_code=422, detail="Dados inválidos")

@entrega.delete("/entregas/delete/{id}", tags=["entregas"])
def delete_user(id: int):
    response = get_by_id(id)
    if response is None:
        return HTTPException(status_code=404, detail="Entrega não encontrada no banco de dados")
    else:
        conn.execute(entregas.delete().where(entregas.c.id == id))
        return {f"Dados da entrega {id}, excluídos"}
