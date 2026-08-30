from src.assistant.parser.parser import CommandParser


def test_chrome_command() -> None:
    parser = CommandParser()

    command = parser.parse("chrome aç")

    assert command is not None
    assert command.name == "open_application"
    assert command.arguments["application"] == "chrome"


def test_unknown_command() -> None:
    parser = CommandParser()

    command = parser.parse("merhaba")

    assert command is None


def test_close_chrome_command() -> None:
    parser = CommandParser()

    command = parser.parse("chrome kapat")

    assert command is not None
    assert command.name == "close_application"
    assert command.arguments["application"] == "chrome"


def test_increase_volume_command() -> None:
    parser = CommandParser()

    command = parser.parse("sesi aç")

    assert command is not None
    assert command.name == "increase_volume"


def test_decrease_volume_command() -> None:
    parser = CommandParser()

    command = parser.parse("sesi kıs")

    assert command is not None
    assert command.name == "decrease_volume"


def test_lock_computer_command() -> None:
    parser = CommandParser()

    command = parser.parse("bilgisayarı kilitle")

    assert command is not None
    assert command.name == "lock_computer"
    