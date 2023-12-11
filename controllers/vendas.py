from fastapi import APIRouter, HTTPException
from config.db import conn
from models.vendas import vendas
from schemas.vendas import Venda
from sqlalchemy import select, insert
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from datetime import datetime
import re

venda = APIRouter()


@venda.get('/vendas/', tags=["vendas"],response_model=List[Venda])
def get_all():
    return conn.execute(vendas.select()).fetchall()


@venda.get('/vendas/{num_doc}', tags=["vendas"], response_model=Venda)
def get_by_num_doc(num_doc:int):
    response = conn.execute(vendas.select().where(vendas.c.num_doc == num_doc)).first()
    if response is None:
       return HTTPException(status_code=404, detail="Venda não encontrada no banco de dados")
    else:
        return response
    
@venda.get('/vendas/soma/{doc_cliente}', tags=["vendas"], response_model=List[Venda])
def get_by_num_doc(doc_cliente:str):
    response = conn.execute(vendas.select().where(vendas.c.doc_cliente == doc_cliente)).all()
    soma_valores = sum(resultado[6] for resultado in response)
    if response is None:
       return HTTPException(status_code=404, detail="Venda não encontrada no banco de dados")
    else:
        return response
    
@venda.post('/vendas/post', tags=["vendas"])
def create(venda_i: Venda):
    data_hora_atual = datetime.now()
    date = data_hora_atual.strftime("%d-%m-%Y")
    hour = data_hora_atual.strftime("%H:%M:%S")
    documento_cliente_numerico = re.sub(r'\D', '', venda_i.doc_cliente)
    response = conn.execute(vendas.select().where(vendas.c.num_doc == venda_i.num_doc)).first()
    try:
        if (venda_i.doc_cliente == documento_cliente_numerico) and (len(venda_i.doc_cliente) == 11) and (response == None):
            conn.execute(vendas.insert().values(
                doc_cliente = venda_i.doc_cliente,
                num_doc = venda_i.num_doc,
                nome_cliente = venda_i.nome_cliente,
                status = "Disponível",
                hora = hour,
                data = date,
                valor = venda_i.valor
            ))
            conn.commit()
            return {"Cadastrado com sucesso"}
        else:
            if response == None:
                return{"Número de Documento do Cliente cotém caracteres diferentes de números ou está incompleto"}
            else:
                return {"Venda já cadastrada"}
    except ValueError:
        return HTTPException(status_code=422, detail="Dados inválidos")

@venda.put('/vendas/put/{num_doc}', tags=["vendas"])
def update_doc(venda_i: Venda, num_doc: int):
    documento_cliente_numerico = re.sub(r'\D', '', venda_i.doc_cliente)
    try:
        if venda_i.doc_cliente == documento_cliente_numerico and len(venda_i.doc_cliente) == 11:
            conn.execute(
                vendas.update()
                .values(
                doc_cliente = venda_i.doc_cliente,
                num_doc = venda_i.num_doc,
                nome_cliente = venda_i.nome_cliente,
                status = venda_i.status,
                valor = venda_i.valor
            )
                .where(vendas.c.num_doc == num_doc)
            )
            conn.commit()
            return {"Alterado com sucesso"}
        else:
            return{"Número de Documento do Cliente cotém caracteres diferentes de números ou está incompleto"}
    except ValueError:
        return HTTPException(status_code=422, detail="Dados inválidos")


@venda.delete("/vendas/delete/{num_doc}", tags=["vendas"], status_code=HTTP_204_NO_CONTENT)
def delete_user(num_doc: int):
    response = conn.execute(vendas.select().where(vendas.c.num_doc == num_doc)).first()
    
    if response is None:
        return HTTPException(status_code=404, detail="Entrega não encontrada no banco de dados")
    else:
        conn.execute(vendas.delete().where(vendas.c.num_doc == num_doc))
        return {f"Dados do documento {id}, excluídos"}
