from typing import Final

MAPPING: Final = {
    "a": "⸝",
    "á": "⸝",
    "b": "ˏ",
    "c": "╵",
    "d": "⸍",
    "ð": "ו",
    "e": "ᛁ",
    "é": "ᛁ",
    "f": "ᛙ",
    "g": "ᛍ",
    "h": "ᚽ",
    "i": "ᛁ",
    "í": "ᛁ",
    "j": "ᛁ",
    "k": "ᛍ",
    "l": "⸌",
    "m": "⠃",
    "n": "⸜",
    "o": "ˎ",
    "ó": "ˎ",
    "p": "ˏ",
    "q": "ᛍ",
    "r": "◟",
    "R": "⡄",
    "s": "╵",
    "t": "⸍",
    "þ": "ו",
    "u": "╮",
    "ú": "╮",
    "v": "╮",
    "w": "╮",
    "x": "╵",
    "y": "╮",
    "ý": "╮",
    "z": "╵",
    "å": "ˎ",
    "ä": "⸝",
    "æ": "⸝",
    "ö": "ˎ",
    "ø": "ˎ",
    "ǫ": "ˎ",
    " ": ":",
}


def get_letter_mapping() -> dict[str, str]:
    return MAPPING