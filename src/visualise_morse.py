import time
from gpiozero import LED
from src.morse_alphabet import morse_code, DOT, COMMA, PAUSE

led = LED(17) # gpio input


def translate_marks(input_text: str):
    """method translates the input string into the morse alphabet

    Args:
        input (str): string, that will be translated to morse alphabet

    Returns:
        [list]: list of morse code sequence
    """
    input_text = input_text.lower()
    translated_marks = []
    for letter in input_text:
        if letter in morse_code:
            translated_marks += morse_code.get(letter)
            translated_marks.append(PAUSE)
    return translated_marks


def visualise(tr_marks: list):
    """
    method is turning on/off the led on RPi depending on the morse alphabet

    Args:
        tr_marks ([list]): output list from translate_marks
    """
    unit = 0.25
    for mark in tr_marks:
        if mark == DOT:
            led.on()
            time.sleep(unit)
            led.off()
            time.sleep(unit)
        elif mark == COMMA:
            led.on()
            time.sleep(unit*3)
            led.off()
            time.sleep(unit)
        elif mark == PAUSE:
            led.off()
            time.sleep(unit*2)



def main(input_text: str) -> None:
    """
    Args:
        input_text (str): input string, that will be translated into the morse alphabet
    """
    tr_marks = translate_marks(input_text)
    visualise(tr_marks)
