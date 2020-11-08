from typing import List
from src.translate_morse import translate_marks
from src.morse_alphabet import DOT, DOT_SYMBOL, COMMA, COMMA_SYMBOL, PAUSE, PAUSE_SYMBOL


def print_morse(tr_marks: list):
    """method is printing morse alphabet as known marks

    Args:
        tr_marks (list): output list from translate_marks
    """
    separator = " "
    mark_morse: List[str] = []
    for mark in tr_marks:
        if mark == DOT:
            mark_morse += DOT_SYMBOL
        elif mark == COMMA:
            mark_morse += COMMA_SYMBOL
        elif mark == PAUSE:
            mark_morse += PAUSE_SYMBOL

    print(separator.join(mark_morse))


def main(input_text: str) -> None:
    """
    Args:
        input_text (str): input string, that will be translated into the morse code as marks
    """
    tr_marks = translate_marks(input_text)
    print_morse(tr_marks)
    