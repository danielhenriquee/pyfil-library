# PyFil - Python Image Filtering Library

## Descrição

**PyFil** é uma biblioteca Python para processamento e filtragem de imagens, desenvolvida com foco em simplicidade e eficiência. A biblioteca oferece um conjunto de filtros e transformações essenciais para manipulação de imagens, utilizando processamento matricial com NumPy e a robustez da PIL (Python Imaging Library).

O projeto foi desenvolvido como parte da disciplina **Introdução à Programação em Python** da UNIVALI, com o objetivo de simular o ciclo completo de desenvolvimento, empacotamento e distribuição de software open-source.

## Características Principais

- **Interface Intuitiva**: Funções simples e diretas para aplicação de filtros
- **Eficiência**: Implementação otimizada usando operações vetorizadas do NumPy
- **Compatibilidade**: Suporte para múltiplos formatos de imagem (JPEG, PNG, BMP, etc.)
- **Conversão Automática**: Tratamento automático de diferentes modos de cor
- **Sem Dependências Externas Pesadas**: Utiliza apenas PIL/Pillow e NumPy

## Instalação

### Via Test PyPI

```bash
pip install -i https://test.pypi.org/simple/ pyfil
```

### Instalação das Dependências

A biblioteca requer as seguintes dependências, que serão instaladas automaticamente:

```bash
pip install Pillow numpy
```

## Início Rápido

### Exemplo Básico

```python
from PIL import Image
import pyfil

# Carregar uma imagem
img = Image.open("foto.jpg")

# Aplicar filtro de escala de cinza
img_gray = pyfil.to_grayscale(img)
img_gray.save("foto_cinza.jpg")

# Aplicar filtro sépia
img_sepia = pyfil.to_sepia(img)
img_sepia.save("foto_sepia.jpg")

# Criar negativo
img_negative = pyfil.to_negative(img)
img_negative.save("foto_negativa.jpg")
```

### Exemplo com Múltiplos Filtros

```python
from PIL import Image
import pyfil

# Carregar imagem
original = Image.open("paisagem.jpg")

# Combinação de filtros: sépia + brilho reduzido
img_combo = pyfil.to_sepia(original)
img_combo = pyfil.to_bright(img_combo, factor=0.8)
img_combo.save("paisagem_vintage.jpg")
```

## Documentação da API

### `ensure_rgb(img: Image.Image) -> Image.Image`

Garante que a imagem esteja no formato RGB, convertendo-a caso necessário.
Utilizada internamente para garantir compatibilidade entre filtros.

**Parâmetros:**
- `img` (PIL.Image.Image): Imagem de entrada em qualquer modo de cor

**Retorna:**
- PIL.Image.Image: Imagem convertida para modo RGB

**Exemplo:**
```python
img = Image.open("imagem.png")  # Pode estar em RGBA
img_rgb = pyfil.ensure_rgb(img)
```

---

### `to_grayscale(img: Image.Image) -> Image.Image`

Converte a imagem para escala de cinza mantendo 3 canais RGB.

Utiliza a fórmula de luminância do padrão ITU-R BT.601:
```
Y = 0.299×R + 0.587×G + 0.114×B
```

**Parâmetros:**
- `img` (PIL.Image.Image): Imagem RGB de entrada

**Retorna:**
- PIL.Image.Image: Imagem em tons de cinza com 3 canais

**Exemplo:**
```python
img_gray = pyfil.to_grayscale(img)
```

---

### `to_blur(img: Image.Image, intensity: int = 1) -> Image.Image`

Aplica desfoque na imagem usando média simples em janela 3×3.

**Parâmetros:**
- `img` (PIL.Image.Image): Imagem RGB de entrada
- `intensity` (int, opcional): Número de iterações do filtro (padrão: 1)

**Retorna:**
- PIL.Image.Image: Imagem com efeito de desfoque

**Exemplo:**
```python
# Blur leve
img_blur_leve = pyfil.to_blur(img, intensity=1)

# Blur intenso
img_blur_intenso = pyfil.to_blur(img, intensity=5)
```

---

### `to_negative(img: Image.Image) -> Image.Image`

Gera o negativo da imagem invertendo os valores de cor.

Aplica a transformação: `pixel_saída = 255 - pixel_entrada`

**Parâmetros:**
- `img` (PIL.Image.Image): Imagem RGB de entrada

**Retorna:**
- PIL.Image.Image: Imagem com cores invertidas

**Exemplo:**
```python
img_negative = pyfil.to_negative(img)
```

---

### `to_sepia(img: Image.Image) -> Image.Image`

Aplica filtro sépia para criar efeito de fotografia envelhecida.

Utiliza matriz de transformação de cores padrão para tons marrom/amarelados.

**Parâmetros:**
- `img` (PIL.Image.Image): Imagem RGB de entrada

**Retorna:**
- PIL.Image.Image: Imagem com filtro sépia aplicado

**Exemplo:**
```python
img_sepia = pyfil.to_sepia(img)
```

---

### `to_bright(img: Image.Image, factor: Union[int, float]) -> Image.Image`

Ajusta o brilho da imagem multiplicando os pixels por um fator.

**Parâmetros:**
- `img` (PIL.Image.Image): Imagem de entrada
- `factor` (float): Fator de multiplicação
  - `1.0`: mantém o brilho original
  - `< 1.0`: escurece a imagem (ex: 0.5 reduz o brilho pela metade)
  - `> 1.0`: clareia a imagem (ex: 1.5 aumenta o brilho em 50%)

**Retorna:**
- PIL.Image.Image: Imagem com brilho ajustado

**Exemplo:**
```python
# Escurecer
img_dark = pyfil.to_bright(img, factor=0.6)

# Clarear
img_light = pyfil.to_bright(img, factor=1.4)
```

## Estrutura do Projeto

```
pyfil/
│
├── pyfil/
│   ├── __init__.py
│   └── pyfil.py          # Módulo principal com todas as funções
│
├── tests/
│   └── test_pyfil.py     # Testes unitários (se implementados)
│
├── examples/
│   └── usage_examples.py # Exemplos de uso
│
├── LICENSE               # Licença do projeto
├── README.md            # Este arquivo
├── pyproject.toml       # Configuração do projeto
└── setup.py             # Script de instalação
```

## Requisitos do Sistema

- **Python**: 3.7 ou superior
- **Pillow**: 8.0 ou superior
- **NumPy**: 1.19 ou superior

## Fundamentos Técnicos

### Processamento de Imagens

A biblioteca utiliza representação matricial de imagens, onde cada pixel é tratado como um vetor de valores RGB (Red, Green, Blue) no intervalo [0, 255]. As operações são realizadas de forma vetorizada usando NumPy para garantir eficiência computacional.

### Conversão de Espaços de Cor

A função `to_grayscale` implementa a conversão RGB → Luminância seguindo o padrão ITU-R BT.601, que pondera os canais de acordo com a sensibilidade do olho humano às diferentes cores.

### Convolução e Filtragem Espacial

O filtro `to_blur` implementa uma convolução discreta 2D com kernel uniforme 3×3, aplicando média local para suavização da imagem. O tratamento de bordas utiliza padding por replicação de pixels extremos.

## Testes

Para executar os testes unitários (quando implementados):

```bash
python -m pytest tests/
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE) - veja o arquivo LICENSE para detalhes.

## Autores

- **Daniel Henrique da Silva**
- **Guilherme Melo**
- **Leonardo Pinheiro de Souza**
