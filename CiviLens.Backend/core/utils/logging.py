import logging
import sys
from logging.handlers import RotatingFileHandler




DEFAULT_LOG_LEVEL = logging.INFO




def get_logger(name: str = "civilens", level: int | None = None, file: str | None = None) -> logging.Logger:
    """Return a configured logger for the project.


    - If `file` is provided a RotatingFileHandler is added.
    - Streams logs to stdout by default (so Docker/Windows captures them).
    """


    logger = logging.getLogger(name)
    if level is None:
        level = DEFAULT_LOG_LEVEL
        logger.setLevel(level)


    if not logger.handlers:
        fmt = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")


        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(fmt)
        logger.addHandler(sh)


    if file:
        fh = RotatingFileHandler(file, maxBytes=10 * 1024 * 1024, backupCount=5)
        fh.setFormatter(fmt)
        logger.addHandler(fh)


    return logger