from dataclasses import dataclass


@dataclass(slots=True)
class Chunk:
    """
    Represents one text chunk ready
    for embedding and retrieval.
    """

    chunk_id: str
    content: str
    source_file: str
    page_number: int