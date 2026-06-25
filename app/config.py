import json
from pathlib import Path


class Config:

    def __init__(self):

        config_file = Path("config/settings.json")

        if not config_file.exists():
            raise FileNotFoundError("config/settings.json not found")

        with open(config_file, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def model(self):
        return self.data["model"]

    @property
    def dataset(self):
        return self.data["dataset"]

    @property
    def embedding_model(self):
        return self.data["embedding_model"]

    @property
    def chunk_size(self):
        return self.data["chunk_size"]

    @property
    def chunk_overlap(self):
        return self.data["chunk_overlap"]

    @property
    def top_k(self):
        return self.data["top_k"]

    @property
    def temperature(self):
        return self.data["temperature"]

    @property
    def max_context(self):
        return self.data["max_context"]
