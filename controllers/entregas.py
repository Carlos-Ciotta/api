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
    try:
        data_hora_atual = datetime.now()
        date = data_hora_atual.strftime("%d-%m-%Y")
        hour = data_hora_atual.strftime("%H:%M:%S")
        telefone_numerico = re.sub(r'\D', '', entrega_i.telefone)
        region = "+55"
        # Verifica se o número de telefone contém apenas dígitos
        if entrega_i.telefone == telefone_numerico and len(telefone_numerico) == 11:
            entrega_i.telefone = region + entrega_i.telefone
            conn.execute(entregas.insert().values(
                nome_cliente = entrega_i.nome_cliente,
                telefone = entrega_i.telefone,
                bairro = entrega_i.bairro,
                status = "Aguardando",
                logradouro = entrega_i.logradouro,
                hora = hour,
                data = date
            ))
            conn.commit()
            return {"Cadastrado com sucesso"}
        else:
            return HTTPException(status_code=422, detail="Telefone inválido")
    except ValueError:
        # Se houver um erro de validação, retorne uma resposta de erro 422
        return HTTPException(status_code=422, detail="Dados inválidos")

@entrega.put('/entregas/put/{id}', tags=["entregas"])
def update_doc(entrega_i: Entrega, id: int):
    try:
        telefone_numerico = re.sub(r'\D', '', entrega_i.telefone)
        region = "+55"
        if entrega_i.telefone == telefone_numerico and len(telefone_numerico) == 11:
            entrega_i.telefone = region + entrega_i.telefone
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
        else:
            return HTTPException(status_code=422, detail="Telefone inválido")
    except ValueError:
        # Se houver um erro de validação, retorne uma resposta de erro 422
        return HTTPException(status_code=422, detail="Dados inválidos")

@entrega.delete("/entregas/delete/{id}", tags=["entregas"])
def delete_user(id: int):
    response = conn.execute(entregas.select().where(entregas.c.id == id)).first()
    
    if response is None:
        return HTTPException(status_code=404, detail="Entrega não encontrada no banco de dados")
    else:
        conn.execute(entregas.delete().where(entregas.c.id == id))
        return {f"Dados do documento {id}, excluídos"}