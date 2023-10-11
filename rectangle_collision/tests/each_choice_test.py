# from colisao_original import colisao
# from colisao_corrigido import colisao
from colisao_melhor import colisao
from pytest import *


# CT1. Vértice comum existe (VC) e nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice acima da reta (VA)
def test_ec_vc_vnd_va():
    assert colisao(0, 0, 2, 2, 1, 1, 2, 2) is 1


# CT2. Vértice comum não existe (VNC) e nenhum vértice do 1° retângulo dentro do 2° (VND) e Vértice abaixo da reta (VB)
def test_ec_vnc_vnd_vb():
    assert colisao(1, 1, 2, 2, 3, 0, 4, 4) is 0


# CT3. Vértice comum não existe (VNC) e existe vértice do 1° retângulo dentro do 2° (VD) e Vértice acima da reta (VA)
def test_ec_vnc_vd_va():
    assert colisao(1, 1, 3, 3, 2, 2, 4, 4) is 1


# CT4. Vértice comum não existe (VNC) e existe vértice do 1° retângulo dentro do 2° (VD) e Vértice abaixo da reta (VI)
def test_ec_vnc_vd_vi():
    assert colisao(0, 0, 4, 2, 3, 0, 5, 4) is 1
