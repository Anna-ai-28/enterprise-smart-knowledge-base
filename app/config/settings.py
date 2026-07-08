from pathlib import Path
import os

from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()


class Settings:
    """
    Centralized application configuration.

    All project settings should be accessed through
    this class instead of hardcoding values.
    """

    # -------------------------
    # Base Directory
    # -------------------------
    BASE_DIR = Path(__file__).resolve().parents[2]

    # -------------------------
    # Data Directories
    # -------------------------
    RAW_DATA_DIR = BASE_DIR / "data" / "raw"
    PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

    # -------------------------
    # Vector Database
    # -------------------------
    CHROMA_DB_DIR = BASE_DIR / "chroma_db"

    # -------------------------
    # Logging
    # -------------------------
    LOG_DIR = BASE_DIR / "logs"

    # -------------------------
    # Gemini API
    # -------------------------
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # -------------------------
    # Chunking Parameters
    # -------------------------
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100


settings = Settings()