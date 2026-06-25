from app.document_loader import DocumentLoader
from app.document_parser import DocumentParser
from app.chunker import Chunker


loader = DocumentLoader()

parser = DocumentParser()

chunker = Chunker()

documents = loader.scan()

for file in documents:

    document = parser.parse(file)

    chunks = chunker.chunk(document)

    print()

    print(document.filename)

    print(f"Chunks: {len(chunks)}")

    print()

    for chunk in chunks:

        print("------------------------")

        print(f"Chunk {chunk.index}")

        print(f"{chunk.start} -> {chunk.end}")

        print()

        print(chunk.text)

        print()