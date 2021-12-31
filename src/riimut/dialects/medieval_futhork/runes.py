def get_rune_mapping() -> "dict[str, str]":
    mapping = {
        "ᚠ": "f",
        "ᚢ": "u",
        "ᚦ": "þ",
        "ᚮ": "o",
        "ᚱ": "r",
        "ᚴ": "k",
        "ᚼ": "h",
        "ᚿ": "n",
        "ᛁ": "i",
        "ᛆ": "a",
        "ᛌ": "s",
        "ᛋ": "s",
        "ᛐ": "t",
        "ᛏ": "t",
        "ᛒ": "b",
        "ᛘ": "m",
        "ᛚ": "l",
        "ᛦ": "y",
        ":": " ",

        # Sting diacritic secondary sounds.
        "ᚯ": "ø",
        "ᛅ": "æ",
        "ᚰ": "ǫ",
        "ᛕ": "ᴘ",
        "ᚽ": "e",
        "ᚵ": "g",
    }

    return mapping
