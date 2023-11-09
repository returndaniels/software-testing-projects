import pytest
from banco import banco


def test_C1():
    C = 2
    N = 1
    tempos = [(0, 10)]
    assert banco(C, N, tempos) == 0


def test_C2():
    C = 1
    N = 1
    tempos = [(0, 10)]
    assert banco(C, N, tempos) == 0


def test_C4():
    C = 2
    N = 3
    tempos = [(0, 20), (11, 20), (21, 30)]
    assert banco(C, N, tempos) == 0


def test_C5():
    C = 2
    N = 4
    tempos = [(0, 10), (11, 20), (21, 30), (0, 10)]
    assert banco(C, N, tempos) == 1


def test_C6():
    C = 2
    N = 3
    tempos = [(0, 30), (11, 40), (21, 60)]
    assert banco(C, N, tempos) == 0


def test_C7():
    C = 2
    N = 4
    tempos = [(0, 20), (11, 40), (21, 30), (52, 60)]
    assert banco(C, N, tempos) == 0


def test_C8():
    C = 0
    N = 2
    tempos = [(11, 4), (21, 60)]
    with pytest.raises(Exception):
        banco(C, N, tempos)


def test_mutant_7():
    C = 2
    N = 3
    tempos = [
        (15, 20),
        (5, 20),
        (5, 20),
    ]
    assert banco(C, N, tempos) == 1


def test_mutant_17():
    C = 2
    N = 3
    tempos = [(0, 20), (0, 40), (0, 30)]
    assert banco(C, N, tempos) == 1


def test_mutant_36():
    C = 1
    N = 3
    tempos = [(15, 30), (15, 38), (23, 40)]
    assert banco(C, N, tempos) == 2
