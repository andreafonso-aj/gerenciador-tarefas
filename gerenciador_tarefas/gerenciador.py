from fastapi import FastAPI

TAREFAS = [{'id': 1, 'título': 'Comprar ovos'}, {'id': 2, 'título': 'Comprar Sabonete'}]

app = FastAPI()

@app.get("/tarefas")
def listar():
    return TAREFAS