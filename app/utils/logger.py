import logging
from pathlib import Path

from app.config.settings import settings


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Each module should request its own logger using:
        logger = get_logger(__name__)
    """

    # Ensure log directory exists
    Path(settings.LOG_DIR).mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = logging.FileHandler(
        settings.LOG_DIR / "application.log",
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger