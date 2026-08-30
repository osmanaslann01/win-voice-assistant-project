from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Command:
    name: str
    arguments: dict[str, Any]
        