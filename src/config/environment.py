import os

class Environments:
    """
    Singleton for managing environment variables.

    The `Environments` class loads environment variables using the `envparse` package.
    It ensures a consistent configuration across the application by enforcing a single
    instance of the environment configuration.

    Attributes:
        description (type): description.
    """

    def __new__(cls: "Environments") -> "Environments":
        """
        Implements the Singleton pattern to ensure only one instance exists.

        Returns:
            Environments: The single instance of the class.
        """
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self: "Environments") -> None:
        """
        Initializes the instance by loading environment variables.

        This constructor is idempotent, meaning it only initializes the class once,
        even if called multiple times.
        """
        if hasattr(self, "_initialized"):
            return  # Avoid reinitialization

        self._initialized = True

        self.base_key: str = os.getenv("BASE_KEY")

# Singleton instance ready for use
envs = Environments()