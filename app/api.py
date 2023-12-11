from fastapi import FastAPI, HTTPException, Response, Depends
from pydantic import BaseModel
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtain the parent directory
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

from modules.chatbot.eves import Eve_v5a

app = FastAPI()

class sign_in(BaseModel):
    client_id: str = "1"

@app.post("/initialize_eve")
def initialize_eve(payload: sign_in = Depends()):
    eve = Eve_v5a()
    eve.initialize()

