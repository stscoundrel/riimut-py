from src.riimut import futhorc


def test_transforms_letters_to_runes():
    content = "aábcdðeéfghiíïʒjklmnŋoóǫpqrstuúvwxyýzåäæœöøþ "
    expected = "ᚪᚪᛒᚳᛞᛞᛖᛖᚠᚷᚻᛁᛇᛇᛇᛡᚳᛚᛗᚾᛝᚩᚩᚩᛈᚳᚱᛋᛏᚢᚢᚹᚹᛉᚣᚣᛉᚩᚫᚫᛟᛟᛟᚦ:"
    result = futhorc.letters_to_runes(content)

    assert result == expected


def test_transforms_runes_to_letters():
    content = "ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛡᛄᛇᛈᛉᛋᚴᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛠ:"
    expected = "fuþorcgwhnijjïpxsstbemlŋœdaæyea "
    result = futhorc.runes_to_letters(content)

    assert result == expected


def test_transforms_late_west_saxon_to_runes():
    # From 8th century Franks Casket, in late West Saxon.
    content = "fisc.flodu.ahofonferg | enberig |"
    expected = "ᚠᛁᛋᚳ.ᚠᛚᚩᛞᚢ.ᚪᚻᚩᚠᚩᚾᚠᛖᚱᚷ:|:ᛖᚾᛒᛖᚱᛁᚷ:|"
    result = futhorc.letters_to_runes(content)

    assert result == expected


def test_transforms_runes_to_late_west_saxon():
    # From 8th century Franks Casket, in late West Saxon.
    content = "ᚠᛁᛋᚳ.ᚠᛚᚩᛞᚢ.ᚪᚻᚩᚠᚩᚾᚠᛖᚱᚷ:|:ᛖᚾᛒᛖᚱᛁᚷ:|"
    expected = "fisc.flodu.ahofonferg | enberig |"
    result = futhorc.runes_to_letters(content)

    assert result == expected
