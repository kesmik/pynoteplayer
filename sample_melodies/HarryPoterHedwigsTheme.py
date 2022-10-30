from pynoteplayer.Melody import Melody
from pynoteplayer.Note import Note


class HarryPoterHedwigsTheme(Melody):
    def __init__(self, player=None) -> None:
        self.tempo_bpm = 144
        self.time_signature = {
            'beats': 3,
            'beat-type': 4
        }
        super().__init__(self.tempo_bpm, self.time_signature, player)

        self.notes = [
            Note('REST', 2), Note('D4', 4),
            Note('G4', 4, 1), Note('As4', 8), Note('A4', 4),
            Note('G4', 2), Note('D5', 4),
            Note('C5', 2, 1),
            Note('A4', 2, 1),
            Note('G4', 4, 1), Note('As4', 8), Note('A4', 4),
            Note('F4', 2), Note('Gs4', 4),
            Note('D4', 1, 1),
            Note('D4', 4),

            Note('G4', 4, 1), Note('As4', 8), Note('A4', 4),
            Note('G4', 2), Note('D5', 4),
            Note('F5', 2), Note('E5', 4),
            Note('Ds5', 2), Note('B4', 4),
            Note('Ds5', 4, 1), Note('D5', 8), Note('Cs5', 4),
            Note('Cs4', 2), Note('B4', 4),
            Note('G4', 1, 1),
            Note('As4', 4),

            Note('D5', 2), Note('As4', 4),
            Note('D5', 2), Note('As4', 4),
            Note('Ds5', 2), Note('D5', 4),
            Note('Cs5', 2), Note('A4', 4),
            Note('As4', 4, 1), Note('D5', 8), Note('Cs5', 4),
            Note('Cs4', 2), Note('D4', 4),
            Note('D5', 1, 1),
            Note('REST', 4), Note('As4', 4),

            Note('D5', 2), Note('As4', 4),
            Note('D5', 2), Note('As4', 4),
            Note('F5', 2), Note('E5', 4),
            Note('Ds5', 2), Note('B4', 4),
            Note('Ds5', 4, 1), Note('D5', 8), Note('Cs5', 4),
            Note('Cs4', 2), Note('As4', 4),
            Note('G4', 1, 1)
        ]
