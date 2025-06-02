from typing import Dict, Any

class BaseAgent:
    """Base class for all agents in the system."""

    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}

    def log_error(self, error: Exception, message: str) -> None:
        """Log an error with a custom message."""
        print(f"Error: {message} - {str(error)}") 