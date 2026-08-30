import os
import subprocess
from pathlib import Path


class ApplicationService:
    APPLICATIONS = {
        "chrome": {
            "executable": Path(
                os.environ.get("ProgramFiles", "")
            ) / "Google/Chrome/Application/chrome.exe",
            "process": "chrome.exe",
        },
        "notepad": {
            "executable": Path(
                os.environ.get("WINDIR", "C:/Windows")
            ) / "System32/notepad.exe",
            "process": "notepad.exe",
        },
        "calculator": {
            "executable": Path(
                os.environ.get("WINDIR", "C:/Windows")
            ) / "System32/calc.exe",
            "process": "CalculatorApp.exe",
        },
    }

    def open(self, application: str) -> None:
        config = self.APPLICATIONS.get(application)

        if config is None:
            raise ValueError(
                f"Desteklenmeyen uygulama: {application}"
            )

        executable = config["executable"]

        if not executable.exists():
            raise FileNotFoundError(
                f"Uygulama bulunamadı: {executable}"
            )

        subprocess.Popen([str(executable)])

    def close(self, application: str) -> None:
        config = self.APPLICATIONS.get(application)

        if config is None:
            raise ValueError(
                f"Desteklenmeyen uygulama: {application}"
            )

        process_name = config["process"]

        subprocess.run(
            ["taskkill", "/IM", process_name],
            check=False,
            capture_output=True,
            text=True,
        )