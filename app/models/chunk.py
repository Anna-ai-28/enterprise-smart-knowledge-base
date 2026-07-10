from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Chunk:
    """
    Represents a chunk of text ready for
    embedding and retrieval.
    """

    id: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)