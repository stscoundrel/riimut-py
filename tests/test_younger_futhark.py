from src.riimut import younger_futhark


def test_transforms_letters_to_runes():
    content = "aábcdðeéfghiíjklmnoópqrstþuúvwxyýzåäæöøǫþ"
    expected = "ᛅᛅᛒᛋᛏᚦᛁᛁᚠᚴᚼᛁᛁᛁᚴᛚᛘᚾᚢᚢᛒᚴᚱᛋᛏᚦᚢᚢᚢᚢᛋᚢᚢᛋᚢᛅᛅᚢᚢᚢᚦ"
    result = younger_futhark.letters_to_runes(content)

    assert result == expected


def test_transforms_runes_to_letters():
    content = "ᚠᚢᚦᚬᚱᚴᚼᚽᚾᚿᛁᛅᛆᛋᛌᛏᛐᛒᛘᛚᛦ:"
    expected = "fuþorkhhnniaassttbmlR "
    result = younger_futhark.runes_to_letters(content)

    assert result == expected


def test_transforms_old_norse_to_runes():
    # From Old Groms runestone.
    content = "auk tani karþi kristna"
    expected = "ᛅᚢᚴ:ᛏᛅᚾᛁ:ᚴᛅᚱᚦᛁ:ᚴᚱᛁᛋᛏᚾᛅ"
    result = younger_futhark.letters_to_runes(content)

    assert result == expected


def test_transforms_runes_to_old_norse():
    # From Old Groms runestone.
    content = "ᛅᚢᚴ:ᛏᛅᚾᛁ:ᚴᛅᚱᚦᛁ:ᚴᚱᛁᛋᛏᚾᛅ"
    expected = "auk tani karþi kristna"
    result = younger_futhark.runes_to_letters(content)

    assert result == expected
