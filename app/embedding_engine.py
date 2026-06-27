from app.chunk import Chunk
from app.embedding import Embedding

from app.providers.embedding.ollama_embedding import OllamaEmbeddingProvider


class EmbeddingEngine:

    def __init__(self):

        self.provider = OllamaEmbeddingProvider()

    def create_embedding(
        self,
        chunk: Chunk
    ):

        vector = self.provider.embed(

            chunk.text

        )

        return Embedding(

            document=chunk.document,

            chunk_index=chunk.index,

            text=chunk.text,

            vector=vector

        )