from fastapi import FastAPI
from qwen import QwenChatbot

app = FastAPI()

model = QwenChatbot()

@app.get("/run")
def run():
  print("Chat with Qwen3\n")
  while (message := input("User\n ")) != "exit":
    response = model.generate_response(message)
    print("\n---------------------------------------\n")
    print(f"Chat bot\n {response}")
    print("\n---------------------------------------\n")

@app.get("/health")
def healthy():
  return "I'm a healthy small qwen"
  