from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/receive")
def receive_message(message: Message):
    print(f"Received message: {message.message}")
    response = f"print('Hello sent from Service B', end = '')"
    print(f"Sending response: {response}")
    return {"response": response}

if __name__ == "__main__":
    print("Starting Service B...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
