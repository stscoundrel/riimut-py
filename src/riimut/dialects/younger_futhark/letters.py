from typing import Final

MAPPING: Final = {
    "a": "ᛅ",
    "á": "ᛅ",
    "b": "ᛒ",
    "c": "ᛋ",
    "d": "ᛏ",
    "ð": "ᚦ",
    "e": "ᛁ",
    "é": "ᛁ",
    "f": "ᚠ",
    "g": "ᚴ",
    "h": "ᚼ",
    "i": "ᛁ",
    "í": "ᛁ",
    "j": "ᛁ",
    "k": "ᚴ",
    "l": "ᛚ",
    "m": "ᛘ",
    "n": "ᚾ",
    "o": "ᚢ",
    "ó": "ᚢ",
    "p": "ᛒ",
    "q": "ᚴ",
    "r": "ᚱ",
    "s": "ᛋ",
    "t": "ᛏ",
    "þ": "ᚦ",
    "u": "ᚢ",
    "ú": "ᚢ",
    "v": "ᚢ",
    "w": "ᚢ",
    "x": "ᛋ",
    "y": "ᚢ",
    "ý": "ᚢ",
    "z": "ᛋ",
    "å": "ᚢ",
    "ä": "ᛅ",
    "æ": "ᛅ",
    "ö": "ᚢ",
    "ø": "ᚢ",
    "ǫ": "ᚢ",
    " ": ":",
}


def get_letter_mapping() -> dict[str, str]:
    return MAPPING
