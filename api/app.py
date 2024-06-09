from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.staticfiles import StaticFiles
import uvicorn
from pathlib import Path
import os
from routers import files

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = os.path.join(Path(__file__).resolve().parent, "upload_files")
print(UPLOAD_FOLDER)
app.mount("/files/static", StaticFiles(directory=UPLOAD_FOLDER), name="static")

app.include_router(files.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
