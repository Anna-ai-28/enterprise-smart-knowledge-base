from pathlib import Path

from pypdf import PdfReader

from app.config.settings import settings
from app.models.document import Document
from app.utils.logger import get_logger


logger = get_logger(__name__)


class PDFDocumentLoader:
    """
    Loads PDF files from the raw data directory
    and extracts page-wise text.
    """

    def __init__(self, data_directory: Path = settings.RAW_DATA_DIR):
        self.data_directory = Path(data_directory)

    def load(self) -> list[Document]:
        """
        Read every PDF inside the raw data folder
        and return extracted documents.
        """

        documents = []

        pdf_files = sorted(self.data_directory.glob("*.pdf"))

        if not pdf_files:
            logger.warning("No PDF files found.")
            return documents

        logger.info("Found %d PDF(s).", len(pdf_files))

        for pdf_path in pdf_files:

            try:

                reader = PdfReader(pdf_path)

                logger.info("Reading %s", pdf_path.name)

                for page_number, page in enumerate(reader.pages, start=1):

                    text = page.extract_text()

                    if not text:
                        continue

                    documents.append(
                        Document(
                            content=text,
                            source_file=pdf_path.name,
                            page_number=page_number,
                        )
                    )

            except Exception as exc:

                logger.exception(
                    "Failed to process %s: %s",
                    pdf_path.name,
                    exc,
                )

        logger.info("Loaded %d document pages.", len(documents))

        return documents