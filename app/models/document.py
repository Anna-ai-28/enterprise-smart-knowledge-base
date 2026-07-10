from dataclasses import dataclass


@dataclass(slots=True)
class Document:
    """
    Represents one extracted document page
    and its metadata.
    """

    content: str
    source_file: str
    page_number: int