from pycaw.pycaw import AudioUtilities


class AudioService:
    def __init__(self) -> None:
        devices = AudioUtilities.GetSpeakers()
        self.volume = devices.EndpointVolume

    def increase(self, amount: float = 0.05) -> None:
        current = self.volume.GetMasterVolumeLevelScalar()
        new_volume = min(1.0, current + amount)
        self.volume.SetMasterVolumeLevelScalar(new_volume, None)

    def decrease(self, amount: float = 0.05) -> None:
        current = self.volume.GetMasterVolumeLevelScalar()
        new_volume = max(0.0, current - amount)
        self.volume.SetMasterVolumeLevelScalar(new_volume, None)