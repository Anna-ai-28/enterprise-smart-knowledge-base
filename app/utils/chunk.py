from dataclasses import dataclass


@dataclass(slots=True)
class Chunk:
    """
    Represents one chunk of text along with
    metadata required for retrieval.
    """

    chunk_id: str
    content: str
    source_file: str
    page_number: int