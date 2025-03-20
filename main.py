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

@app.get("/api")
async def get_students(q: List[str] = Query(None)):
    # If class_ is provided, filter students by class
    if q:
        filtered_df = df[df["class"].isin(q)]
    else:
        filtered_df = df

    # Convert the filtered DataFrame to a list of dictionaries
    students = filtered_df.to_dict(orient="records")

    # Return the data in the required format
    return JSONResponse(content={"students": students})
