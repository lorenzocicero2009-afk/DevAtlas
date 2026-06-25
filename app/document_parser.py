from pathlib import Path

from app.document import Document


class DocumentParser:

    def parse(self, path: Path) -> Document:

        extension = path.suffix.lower()

        text = ""

        if extension in [".txt", ".md"]:

            text = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

        return Document(

            filepath=str(path),

            filename=path.name,

            extension=extension,

            size=path.stat().st_size,

            text=text,

            metadata={}
        )