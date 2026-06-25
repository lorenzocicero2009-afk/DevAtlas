from app.chunk import Chunk
from app.document import Document


class Chunker:

    def __init__(
        self,
        chunk_size=500,
        overlap=100
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, document: Document):

        chunks = []

        text = document.text

        start = 0

        index = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk_text = text[start:end]

            chunks.append(

                Chunk(

                    document=document.filename,

                    index=index,

                    text=chunk_text,

                    start=start,

                    end=min(end, len(text))
                )

            )

            index += 1

            start += self.chunk_size - self.overlap

        return chunks