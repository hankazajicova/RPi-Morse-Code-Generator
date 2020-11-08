from typing import List
from src.morse_alphabet import morse_code, PAUSE

def translate_marks(input_text: str):
    """method translates the input string into the morse alphabet

    Args:
        input (str): string, that will be translated to morse alphabet

    Returns:
        [list]: list of morse code sequence
    """
    input_text = input_text.lower()
    translated_marks: List[str] = []
    for letter in input_text:
        if letter in morse_code:
            translated_marks += morse_code[letter]
            translated_marks.append(PAUSE)
    return translated_marks
    