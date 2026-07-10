from app.text_splitters.base import BaseTextSplitter


class RecursiveTextSplitter(BaseTextSplitter):
    """
    Production-grade recursive text splitter.

    Splitting priority:

    Paragraphs
        ↓
    Newlines
        ↓
    Sentences
        ↓
    Spaces
        ↓
    Characters
    """

    def __init__(
        self,
        chunk_size: int,
        overlap: int,
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_text(
        self,
        text: str,
    ) -> list[str]:

        raise NotImplementedError