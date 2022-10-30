import os
import sys
import subprocess
from time import sleep
import platform
if platform.system() == 'Windows':
    import winsound


def MelodyPlayer():
    players = {
        "win32": WinMelodyPlayerImpl,
        "linux": LinuxMelodyPlayerImpl
    }

    try:
        return players[sys.platform]()
    except KeyError:
        raise KeyError(f"Your current platform {sys.platform} is not supported"
                       "please provide your own MelodyPlayer")


class WinMelodyPlayerImpl:

    def play_note(self, freq, duration):
        try:
            winsound.Beep(freq, duration)
        except ValueError:
            print(
                f'Can not play: {freq} will remain silent for {duration} ms')
            sleep(duration / 1000)


class LinuxMelodyPlayerImpl:
    def __init__(self) -> None:
        try:
            devnull = open(os.devnull)
            subprocess.Popen(['sox'], stdout=devnull,
                             stderr=devnull).communicate()
        except FileNotFoundError as e:
            raise OSError("Linux implementation of player depends on 'sox' "
                          "package. Please install it first in your distribution "
                          "or provide your own system dependend player")

    def play_note(self, freq, duration):
        duration = duration / 1000
        subprocess.run(['play', '-n', 'synth', f"{duration}", 'sine', f"{freq}"],
                       stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
