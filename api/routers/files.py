from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
import shutil
import uuid
from pathlib import Path
import logging
from core.pdf_parse import pdf_to_markdown
from core.paddleocr import PPStructure
from libs.file_tools import delete_files_in_directory

ocr_engine = PPStructure(
    recovery=True,
    structure_version="PP-StructureV2",
    show_log=False,
)

router = APIRouter(
    prefix="/files",
    tags=["files"],
)

# 获取当前文件的目录
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = os.path.join(BASE_DIR, "upload_files")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_files_and_parse(file: UploadFile = File(...)):
    delete_files_in_directory(UPLOAD_FOLDER)
    safe_filename = f"{uuid.uuid4()}-{file.filename}"
    save_path = os.path.join(UPLOAD_FOLDER, safe_filename)

    try:
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"message": "Could not save file."}
        )

    file_url = f"http://127.0.0.1:8000/files/static/{safe_filename}"
    return {
        "filename": file.filename,
        "uuid_filename": safe_filename,
        "content_type": file.content_type,
        "url": file_url,
    }


@router.get("/text_parse")
async def upload_files_and_parse(file_id: str):
    pdf_path = os.path.join(UPLOAD_FOLDER, file_id)
    logging.info(f"pdf_path: {pdf_path}")
    parse_result = pdf_to_markdown(pdf_path, ocr_engine=ocr_engine)
    return {"parse_result": parse_result}
