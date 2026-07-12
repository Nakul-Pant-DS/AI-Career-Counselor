from enum import Enum


class VectorIndex(str, Enum):
    """
    Supported Vector Database indexes.
    """

    RESUME = "resume"

    CAREER = "career"

    JOBS = "jobs"

    INTERVIEW = "interview"
