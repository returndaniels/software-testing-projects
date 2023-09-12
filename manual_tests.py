#Triang 3
def tipoTriangulo3(a,b,c):
    
    if (a <= 0 and b <= 0 and c <= 0):
        return "invalido"
    
		
    if (a+b >= c and a+c >= b and b+c >= a):
        if (a==b and b == c):
            return "equilatero"
        if (a==b or a==c or b==c):
            return "isosceles"
        return "escaleno"
    return "invalido"

#Triang 7
def tipoTriangulo7(a,b,c):
    
    if (a <= 0 and b <= 0 and c <= 0):
        return "invalido"

    if (a==b and a==c):
        return "equilatero"
    if (a+b > c and a+c > b and b+c > a):
        if (a==b or a==c or b == c):
            return "isosceles"
        return "escaleno"
    return "invalido"



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    
def automated_tester(a: int, b: int, c: int, expected: 'str', func):
    result = None    
    try:
        result = func(a, b, c)
    except:
        result = 'invalido'
            
    return result == expected

# test input
print("Testes para função do arquivo 3")
print("passou: (4, 2, 3) -> 'escaleno" if automated_tester(4, 2, 3, 'escaleno', tipoTriangulo3) else "falhou: (4, 2, 3) -> esperado: 'escaleno'")
print("passou: (4, 4, 2) -> 'isosceles'" if automated_tester(4, 4, 2, 'isosceles', tipoTriangulo3) else "falhou: (4, 4, 2) -> esperado: 'isosceles'")
print("passou: (1, 1, 1) -> 'equilatero'" if automated_tester(1, 1, 1, 'equilatero', tipoTriangulo3) else "falhou: (1, 1, 1) -> esperado: 'equilatero'")
print("passou: (0, 1, 1) -> 'invalido'" if automated_tester(0, 1, 1, 'invalido', tipoTriangulo3) else "falhou: (0, 1, 1) -> esperado: 'invalido'")
print("passou: (1, -1, 3) -> 'invalido'" if automated_tester(1, -1, 3, 'invalido', tipoTriangulo3) else "falhou: (1, -1, 3) -> esperado: 'invalido'")
print("passou: (1, 2, 'três') -> 'invalido'" if automated_tester(1, 2, "três", 'invalido', tipoTriangulo3) else "falhou: (1, 2, 'três') -> esperado: 'invalido'")
print("passou: (2, 1, 1) -> 'invalido'" if automated_tester(2, 1, 1, 'invalido', tipoTriangulo3) else "falhou: (2, 1, 1) -> esperado: 'invalido'")

print('\n')
# test input
print("Testes para função do arquivo 7")
print("passou: (4, 2, 3) -> 'escaleno" if automated_tester(4, 2, 3, 'escaleno', tipoTriangulo7) else "falhou: (4, 2, 3) -> esperado: 'escaleno'")
print("passou: (4, 4, 2) -> 'isosceles'" if automated_tester(4, 4, 2, 'isosceles', tipoTriangulo7) else "falhou: (4, 4, 2) -> esperado: 'isosceles'")
print("passou: (1, 1, 1) -> 'equilatero'" if automated_tester(1, 1, 1, 'equilatero', tipoTriangulo7) else "falhou: (1, 1, 1) -> esperado: 'equilatero'")
print("passou: (0, 1, 1) -> 'invalido'" if automated_tester(0, 1, 1, 'invalido', tipoTriangulo7) else "falhou: (0, 1, 1) -> esperado: 'invalido'")
print("passou: (1, -1, 3) -> invalido" if automated_tester(1, -1, 3, 'invalido', tipoTriangulo7) else "falhou: (1, -1, 3) -> esperado: 'invalido'")
print("passou: (1, 2, 'três') -> 'invalido'" if automated_tester(1, 2, "três", 'invalido', tipoTriangulo7) else "falhou: (1, 2, 'três') -> esperado: 'invalido'")
print("passou: (2, 1, 1) -> 'invalido'" if automated_tester(2, 1, 1, 'invalido', tipoTriangulo7) else "falhou: (2, 1, 1) -> esperado: 'invalido'")