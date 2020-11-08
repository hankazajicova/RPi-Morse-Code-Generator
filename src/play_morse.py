from pydub import AudioSegment
from pydub.playback import play
from src.morse_alphabet import DOT, COMMA, PAUSE
from src.translate_morse import translate_marks

sound = AudioSegment.from_mp3('src/1khz.mp3')
silence = AudioSegment.silent(duration=250)


def play_morse(tr_marks: list):
    """method is playing morse code sounds depending on the input

    Args:
        tr_marks (list): output list from translate_marks
    """
    play_morse_code = silence
    for mark in tr_marks:
        if mark == DOT:
            play_morse_code += sound
            play_morse_code += silence
        elif mark == COMMA:
            play_morse_code += sound
            play_morse_code += sound
            play_morse_code += sound
            play_morse_code += silence
        elif mark == PAUSE:
            play_morse_code += silence
            play_morse_code += silence

    play(play_morse_code)


def main(input_text: str) -> None:
    """
    Args:
        input_text (str): input string, that will be translated into the sound morse alphabet
    """
    tr_marks = translate_marks(input_text)
    play_morse(tr_marks)
