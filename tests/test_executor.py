from unittest.mock import patch

from src.assistant.commands.executor import CommandExecutor
from src.assistant.parser.models import Command


def test_open_application_command() -> None:
    executor = CommandExecutor()

    command = Command(
        name="open_application",
        arguments={"application": "chrome"},
    )

    with patch.object(executor.application_service, "open") as mock_open:
        executor.execute(command)

    mock_open.assert_called_once_with("chrome")


def test_unknown_command() -> None:
    executor = CommandExecutor()

    command = Command(
        name="unknown",
        arguments={},
    )

    try:
        executor.execute(command)
    except ValueError:
        return

    raise AssertionError("Unknown command should raise ValueError")

