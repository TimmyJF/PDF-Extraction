from fastapi import FastAPI
from extract_pdf import extract_from_folder

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
@app.post("/extract")
def create_path(path: str):
    # Add the path to the paths list
    paths.append(path)
    return paths

# Make another endpoint for the API but at the folder path and call the extract_sum method
@app.get("/extract/{folder_path}")
def extract_sum(folder_path: int) -> str:
    #try to call the extract_from_folder function. If not, then throw an exception
    try:
        total = extract_from_folder(paths[folder_path])
        return {"total": total}
    except Exception as e:
        return {"Error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)