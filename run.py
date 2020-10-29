#!/usr/bin/python3
import sys
from src.visualise_morse import main


if __name__ == "__main__":
    INPUT_TEXT = ' '.join(sys.argv[1:])
    main(INPUT_TEXT)
