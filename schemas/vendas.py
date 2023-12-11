from pydantic import BaseModel

class Venda(BaseModel):
    num_doc : int
    doc_cliente : str
    nome_cliente : str
    data : str
    hora : str
    valor : float
    status : str