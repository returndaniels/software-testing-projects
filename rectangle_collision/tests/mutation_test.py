from colisao_melhor import colisao
from pytest import *


def test_mutation_1():
    assert colisao(1, 1, 2, 2, 0, 0, 1, 2) is 1


def test_mutation_2():
    assert colisao(1, 1, 2, 2, 2, 1, 4, 3) is 1


def test_mutation_3():
    assert colisao(0, 1, 2, 2, 0, 0, 2, 1) is 1


def test_mutation_4():
    assert colisao(1, 1, 2, 2, 2, 2, 5, 4) is 1
