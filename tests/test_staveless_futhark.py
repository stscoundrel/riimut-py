from src.riimut import staveless_futhark


def test_transforms_letters_to_runes():
    content = "aábcdðeéfghiíjklmnoópqrRstþuúvwxyýzåäæœöøǫþ "
    expected = "⸝⸝ˏ╵⸍וᛁᛁᛙᛍᚽᛁᛁᛁᛍ⸌⠃⸜ˎˎˏᛍ◟◟╵⸍ו╮╮╮╮╵╮╮╵ˎ⸝⸝ˎˎˎˎו:"
    result = staveless_futhark.letters_to_runes(content)

    assert result == expected


def test_transforms_runes_to_letters():
    content = "ᛙ╮וˎ⡄ᛍᚽ⸜ᛁ⸝╵⸍ˏ⠃⸌⡄:"
    expected = "fuþoRkhniastbmlR "
    result = staveless_futhark.runes_to_letters(content)

    assert result == expected


def test_transforms_old_norse_to_runes():
    # From Old Norse text in Hög runestone.
    content = "kuþniutr þru sun lit rita stin þina ak bru kirþi aftiʀ bruþr sina asbiurn ak at kuþlaf"
    expected = "ᛍ╮ו⸜ᛁ╮⸍◟:ו◟╮:╵╮⸜:⸌ᛁ⸍:◟ᛁ⸍⸝:╵⸍ᛁ⸜:וᛁ⸜⸝:⸝ᛍ:ˏ◟╮:ᛍᛁ◟וᛁ:⸝ᛙ⸍ᛁʀ:ˏ◟╮ו◟:╵ᛁ⸜⸝:⸝╵ˏᛁ╮◟⸜:⸝ᛍ:⸝⸍:ᛍ╮ו⸌⸝ᛙ"
    result = staveless_futhark.letters_to_runes(content)

    assert result == expected


def test_transforms_runes_to_old_norse():
    # From Old Norse text in Hög runestone.
    content = "ᛍ╮ו⸜ᛁ╮⸍◟:ו◟╮:╵╮⸜:⸌ᛁ⸍:◟ᛁ⸍⸝:╵⸍ᛁ⸜:וᛁ⸜⸝:⸝ᛍ:ˏ◟╮:ᛍᛁ◟וᛁ:⸝ᛙ⸍ᛁʀ:ˏ◟╮ו◟:╵ᛁ⸜⸝:⸝╵ˏᛁ╮◟⸜:⸝ᛍ:⸝⸍:ᛍ╮ו⸌⸝ᛙ"
    expected = "kuþniutr þru sun lit rita stin þina ak bru kirþi aftiʀ bruþr sina asbiurn ak at kuþlaf"
    result = staveless_futhark.runes_to_letters(content)

    assert result == expected
