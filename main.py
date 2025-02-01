import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from JSON file
with open("q-vercel-python.json", "r") as file:
    students_data = json.load(file)

# Convert to dictionary for quick lookup
students = {student["name"]: student["marks"] for student in students_data}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    result = {"marks": [students.get(n, 0) for n in name]}
    return result

