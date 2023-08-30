from pytest import *

#Triang 8
def tipoTriangulo8(a,b,c):

    lados = [a,b,c]
    
    valido = False
    
    for lado in lados:
        aux = lados.copy()
        aux.remove(lado)
        
        if lado > abs(aux[0] - aux[1]) and lado < aux[0] + aux[1]:
            valido = True
            break
            
    if not(valido) or (a <= 0 or b <= 0 or c <= 0):
        return "invalido"
    
    if a == b and b == c and a == c:
        return "equilatero"
    if a == b or b == c or a == c:
        return "isosceles"
    return "escaleno"



# Testes para a função tipoTriangulo8
def test_tipoTriangulo8_escaleno():
    assert tipoTriangulo8(4, 2, 3) == "escaleno"

def test_tipoTriangulo8_isosceles():
    assert tipoTriangulo8(4, 4, 2) == "isosceles"

def test_tipoTriangulo8_equilatero():
    assert tipoTriangulo8(1, 1, 1) == "equilatero"

def test_tipoTriangulo8_invalido():
    assert tipoTriangulo8(0, 1, 1) == "invalido"

def test_tipoTriangulo8_invalido():
    assert tipoTriangulo8(1, -1, 3) == "invalido"

def test_tipoTriangulo8_invalido():
    assert tipoTriangulo8(1, 2, "três") == "invalido"

def test_tipoTriangulo8_invalido():
    assert tipoTriangulo8(2, 1, 1) == "invalido"