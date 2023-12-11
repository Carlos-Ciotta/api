from pydantic import BaseModel
from typing import Optional

class Entrega(BaseModel):
    id: Optional[int]
    nome_cliente: str
    logradouro: str
    bairro: str
    telefone: str
    status : str
    hora : str
    data : str
