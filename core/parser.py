import re
import logging
from pathlib import Path
from typing import List

from core.utils import clean_text, ensure_file_exists

# Setup logger for this module
logger = logging.getLogger(__name__)


def extract_text_from_txt(file_path: str) -> str:
    """
    Extract raw text from a .txt file.

    Args:
        file_path (str): Path to the .txt file

    Returns:
        str: Extracted and cleaned text
    """
    path = ensure_file_exists(file_path)
    try:
        text = path.read_text(encoding="utf-8")
        return clean_text(text)
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        raise


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract raw text from a PDF file.

    Args:
        file_path (str): Path to the PDF file

    Returns:
        str: Extracted and cleaned text
    """
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        raise ImportError("PyPDF2 is required for PDF parsing. Install via: pip install PyPDF2")

    path = ensure_file_exists(file_path)
    text = ""
    try:
        pdf = PdfReader(str(path))
        for page in pdf.pages:
            text += page.extract_text() or ""
        return clean_text(text)
    except Exception as e:
        logger.error(f"Error reading PDF {file_path}: {e}")
        raise


def extract_skills(text: str, skills_db: List[str]) -> List[str]:
    """
    Extract skills from text by matching with a skills database.

    Args:
        text (str): Resume or job description text
        skills_db (List[str]): List of known skills

    Returns:
        List[str]: Matched skills
    """
    if not text:
        return []

    matched_skills = []
    text_lower = text.lower()

    for skill in skills_db:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text_lower):
            matched_skills.append(skill)

    return matched_skills
