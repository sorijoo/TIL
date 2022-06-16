from pascalize import pascalize


def test_empty_string():
    assert pascalize('') == ''


def test_single_letter():
    assert pascalize('h') == 'H'


def test_single_word():
    assert pascalize('hey') == 'Hey'


def test_two_words():
    assert pascalize('hey_you') == 'HeyYou'


def test_many_words():
    assert pascalize('hey_you_there') == 'HeyYouThere'
