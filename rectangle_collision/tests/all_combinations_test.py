# from colisao_original import colisao
# from colisao_corrigido import colisao
from colisao_melhor import colisao

from pytest import *


# CT1. Vértice comum existe (VC), algum vértice do 1° retângulo dentro do 2° (VD) e Vértice possui interseção com a reta (VI)
def test_ac_vc_vd_vi():
    assert colisao(1, 1, 3, 3, 1, 1, 4, 4) is 1


# CT2. Vértice comum existe (VC), Algum vértice do 1° retângulo dentro do 2° (VD) e Vértice abaixo da reta (VB)
def test_ac_vc_vd_vb():
    assert colisao(1, 1, 3, 3, 0, 0, 3, 3) is 1


# CT3: Vértice comum existe (VC), Nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice acima da reta (VA)
def test_ac_vc_vnd_va():
    assert colisao(0, 0, 3, 3, 1, 1, 3, 3) is 1


# CT4: Vértice comum existe (VC), Nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice possui interseção com a reta (VI)
def test_ac_vc_vnd_vi():
    assert colisao(0, 1, 3, 3, 1, 1, 3, 3) is 1


# CT5: Vértice comum existe (VC), Nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice abaixo da reta (VB):
def test_ac_vc_vnd_vb():
    assert colisao(0, 1, 3, 3, 1, 0, 3, 3) is 1


# CT6. Vértice comum não existe (VNC), algum vértice do 1° retângulo dentro do 2° (VD) e Vértice acima da reta (VA)
def test_ac_vnc_vd_va():
    assert colisao(0, 0, 2, 2, 1, 1, 4, 4) is 1


# CT7. Vértice comum não existe (VNC), algum vértice do 1° retângulo dentro do 2° (VD) e Vértice possui interseção com a reta (VI)
def test_ac_vnc_vd_vi():
    assert colisao(0, 0, 2, 2, 1, 0, 4, 4) is 1


# CT8. Vértice comum não existe (VNC), algum vértice do 1° retângulo dentro do 2° (VD) e Vértice abaixo da reta (VB)
def test_ac_vnc_vd_vb():
    assert colisao(0, 1, 2, 2, 1, 0, 4, 4) is 1


# CT9. Vértice comum não existe (VNC), nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice acima da reta (VA)
def test_ac_vnc_vnd_va():
    assert colisao(0, 1, 2, 2, 1, 3, 4, 4) is 0


# CT10. Vértice comum não existe (VNC), nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice possui interseção com a reta (VI)
def test_ac_vnc_vnd_vi():
    assert colisao(0, 1, 2, 2, 3, 1, 4, 4) is 0


# CT11. Vértice comum não existe (VNC), nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice abaixo da reta (VB)
def test_ac_vnc_vnd_vb():
    assert colisao(0, 1, 2, 2, 3, 0, 4, 4) is 0
