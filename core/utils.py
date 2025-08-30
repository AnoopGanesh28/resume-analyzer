#Import modules
import re                   #for regular expressions
import logging              #for logging
from pathlib import Path    #for path manipulations

#Setup logging (useful for debugging & clean output)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s", 
    handlers=[logging.StreamHandler()],
)

logger=logging.getLogger(__name__)


def clean_text(text: str) -> str:
    """
    Clean text by removing extra spaces, newlines, and non-printable characters.
    
    Args:
        text (str): Raw extracted text from resume/job description.
    
    Returns:
        str: Cleaned text.
    """
    if not text:
        return ""
    
    # Remove non-printable characters
    text = re.sub(r'[^\x20-\x7E\n]', ' ', text)
    
    # Replace multiple spaces/newlines with single space
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def ensure_file_exists(file_path: str) -> Path:
    """
    Ensure that the given file exists. Raise error if not found.
    
    Args:
        file_path (str): Path to a file
    
    Returns:
        Path: Path object if file exists.
    """
    path = Path(file_path)
    if not path.exists():
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    return path
    