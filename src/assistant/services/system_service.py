import ctypes


class SystemService:
    def lock_computer(self) -> None:
        result = ctypes.windll.user32.LockWorkStation()

        if result == 0:
            raise RuntimeError("Bilgisayar kilitlenemedi.")