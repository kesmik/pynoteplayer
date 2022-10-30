from pynoteplayer.Melody import Melody
from pynoteplayer.Note import Note


class HappyBirthday(Melody):
    def __init__(self, player=None) -> None:
        self.tempo_bpm = 125
        self.time_signature = {
            'beats': 3,
            'beat-type': 4
        }
        super().__init__(self.tempo_bpm, self.time_signature, player)

        self.notes = [
            Note('C4', 4), Note('C4', 8),
            Note('D4', 4, 1), Note('C4', 4, 1), Note('F4', 4, 1),
            Note('E4', 2, 1), Note('C4', 4), Note('C4', 8),
            Note('D4', 4, 1), Note('C4', 4, 1), Note('G4', 4, 1),
            Note('F4', 2, 1), Note('C4', 4), Note('C4', 8),
            Note('C5', 4, 1), Note('A4', 4, 1), Note('F4', 4, 1),
            Note('E4', 4, 1), Note('D4', 4, 1), Note('As4', 4), Note('As4', 8),
            Note('A4', 4, 1), Note('F4', 4, 1), Note('G4', 4, 1),
            Note('F4', 2, 1)
        ]
