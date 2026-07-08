from dataclasses import dataclass


@dataclass(slots=True)
class Document:
    """
    Represents one extracted page (or document unit)
    along with its metadata.
    """

    content: str
    source_file: str
    page_number: int