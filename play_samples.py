import os
import sys
import inspect
from pynoteplayer.Melody import Melody

# the code bellow is used to load all the melodies from sample folder dinamically
# it is not the prettiest one, but allows to add songs dinmically

for module in os.listdir(os.path.join('sample_melodies')):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__('sample_melodies.' + module[:-3], locals(), globals())
    del module

if __name__ == "__main__":

    sample_songs = [s for s in inspect.getmembers(
        sys.modules['sample_melodies']) if not s[0].startswith('__')]

    for name, mod in sample_songs:
        classes = [(cls_name, cls_obj) for cls_name, cls_obj in inspect.getmembers(
            sys.modules['sample_melodies.' + name]) if inspect.isclass(cls_obj) and
            issubclass(cls_obj, Melody) and inspect.getmro(cls_obj)[0] != Melody]

        for melody_name, melody_cls in classes:
            if input(f'Do you want to play {melody_name}? [Y/n]: ').lower() != 'n':
                try:
                    melody_cls().play()
                except KeyboardInterrupt:
                    continue
