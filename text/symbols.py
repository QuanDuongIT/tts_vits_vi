import piper_phonemize
from piper_phonemize import *


def All_method():
    print(dir(piper_phonemize))

def symbols():
    print(''.join(get_espeak_map()))

symbols = ''.join(get_espeak_map())

# Special symbol ids
SPACE_ID = symbols.index(" ")
