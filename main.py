from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample marks data
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 75,
    "David": 95,
    "Eve": 80,
}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    marks = [students.get(n, "Not Found") for n in name]
    return {"marks": marks}
