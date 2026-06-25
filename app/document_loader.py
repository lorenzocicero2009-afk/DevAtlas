from pathlib import Path

from app.config import Config

SUPPORTED_EXTENSIONS = {
    ".txt",
    ".md",
    ".pdf",
    ".html",
    ".htm",
    ".docx",
    ".json",
    ".csv"
}


class DocumentLoader:

    def __init__(self):

        cfg = Config()

        self.dataset = Path(cfg.dataset)

    def scan(self):

        print()
        print("Scanning dataset...")
        print()

        if not self.dataset.exists():
            print("❌ Dataset folder not found!")
            return []

        documents = []

        for file in sorted(self.dataset.rglob("*")):

            if not file.is_file():
                continue

            if file.name in {"README.md", ".gitkeep"}:
                continue

            if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            documents.append(file)

            size = round(file.stat().st_size / 1024, 2)

            print(f"✓ {file} ({size} KB)")

        print()

        print(f"Found {len(documents)} supported documents.")

        return documents
