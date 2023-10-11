# from colisao_original import colisao
# from colisao_corrigido import colisao
from colisao_melhor import colisao

from pytest import *


# CT1. Vértice comum existe (VC), algum vértice do 1° retângulo dentro do 2° (VD) e Vértice abaixo da reta (VB)
def test_pw_vc_vd_vb():
    assert colisao(2, 2, 4, 4, 1, 1, 4, 4) is 1


# CT2. Vértice comum existe (VC), nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice possui interseção com a reta (VI)
def test_pw_vc_vnd_vi():
    assert colisao(2, 2, 4, 4, 1, 2, 4, 4) is 1


# CT3. Vértice comum não existe (VNC), nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice abaixo da reta (VB)
def test_pw_vnc_vnd_vb():
    assert colisao(1, 1, 2, 2, 3, 0, 4, 4) is 0


# CT4. Vértice comum não existe (VNC), algum vértice do 1° retângulo dentro do 2° (VD) e Vértice possui interseção com a reta (VI)
def test_pw_vnc_vd_vi():
    assert colisao(1, 1, 3, 3, 2, 1, 5, 5) is 1


# CT5. Vértice comum não existe (VNC), nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice acima da reta (VA)
def test_pw_vnc_vnd_va():
    assert colisao(1, 1, 3, 3, 4, 2, 5, 4) is 0
