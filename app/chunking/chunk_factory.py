from uuid import uuid4

from app.models import Chunk, Document


class ChunkFactory:
    """
    Responsible for creating Chunk objects.
    """

    @staticmethod
    def create(
        text: str,
        document: Document,
    ) -> Chunk:

        return Chunk(
            id=str(uuid4()),
            text=text,
            metadata={
                "source_file": document.source_file,
                "page_number": document.page_number,
            },
        )