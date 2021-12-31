from src.riimut import medieval_futhork


def test_transforms_letters_to_runes():
    content = "aábcdðeéfghiíjklmnoóǫpqrstuúvwxyýzåäæœöøþ "
    expected = "ᛆᛆᛒᚴᚦᚦᚽᚽᚠᚵᚼᛁᛁᛁᚴᛚᛘᚿᚮᚮᚰᛕᚴᚱᛋᛏᚢᚢᚠᚠᛋᛦᛦᛋᚮᛅᛅᚯᚯᚯᚦ:"
    result = medieval_futhork.letters_to_runes(content)

    assert result == expected


def test_transforms_runes_to_letters():
    content = "ᚠᚢᚦᚮᚱᚴᚼᚿᛁᛆᛌᛋᛐᛏᛒᛘᛚᛦᚯᛅᚰᛕᚽ:"
    expected = "fuþorkhniassttbmlyøæǫᴘe "
    result = medieval_futhork.runes_to_letters(content)

    assert result == expected


def test_transforms_later_old_norse_to_runes():
     # From Lord's Prayer, in Old Norse.
    content = "Faðer uor som ast i himlüm, halgað warðe þit nama"
    expected = "ᚠᛆᚦᚽᚱ:ᚢᚮᚱ:ᛋᚮᛘ:ᛆᛋᛏ:ᛁ:ᚼᛁᛘᛚᚢᛘ,:ᚼᛆᛚᚵᛆᚦ:ᚠᛆᚱᚦᚽ:ᚦᛁᛏ:ᚿᛆᛘᛆ"
    result = medieval_futhork.letters_to_runes(content)

    assert result == expected


def test_transforms_runes_to_later_old_norse():
    # From Lord's Prayer, in Old Norse.
    content = "ᚠᛆᚦᚽᚱ:ᚢᚮᚱ:ᛋᚮᛘ:ᛆᛋᛏ:ᛁ:ᚼᛁᛘᛚᚢᛘ:ᚼᛆᛚᚵᛆᚦ:ᚠᛆᚱᚦᚽ:ᚦᛁᛏ:ᚿᛆᛘᛆ"
    expected = "faþer uor som ast i himlum halgaþ farþe þit nama" # Wont tell apart eth & thorn in mid sentence.
    result = medieval_futhork.runes_to_letters(content)

    assert result == expected
