# RPi-Morse-Code-Generator

- Morse code translator for Raspberry Pi

- Run with:

    ```bash
    ./run.py <method> <text you want to generate to morse code>
    ```

    method - print, play, blink (multiple methods can't be used)

- debugged with Python extension for Visual Studio Code
- cleaned with pylint and mypy using:

    ```bash
    pylint *.py **/*.py
    mypy *.py **/*.py
    ```

- disabled missing-module-docstring and pointless-string-statement in .pylintrc

## Doveloped for

- Raspberry Pi 1 with GPIO led diod
- led diod switched in 17 GPIO pin
- for sound used JBL Charge 3 (forced 3.5mm jack - sudo raspi-config - Advanced Options - Audio)

![board_scheme](https://user-images.githubusercontent.com/11961745/97628559-274adc00-1a2d-11eb-924b-f3551e7d5edc.png)

## Links

[International Morse Code](https://morsecode.world/international/morse2.html)

[RaspberryPi](https://www.raspberrypi.org/)
