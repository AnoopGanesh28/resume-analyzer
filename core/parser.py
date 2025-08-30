# Import modules
import re
import pdfplumber
import docx
from pathlib import Path
from typing import Union
from core.utils import ensure_file_exists, clean_text
import logging

# Setup logger for this module
logger = logging.getLogger(__name__)


def extract_text_from_pdf(file_path: Union[str, Path]) -> str:
    """
    Extract text from a PDF file using pdfplumber.
    
    Args:
        file_path (str | Path): Path to the PDF file.
    
    Returns:
        str: Extracted text content.
    """
    path = ensure_file_exists(file_path)
    text = ""
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""  # Avoid None if page is empty
    except Exception as e:
        logger.error(f"Failed to extract text from PDF: {path}, Error: {e}")
        raise
    return clean_text(text)


def extract_text_from_docx(file_path: Union[str, Path]) -> str:
    """
    Extract text from a DOCX file using python-docx.
    
    Args:
        file_path (str | Path): Path to the DOCX file.
    
    Returns:
        str: Extracted text content.
    """
    path = ensure_file_exists(file_path)
    text = ""
    try:
        doc = docx.Document(path)
        text = "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        logger.error(f"Failed to extract text from DOCX: {path}, Error: {e}")
        raise
    return clean_text(text)


def extract_text_from_txt(file_path: Union[str, Path]) -> str:
    """
    Extract text from a plain TXT file.
    
    Args:
        file_path (str | Path): Path to the TXT file.
    
    Returns:
        str: Extracted text content.
    """
    path = ensure_file_exists(file_path)
    try:
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        logger.error(f"Failed to read TXT file: {path}, Error: {e}")
        raise
    return clean_text(text)


def parse_resume(file_path: Union[str, Path]) -> str:
    """
    Parse a resume file (PDF, DOCX, or TXT) and return cleaned text.
    
    Args:
        file_path (str | Path): Path to resume file.
    
    Returns:
        str: Cleaned text extracted from the resume.
    """
    path = Path(file_path)
    ext = path.suffix.lower()

    if ext == ".pdf":
        return extract_text_from_pdf(path)
    elif ext == ".docx":
        return extract_text_from_docx(path)
    elif ext == ".txt":
        return extract_text_from_txt(path)
    else:
        logger.error(f"Unsupported file type: {ext}")
        raise ValueError(f"Unsupported file type: {ext}")
