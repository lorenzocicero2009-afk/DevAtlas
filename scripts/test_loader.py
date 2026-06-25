from app.document_loader import DocumentLoader

loader = DocumentLoader()

documents = loader.scan()

print()

if not documents:

    print("Dataset is empty.")

else:

    print()

    print("Document list:")

    for doc in documents:

        print(f" • {doc}")
