from pydantic import BaseModel

class Venda(BaseModel):
    num_doc : int
    doc_cliente : float
    nome_cliente : str
    data : str
    hora : str
    valor : float
    status : int