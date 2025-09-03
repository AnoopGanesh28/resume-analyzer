import os
import logging
import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from core.utils import clean_text

# Setup logger for this module
logger = logging.getLogger(__name__)


class EmbeddingModel:
    """
    Wrapper class for loading embedding model and computing similarities.
    """

    def __init__(self, model_name: str = None):
        """
        Initialize the embedding model.

        Args:
            model_name (str): HuggingFace model name. If None, reads from env EMBEDDING_MODEL.
        """
        if model_name is None:
            model_name = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

        logger.info(f"Loading embedding model: {model_name}")
        try:
            self.model = SentenceTransformer(model_name)
        except Exception as e:
            logger.error(f"Error loading model {model_name}: {e}")
            raise

    def get_embedding(self, text: str) -> np.ndarray:
        """
        Convert a single piece of text into an embedding vector.

        Args:
            text (str): Input text

        Returns:
            np.ndarray: Embedding vector
        """
        if not text:
            return np.zeros((384,))  # default size for MiniLM
        text = clean_text(text)
        return self.model.encode(text, convert_to_numpy=True)

    def get_embeddings(self, texts: List[str]) -> np.ndarray:
        """
        Convert multiple texts into embeddings.

        Args:
            texts (List[str]): List of texts

        Returns:
            np.ndarray: 2D array of embeddings
        """
        texts = [clean_text(t) for t in texts if t]
        return self.model.encode(texts, convert_to_numpy=True)

    def similarity(self, text1: str, text2: str) -> float:
        """
        Compute cosine similarity between two texts.

        Args:
            text1 (str): First text
            text2 (str): Second text

        Returns:
            float: Cosine similarity score (0-1)
        """
        emb1 = self.get_embedding(text1).reshape(1, -1)
        emb2 = self.get_embedding(text2).reshape(1, -1)
        score = cosine_similarity(emb1, emb2)[0][0]
        return round(float(score), 4)