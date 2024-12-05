import os
import logging
from logging.handlers import RotatingFileHandler

from app.core.config import settings

log_format = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s " "(%(filename)s:%(lineno)d)"
)


def use_logger(name):
    logger = logging.getLogger(name)

    if settings.ENVIRONMENT == "local":
        logger.setLevel(logging.INFO)

        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, f"{name}.log"),
            maxBytes=1024 * 1024 * 5,
            backupCount=5,
        )
        file_handler.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(log_format)
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 핸들러 추가
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    elif settings.ENVIRONMENT == "production" or settings.ENVIRONMENT == "staging":
        logger.setLevel(logging.ERROR)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)

        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    else:
        raise ValueError(f"Unknown environment: {settings.ENVIRONMENT}")

    return logger
