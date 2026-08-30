from src.assistant.commands.executor import CommandExecutor
from src.assistant.parser.parser import CommandParser


class Assistant:
    def __init__(
        self,
        parser: CommandParser | None = None,
        executor: CommandExecutor | None = None,
    ) -> None:
        self.parser = parser or CommandParser()
        self.executor = executor or CommandExecutor()

    def process(self, text: str) -> None:
        command = self.parser.parse(text)

        if command is None:
            print("Komut anlaşılamadı.")
            return

        try:
            self.executor.execute(command)
        except Exception as exc:
            print(f"Komut çalıştırılırken hata oluştu: {exc}")
            