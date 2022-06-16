import hello


def test_hello_to_no_one():
    actual = hello.hello([])
    expected = 'Hello World!'
    assert actual == expected


def test_hello_to_one_person():
    actual = hello.hello(['Alan'])
    expected = 'Hello Alan!'
    assert actual == expected


def test_hello_to_two_people():
    actual = hello.hello(['Alan', 'Brad'])
    expected = 'Hello Alan and Brad!'
    assert actual == expected


def test_hello_to_three_or_more_people():
    actual = hello.hello(['Alan', 'Brad', 'Cate', 'Dave'])
    expected = 'Hello Alan, Brad, Cate and Dave!'
    assert actual == expected
