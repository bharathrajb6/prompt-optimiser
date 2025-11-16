from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import ChatRequest, ChatResponse
from .llm import optimisePrompt

app = FastAPI(title="Prompt Optimiser")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/optimize", response_model=ChatResponse)
async def getPrompt(request: ChatRequest):
    optimisedPrompt = optimisePrompt(request.query)
    return {
        "answer": optimisedPrompt
    }
