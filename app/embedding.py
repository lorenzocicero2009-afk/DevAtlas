from dataclasses import dataclass


@dataclass
class Embedding:

    document: str

    chunk_index: int

    text: str

    vector: list[float]