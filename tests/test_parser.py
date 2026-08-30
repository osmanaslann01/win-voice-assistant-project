from src.assistant.parser.parser import CommandParser


def test_chrome_command() -> None:
    parser = CommandParser()

    command = parser.parse("chrome aç")

    assert command is not None
    assert command.name == "open_application"
    assert command.arguments["application"] == "chrome"
    