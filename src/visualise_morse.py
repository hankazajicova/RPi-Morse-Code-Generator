import time
from gpiozero import LED
from src.morse_alphabet import DOT, COMMA, PAUSE
from src.translate_morse import translate_marks

led = LED(17) # gpio input


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
        input_text (str): input string, that will be translated into the visual morse alphabet
    """
    tr_marks = translate_marks(input_text)
    visualise(tr_marks)
