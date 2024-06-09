import os
import cv2
import sys
import numpy as np
from PIL import Image
from pathlib import Path
from paddle.utils import try_import
from core.paddleocr import save_structure_res
from core.paddleocr.ppstructure.recovery.recovery_to_doc import (
    sorted_layout_boxes,
    convert_info_markdown,
)

BASE_DIR = Path(__file__).resolve().parent.parent
SAVE_FOLDER = os.path.join(BASE_DIR, "upload_files")


def pdf_to_markdown(pdf_path, ocr_engine):
    imgs = _covert_pdf_to_img(pdf_path)
    layout_res = _get_layout(imgs, ocr_engine, pdf_path)
    res = convert_info_markdown(
        layout_res, SAVE_FOLDER, os.path.basename(pdf_path).split(".")[0]
    )
    return res


# 从 PDF 中获取页面图像
def _covert_pdf_to_img(pdf_path) -> list:
    """从 PDF 中获取页面图像"""
    fitz = try_import("fitz")
    imgs = []

    with fitz.open(pdf_path) as pdf:
        for pg in range(0, pdf.page_count):
            page = pdf[pg]
            pm = page.get_pixmap(alpha=False)
            mat = fitz.Matrix(
                2, 2
            )  # 将 PDF 页面缩放两倍，为了提高图像的分辨率和清晰度。
            pm = page.get_pixmap(matrix=mat, alpha=False)

            # if width or height > 2000 pixels, don't enlarge the image
            if pm.width > 2000 or pm.height > 2000:
                pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)

            # 将像素图转换为 PIL 图像对象。
            img = Image.frombytes("RGB", [pm.width, pm.height], pm.samples)

            # 将 PIL 图像转换为 NumPy 数组，并从 RGB 格式转换为 BGR 格式，以便 OpenCV 使用。
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            imgs.append(img)

    return imgs


def _get_layout(imgs, ocr_engine, pdf_path):
    res = []
    for index, img in enumerate(imgs):
        result = ocr_engine(img)
        save_structure_res(
            result, SAVE_FOLDER, os.path.basename(pdf_path).split(".")[0], index
        )
        h, w, _ = img.shape
        res += sorted_layout_boxes(result, w)
    return res
