import time

from app.core.logging import logger


class AIMetrics:
    """
    Collects and logs AI inference metrics.
    """

    @staticmethod
    def start():

        return time.perf_counter()

    @staticmethod
    def stop(start_time):

        return round(
            time.perf_counter() - start_time,
            3
        )

    @staticmethod
    def log_metrics(
        *,
        model: str,
        prompt: str,
        response: str,
        latency: float,
        retries: int,
        validation_success: bool
    ):

        logger.info("=" * 50)

        logger.info("AI OBSERVABILITY")

        logger.info(f"Model               : {model}")

        logger.info(
            f"Prompt Characters   : {len(prompt)}"
        )

        logger.info(
            f"Response Characters : {len(response)}"
        )

        logger.info(
            f"Latency (sec)       : {latency}"
        )

        logger.info(
            f"Retries             : {retries}"
        )

        logger.info(
            f"Validation          : {validation_success}"
        )

        logger.info("=" * 50)
