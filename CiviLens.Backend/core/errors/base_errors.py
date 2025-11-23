class CivilensError(Exception):
    """Base error for Civilens domain."""

    def __init__(self, message: str = "An error occurred in Civilens", code: str | None = None):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.__class__.__name__}: {self.message}"


class NotFoundError(CivilensError):
    """Raised when a requested resource is not found."""


class ValidationError(CivilensError):
    """Raised when data validation fails."""


class ExternalServiceError(CivilensError):
    """Raised when an external dependency (vector DB, LLM) fails."""