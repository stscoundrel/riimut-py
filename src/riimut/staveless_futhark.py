from .transform import _transform
from .dialects.staveless_futhark.letters import get_letter_mapping
from .dialects.staveless_futhark.runes import get_rune_mapping


def letters_to_runes(content: str) -> str:
    mapping = get_letter_mapping()
    return _transform(content, mapping)


def runes_to_letters(content: str) -> str:
    mapping = get_rune_mapping()
    return _transform(content, mapping)
