from src.riimut import elder_futhark


def test_transforms_letters_to_runes():
    content = "aábcdðeéfghiíjklmnŋoópqrstþuúvwxyýzåäæœöøǫþ"
    expected = "ᚨᚨᛒᚲᛞᚦᛖᛖᚠᚷᚻᛁᛁᛃᚲᛚᛗᚾᛜᛟᛟᛈᚲᚱᛋᛏᚦᚢᚢᚹᚹᛋᛁᛁᛉᛟᛇᛇᛟᚢᚢᛟᚦ"
    result = elder_futhark.letters_to_runes(content)

    assert result == expected


def test_transforms_runes_to_letters():
    content = "ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚻᚾᛁᛃᛇᛈᛉᛊᛋᛏᛒᛖᛗᛚᛜᛝᛟᛞ:"
    expected = "fuþarkgwhhnijïpzsstbemlŋŋod "
    result = elder_futhark.runes_to_letters(content)

    assert result == expected


def test_transforms_proto_norse_to_runes():
    # From 4th century axe in Jutland
    content = "wagagastiz alu wihgu sikijaz aiþalataz"
    expected = "ᚹᚨᚷᚨᚷᚨᛋᛏᛁᛉ:ᚨᛚᚢ:ᚹᛁᚻᚷᚢ:ᛋᛁᚲᛁᛃᚨᛉ:ᚨᛁᚦᚨᛚᚨᛏᚨᛉ"
    result = elder_futhark.letters_to_runes(content)

    assert result == expected


def test_transforms_runes_to_proto_norse():
    # From 4th century axe in Jutland
    content = "ᚹᚨᚷᚨᚷᚨᛋᛏᛁᛉ:ᚨᛚᚢ:ᚹᛁᚻᚷᚢ:ᛋᛁᚲᛁᛃᚨᛉ:ᚨᛁᚦᚨᛚᚨᛏᚨᛉ"
    expected = "wagagastiz alu wihgu sikijaz aiþalataz"
    result = elder_futhark.runes_to_letters(content)

    assert result == expected
