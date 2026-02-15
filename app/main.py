from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agent import FloorPlanAgent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = FloorPlanAgent()

@app.get("/")
def root():
    return {"message": "AI Floor Plan Agent Running"}

@app.post("/generate-floor")
def generate_floor(floor_plan: dict):
    return agent.process(floor_plan)
