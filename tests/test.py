'''
cd tests
python -m venv .venv
source .venv/bin/activate
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pyfil==0.0.1
'''


import pyfil          
from PIL import Image 
import os           

# Tenta abrir a imagem.
try:
    original = Image.open("foto.jpg")
    print(f"Imagem carregada com sucesso! Formato original: {original.format}")
except FileNotFoundError:
    print("ERRO: O arquivo 'foto.jpg' não foi encontrado nesta pasta.")
    exit()

# TESTE DOS FILTROS

# Escala de Cinza
print("1. Aplicando Escala de Cinza...")
gray = pyfil.to_grayscale(original)
gray.save("1_cinza.jpeg")

# Sépia
print("2. Aplicando Filtro Sépia...")
sepia = pyfil.to_sepia(original)
sepia.save("2_sepia.png")

# Negativo
print("3. Aplicando Negativo...")
negative = pyfil.to_negative(original)
# Salvando em PNG para mostrar flexibilidade de formato
negative.save("3_negativo.bmp")

# Blur com intensidade variável
print("4. Aplicando Blur (Intensidade 3)...")
blur = pyfil.to_blur(original, intensity=3)
blur.save("4_blur.webp")

# Brilho
print("5. Aumentando o Brilho (50%)...")
bright = pyfil.to_bright(original, factor=1.5)
bright.save("5_brilho.tiff")

# TESTE DE COMBINAÇÃO DE FILTROS

# EFEITO 1: FOTO ANTIGA
# Passo A: Pega a original e aplica Sépia
passo1 = pyfil.to_sepia(original)
# Passo B: Pega o resultado do passo 1 e aplica Blur
passo2 = pyfil.to_blur(passo1, intensity=3)
# Passo C: Pega o resultado do passo 2 e escurece (fator < 1.0)
resultado_final = pyfil.to_bright(passo2, factor=0.7)
# Salvando o combo
resultado_final.save("6_efeito_antiga.jpg")

# EFEITO 2: SONHO / DREAMLIKE
sonho1 = pyfil.to_blur(original, intensity=2)
sonho2 = pyfil.to_bright(sonho1, factor=1.3)
sonho_final = pyfil.to_blur(sonho2, intensity=1)
sonho_final.save("7_efeito_sonho.jpg")

# EFEITO 3: TERROR / HORROR
terror1 = pyfil.to_grayscale(original)
terror2 = pyfil.to_negative(terror1)
terror3 = pyfil.to_blur(terror2, intensity=1)
terror_final = pyfil.to_bright(terror3, factor=0.5)
terror_final.save("8_efeito_terror.jpg")

# EFEITO 4: VINTAGE SUAVE
vintage1 = pyfil.to_sepia(original)
vintage2 = pyfil.to_bright(vintage1, factor=1.15)
vintage_final = pyfil.to_blur(vintage2, intensity=1)
vintage_final.save("9_efeito_vintage_suave.jpg")

print("Todos os filtros foram aplicados e salvos com sucesso!")