from dataclasses import dataclass
from typing import Callable, Dict, Any


@dataclass
class Tool:
    name: str
    description: str
    input_schema: Dict[str, Any]
    func: Callable | None = None
    endpoint: str | None = None