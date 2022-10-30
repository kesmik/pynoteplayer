from pynoteplayer.Note import Note
from pynoteplayer.Melody import Melody


class SamsungNotification(Melody):
    def __init__(self, player=None) -> None:
        self.tempo_bpm = 290
        self.time_signature = {
            'beats': 4,
            'beat-type': 4
        }
        super().__init__(self.tempo_bpm, self.time_signature, player)

        self.notes = [
            Note('B4', 4), Note('Ds5', 4), Note('B5', 4),
            Note('As5', 8), Note('REST', 8), Note('REST', 8),
            Note('REST', 4), Note('Fs5', 8), Note('REST ', 8),
        ]
