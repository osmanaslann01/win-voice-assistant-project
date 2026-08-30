from .models import Command


class CommandParser:
    def parse(self, text: str) -> Command | None:
        normalized_text = text.strip().lower()

        # Uygulama açma
        if normalized_text in {
            "chrome aç",
            "chrome'u aç",
            "chrome'u başlat",
            "google chrome aç",
        }:
            return Command(
                name="open_application",
                arguments={"application": "chrome"},
            )

        # Uygulama kapatma
        if normalized_text in {
            "chrome kapat",
            "chrome'u kapat",
            "chrome'u kapatır mısın",
        }:
            return Command(
                name="close_application",
                arguments={"application": "chrome"},
            )

        # Ses seviyesi
        if normalized_text in {
            "sesi aç",
            "ses seviyesini artır",
            "sesi yükselt",
        }:
            return Command(
                name="increase_volume",
                arguments={},
            )

        if normalized_text in {
            "sesi kıs",
            "ses seviyesini azalt",
            "sesi düşür",
        }:
            return Command(
                name="decrease_volume",
                arguments={},
            )

        # Sistem
        if normalized_text in {
            "bilgisayarı kilitle",
            "bilgisayarı kilitle",
            "ekranı kilitle",
        }:
            return Command(
                name="lock_computer",
                arguments={},
            )

        return None

    