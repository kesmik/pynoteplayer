from time import sleep
from pynoteplayer.MelodyPlayer import MelodyPlayer


class Melody:
    def __init__(self, tempo_bpm, time_signature: dict = {}, player=None) -> None:
        self.whole_note = 60000 * \
            time_signature.get('beat-type', 4) / tempo_bpm
        if player == None:
            self.note_player = MelodyPlayer()
        else:
            self.note_player = player()

    def play(self):
        for note in self.notes:
            duration_ms = int(note.dur_coef * self.whole_note)
            if note.freq > 0:
                self.note_player.play_note(note.freq, duration_ms)
            else:
                sleep(duration_ms / 1000)
