# pynoteplayer

`pynoteplayer` is a primitive player which allows to play simple tones.
The initial idea was to allow play simple tones on a buzzer on a raspberrypi or
similar boards, but it is also available to be run on windows and linux for
melody test or other purposes.

Windows default player relies on `winsound` python module module, while default
Linux implementation uses [SoX](https://sox.sourceforge.net) tool, which needs
to be installed on your system. Since linux implementation uses subprocess it
may not be perfectly accurate in timing.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install
pynoteplayer.

```bash
pip install TODO:[PROVIDE URL HERE, or PyPi]
```

## Usage

To create a melody please follow sample melodies example.

```python
from pynoteplayer.Melody import Melody
from pynoteplayer.Note import Note


class HappyBirthday(Melody):
    def __init__(self, player=None) -> None:
        # tempo (beats per minute) sets melody speed
        self.tempo_bpm = 125
        # time signature used together with tempo (actually 'beat-type' only).
        # It shows which note is used for tempo
        self.time_signature = {
            'beats': 3,
            'beat-type': 4
        }
        super().__init__(self.tempo_bpm, self.time_signature, player)

        # melody itself
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

HappyBirthday().play()
# or
HappyBirthday(YourPlayer()).play()

```

Note class supports octaves from 'C0' (~16 Hz) to 'B8' (~7902 Hz), also 'REST'
for silent.

First parameter indicates note and octave(freq), second note type
(1 means full note, 4 means quarter note etc.), third one - dot,
which prolongs note accordingly.

Use lowercase `s` for sharp. Flats are not added to Note notation.

```python
Note(note, note_type: int, dot=0)

#EXAMPLES:
Note('D4', 4) - Quarter D4
Note('Cs4', 8) - Eighth Cs4 (C sharp)
Note('D4', 4, 1)
Note('Cs4', 4, 2)
```

Supported parameters:
```python
# note
'C0' - 'B8', 'REST'

# note_type
supported_notes = [1, 2, 4, 8, 16, 32, 64]

# dot
duration_map = {
        1: 1.5,
        2: 1.75,
        3: 1.875,
        4: 1.9375
    }
```

If you would like to implement your own player please provide a class which
implements `play_note` method. `play_note` should expect frequency (Hz) and
duration (ms) arguments

```python
# Windows player implementation
class WinMelodyPlayerImpl:

    def play_note(self, freq_hz, duration_ms):
        try:
            winsound.Beep(freq, duration)
        except ValueError:
            print(
                f'Can not play: {freq} will remain silent for {duration} ms')
            sleep(duration / 1000)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)