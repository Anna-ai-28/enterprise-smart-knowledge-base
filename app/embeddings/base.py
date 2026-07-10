from abc import ABC, abstractmethod


class BaseEmbeddingModel(ABC):
    """
    Abstract base class for embedding providers.
    """

    @abstractmethod
    def embed(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for a list of texts.
        """
        pass