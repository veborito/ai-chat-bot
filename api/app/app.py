from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello World"}

@app.get("/health")
def read_root():
  return {"You called ping i call pong"}

@app.get("/chat/{model}")
def chat_w_model(model: str):
  return {f"you are chatting with {model}"}