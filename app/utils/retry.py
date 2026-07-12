import time
from functools import wraps

from app.core.logging import logger


def retry(max_attempts=3, delay=1):
    """
    Retry decorator for transient LLM failures.
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            last_exception = None

            for attempt in range(1, max_attempts + 1):

                try:

                    logger.info(
                        f"Attempt {attempt}/{max_attempts}"
                    )

                    return func(*args, **kwargs)

                except Exception as e:

                    last_exception = e

                    logger.warning(
                        f"Attempt {attempt} failed: {e}"
                    )

                    if attempt < max_attempts:
                        time.sleep(delay)

            logger.error("Maximum retry attempts exceeded.")

            raise last_exception

        return wrapper

    return decorator
