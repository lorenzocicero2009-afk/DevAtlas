from dataclasses import dataclass


@dataclass
class Chunk:

    document: str

    index: int

    text: str

    start: int

    end: int