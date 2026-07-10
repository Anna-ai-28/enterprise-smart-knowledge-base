from sentence_transformers import SentenceTransformer

from app.embeddings.base import BaseEmbeddingModel
from app.utils.logger import get_logger


logger = get_logger(__name__)


class SentenceTransformerEmbedding(BaseEmbeddingModel):
    """
    Embedding provider using Sentence Transformers.
    """

    MODEL_NAME = "all-MiniLM-L6-v2"

    def __init__(self):
        logger.info("Loading embedding model: %s", self.MODEL_NAME)

        self.model = SentenceTransformer(self.MODEL_NAME)

        logger.info("Embedding model loaded successfully.")

    def embed(self, texts: list[str]) -> list[list[float]]:
        """
        Convert text into vector embeddings.
        """

        if not texts:
            logger.warning("No text provided for embedding.")
            return []

        logger.info("Generating embeddings for %d text(s).", len(texts))

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=False,
        )

        return embeddings.tolist()