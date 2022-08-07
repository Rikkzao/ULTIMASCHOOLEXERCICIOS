import pytest
def desconto():
        quantidade = 50
        desconto = 1

        if quantidade >= 10 and quantidade <= 99:
            return desconto - 0.05
        else:
            return None


def teste():
    assert desconto() == 0.95


def desconto2():
        quantidade = 150
        desconto = 1

        if quantidade >= 100 and quantidade <= 999:
            return desconto - 0.1
        else:
            return None


def teste2():
    assert desconto2() == 0.9

def desconto3():
        quantidade = 1500
        desconto = 1

        if quantidade >= 1000:
            return desconto - 0.15
        else:
            return None


def teste3():
    assert desconto3() == 0.85