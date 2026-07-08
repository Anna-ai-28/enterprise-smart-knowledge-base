from uuid import uuid4

from app.config.settings import settings
from app.utils.chunk import Chunk
from app.utils.document import Document
from app.utils.logger import get_logger


logger = get_logger(__name__)


class TextChunker:
    """
    Splits extracted documents into overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = settings.CHUNK_SIZE,
        chunk_overlap: int = settings.CHUNK_OVERLAP,
    ):
        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size."
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, documents: list[Document]) -> list[Chunk]:
        """
        Convert documents into overlapping chunks.
        """

        chunks: list[Chunk] = []

        step = self.chunk_size - self.chunk_overlap

        for document in documents:

            text = document.content.strip()

            if not text:
                continue

            for start in range(0, len(text), step):

                end = start + self.chunk_size

                chunk_text = text[start:end].strip()

                if not chunk_text:
                    continue

                chunks.append(
                    Chunk(
                        chunk_id=str(uuid4()),
                        content=chunk_text,
                        source_file=document.source_file,
                        page_number=document.page_number,
                    )
                )

        logger.info(
            "Generated %d chunk(s).",
            len(chunks),
        )

        return chunks