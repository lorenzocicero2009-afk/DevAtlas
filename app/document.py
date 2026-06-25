from dataclasses import dataclass, field


@dataclass
class Document:
    filepath: str
    filename: str
    extension: str
    size: int
    text: str = ""
    metadata: dict = field(default_factory=dict)