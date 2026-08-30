from src.assistant.parser.models import Command
from src.assistant.services.application_service import ApplicationService
from src.assistant.services.audio_service import AudioService
from src.assistant.services.system_service import SystemService

class CommandExecutor:
    def __init__(
        self,
        application_service: ApplicationService | None = None,
        audio_service: AudioService | None = None,
        system_service: SystemService | None = None,
    ) -> None:
        self.application_service = (
            application_service
            if application_service is not None
            else ApplicationService()
        )

        self.audio_service = (
            audio_service
            if audio_service is not None
            else AudioService()
        )

        self.system_service = (
        system_service
        if system_service is not None
        else SystemService()
        )

    def execute(self, command: Command) -> None:
        if command.name == "open_application":
            self._open_application(command)

        elif command.name == "close_application":
            self._close_application(command)

        elif command.name == "increase_volume":
            self._increase_volume()

        elif command.name == "decrease_volume":
            self._decrease_volume()

        elif command.name == "lock_computer":
            self._lock_computer()

        else:
            raise ValueError(f"Unknown command: {command.name}")

    def _open_application(self, command: Command) -> None:
        application = command.arguments["application"]
        self.application_service.open(application)

    def _close_application(self, command: Command) -> None:
        application = command.arguments["application"]
        self.application_service.close(application)

    def _increase_volume(self) -> None:
        self.audio_service.increase()

    def _decrease_volume(self) -> None:
        self.audio_service.decrease()

    def _lock_computer(self) -> None:
        self.system_service.lock_computer()