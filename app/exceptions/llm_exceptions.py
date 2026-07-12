class LLMException(Exception):
    """Base exception for all LLM-related errors."""
    pass


class InvalidLLMResponseException(LLMException):
    """Raised when the LLM response cannot be parsed or validated."""
    pass


class LLMValidationException(LLMException):
    """Raised when validated data doesn't match the expected schema."""
    pass
