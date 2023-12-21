from fastapi import FastAPI
from controllers.vendas import venda
from controllers.entregas import entrega

app = FastAPI(
    title="API Sistema de Pontos Ciotta",
    description="API que manipula dados de um sistema de pontos",
    version="0.0.1",
)

#app.include_router(venda)
app.include_router(entrega)