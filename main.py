from fastapi import FastAPI, HTTPException
from extract_pdf import extract_from_folder
import uvicorn

# This is an API using FastAPI that will make it easier for the user to query data for the file that they are looking at
# Initialize the app
app = FastAPI()

# Initialize a list for the different paths to go to
paths = []

# Make the welcome statement in JSON
@app.get("/")
def root():
    return {"message": "Welcome to the PDF extraction API!"}

# Make an endpoint to add the folder path to your API
# MAKE SURE THAT YOUR ADDRESS THAT YOU ARE POSTING IS FORMATTED CORRECTELY:
# For example, my folder path is c:/Users/timmy/Dropbox/My PC (Timmy)/Downloads/k1x assignment
# but I used c%3A%2FUsers%2Ftimmy%2FDropbox%2FMy%20PC%20%28Timmy%29%2FDownloads%2Fk1x%20assignment instead
@app.post("/extract")
def create_path(path: str):
    # Add the path to the paths list
    paths.append(path)
    return paths

# Make another endpoint for the API but at the folder path and call the extract_sum method
@app.get("/extract/{index}")
def extract_sum(index: int) -> dict:
    # Check to see if the index is valid or not
    if index < len(paths):
        # Try to call the extract_from_folder function. If not, then throw an exception
        try:
            total = extract_from_folder(paths[index])
            return {"total": total}
        except Exception as e:
            return {"Error": "Invalid folder path"}
    else:
        raise HTTPException(status_code=404, detail=f"Path {index} not found")