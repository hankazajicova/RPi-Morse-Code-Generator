#!/usr/bin/python3
import sys
from src.visualise_morse import main as visual
from src.play_morse import main as sound
from src.print_morse import main as printed

PRINT_TEXT = "print"
SOUND_TEXT = "play"
VISUAL_TEXT = "blink"


if __name__ == "__main__":
    """
    python3 run.py <method> <text you want to translate>

    <method> - print, play, blink

    multiple methods can't be used
    """
    INPUT_TEXT = " ".join(sys.argv[2:])
    method: str = sys.argv[1:2][0]
    print(method)
    if method == SOUND_TEXT:
        sound(INPUT_TEXT)
    elif method == VISUAL_TEXT:
        visual(INPUT_TEXT)
    else:
        printed(INPUT_TEXT)
    