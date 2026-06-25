from app.document_loader import DocumentLoader
from app.document_parser import DocumentParser

loader = DocumentLoader()

parser = DocumentParser()

documents = loader.scan()

print()

for file in documents:

    document = parser.parse(file)

    print("--------------------------------")

    print(document.filename)

    print(document.extension)

    print(document.size)

    print()

    print(document.text[:300])

    print()