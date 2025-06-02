from .person import router as person
from .tasks import router as tasks
from .oauth import router as oauth

__all__ = ("person", "tasks", "oauth")
