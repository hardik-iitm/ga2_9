import pandas as pd
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Initialize FastAPI application
app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Load student data from CSV (assuming CSV file named 'students.csv')
df = pd.read_csv('q-fastapi.csv')

# Convert the dataframe to a list of dictionaries for easy JSON conversion
students = df.to_dict(orient="records")

@app.get("/api")
async def get_students(class_: List[str] = Query(None)):
    """
    Endpoint to return students data.
    If 'class' query parameter is provided, filter students by class.
    """
    if class_:
        filtered_students = [student for student in students if student["class"] in class_]
    else:
        filtered_students = students

    return JSONResponse(content={"students": filtered_students})
