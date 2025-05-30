from fastapi import FastAPI
from operations import soma

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo!"}

@app.get("/soma")
def somar(a: int, b: int):
    resultado = soma(a, b)
    return {"resultado": resultado}
