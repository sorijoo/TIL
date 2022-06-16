import fibo


def test_first_two_seqs_should_be_1():
    assert fibo.fibo(0) == fibo.fibo(1) == 1


def test_3rd_should_be_2():
    assert fibo.fibo(2) == 2


def test_4th_should_be_3():
    assert fibo.fibo(3) == 3


def test_5th_should_be_5():
    assert fibo.fibo(4) == 5
