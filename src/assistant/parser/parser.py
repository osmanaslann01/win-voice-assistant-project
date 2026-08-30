from .models import Command


class CommandParser:
    def parse(self, text: str) -> Command | None:
        normalized_text = text.strip().lower()

        if normalized_text in {"chrome'u aç", "chrome aç", "chrome'u başlat"}:
            return Command(
                name="open_application",
                arguments={"application": "chrome"},
            )

        return None

    