from src.riimut import younger_futhark


def test_default_transforms_letters_to_runes():
    content = "aábcdðeéfghiíjklmnoópqrstþuúvwxyýzåäæœöøǫþ"
    expected = "ᛅᛅᛒᛋᛏᚦᛁᛁᚠᚴᚼᛁᛁᛁᚴᛚᛘᚾᚢᚢᛒᚴᚱᛋᛏᚦᚢᚢᚢᚢᛋᚢᚢᛋᚢᛅᛅᚢᚢᚢᚢᚦ"
    result = younger_futhark.letters_to_runes(content)

    assert result == expected


def test_transforms_letters_to_long_branch_runes():
    content = "aábcdðeéfghiíjklmnoópqrstþuúvwxyýzåäæœöøǫþ"
    expected = "ᛅᛅᛒᛋᛏᚦᛁᛁᚠᚴᚼᛁᛁᛁᚴᛚᛘᚾᚢᚢᛒᚴᚱᛋᛏᚦᚢᚢᚢᚢᛋᚢᚢᛋᚢᛅᛅᚢᚢᚢᚢᚦ"
    result = younger_futhark.letters_to_long_branch_runes(content)

    assert result == expected


def test_transforms_letters_to_short_twig_runes():
    content = "aábcdðeéfghiíjklmnoópqrstþuúvwxyýzåäæœöøǫþ"
    expected = "ᛆᛆᛒᛌᛐᚦᛁᛁᚠᚴᚽᛁᛁᛁᚴᛚᛘᚿᚢᚢᛒᚴᚱᛌᛐᚦᚢᚢᚢᚢᛌᚢᚢᛌᚢᛆᛆᚢᚢᚢᚢᚦ"
    result = younger_futhark.letters_to_short_twig_runes(content)

    assert result == expected


def test_transforms_letters_to_runes_with_given_variant():
    content = "aábcdðeéfghiíjklmnoópqrstþuúvwxyýzåäæœöøǫþ"
    expected_long_branch = "ᛅᛅᛒᛋᛏᚦᛁᛁᚠᚴᚼᛁᛁᛁᚴᛚᛘᚾᚢᚢᛒᚴᚱᛋᛏᚦᚢᚢᚢᚢᛋᚢᚢᛋᚢᛅᛅᚢᚢᚢᚢᚦ"
    expected_short_twig = "ᛆᛆᛒᛌᛐᚦᛁᛁᚠᚴᚽᛁᛁᛁᚴᛚᛘᚿᚢᚢᛒᚴᚱᛌᛐᚦᚢᚢᚢᚢᛌᚢᚢᛌᚢᛆᛆᚢᚢᚢᚢᚦ"

    long_branch_result = younger_futhark.letters_to_runes(
        content, younger_futhark.Variant.LONG_BRANCH
    )
    short_twig_result = younger_futhark.letters_to_runes(
        content, younger_futhark.Variant.SHORT_TWIG
    )

    assert long_branch_result == expected_long_branch
    assert short_twig_result == expected_short_twig


def test_transforms_runes_to_letters():
    long_branch = "ᚠᚢᚦᚬᚱᚴᚼᚽᚾᚿᛁᛅᛆᛋᛌᛏᛐᛒᛘᛚᛦ:"
    short_twig = "ᚠᚢᚦᚬᚱᚴᚽᚽᚿᚿᛁᛆᛆᛌᛌᛐᛐᛒᛘᛚᛦ:"
    expected = "fuþorkhhnniaassttbmlR "

    # Both runesets should produce same letters.
    long_branch_result = younger_futhark.runes_to_letters(long_branch)
    short_twig_result = younger_futhark.runes_to_letters(short_twig)

    assert long_branch_result == expected
    assert short_twig_result == expected


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
