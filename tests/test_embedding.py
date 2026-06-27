from app.chunk import Chunk

from app.embedding_engine import EmbeddingEngine


chunk = Chunk(

    document="linux.txt",

    index=0,

    text="Linux is an open source operating system.",

    start=0,

    end=42

)

engine = EmbeddingEngine()

embedding = engine.create_embedding(chunk)

print()

print(len(embedding.vector))

print()

print(embedding.vector[:10])