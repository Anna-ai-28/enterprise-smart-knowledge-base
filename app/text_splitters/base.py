from abc import ABC, abstractmethod


class BaseTextSplitter(ABC):
    """
    Base interface for all text splitters.
    """

    @abstractmethod
    def split_text(
        self,
        text: str,
    ) -> list[str]:
        raise NotImplementedError