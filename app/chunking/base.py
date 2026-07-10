from abc import ABC, abstractmethod

from app.models import Document, Chunk


class BaseChunker(ABC):
    """
    Interface for all chunking strategies.
    """

    @abstractmethod
    def split(
        self,
        documents: list[Document],
    ) -> list[Chunk]:
        """
        Split documents into chunks.
        """
        raise NotImplementedError