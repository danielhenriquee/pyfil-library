# PyFil - Biblioteca Python para filtros de imagens

## Descrição

**PyFil** é uma biblioteca Python para processamento e filtragem de imagens, desenvolvida com foco em simplicidade e eficiência. A biblioteca oferece um conjunto de filtros e transformações essenciais para manipulação de imagens, utilizando processamento matricial com NumPy e a robustez da PIL (Python Imaging Library).

O projeto foi desenvolvido como parte da disciplina **Introdução à Programação em Python** da UNIVALI, com o objetivo de simular o ciclo completo de desenvolvimento, empacotamento e distribuição de software open-source.

## Características Principais

- **Interface Intuitiva**: Funções simples e diretas para aplicação de filtros
- **Eficiência**: Implementação otimizada usando operações vetorizadas do NumPy
- **Compatibilidade**: Suporte para múltiplos formatos de imagem (JPEG, PNG, BMP, TIFF, GIF, WEBP, etc.)
- **Flexibilidade de Formato**: Leia uma imagem em um formato e salve em outro (ex: abrir JPG e salvar como PNG)
- **Conversão Automática**: Tratamento automático de diferentes modos de cor
- **Validação Robusta**: Tratamento de erros e validação de entrada em todas as funções
- **Sem Dependências Externas Pesadas**: Utiliza apenas PIL/Pillow e NumPy

## Instalação

### Instalação Completa (Recomendado)

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pyfil
```

Este comando instala automaticamente as dependências necessárias (Pillow e NumPy).

### Instalação Manual (Alternativa)

```bash
# 1. Instalar dependências
pip install Pillow numpy

# 2. Instalar pyfil do Test PyPI
pip install -i https://test.pypi.org/simple/ pyfil
```

## Início Rápido

### Importação Necessária

**Importante:** Para usar a biblioteca, você precisa importar tanto o `pyfil` quanto o `PIL.Image`:

```python
import pyfil          
from PIL import Image
```

- **`pyfil`**: Fornece as funções de filtragem (to_grayscale, to_sepia, etc.)
- **`PIL.Image`**: Necessário para abrir e salvar imagens

### Fluxo Básico de Trabalho

O fluxo padrão para usar a pyfil segue 3 etapas:

1. **Abrir a imagem** com `Image.open()`
2. **Aplicar filtros** usando funções do `pyfil`
3. **Salvar o resultado** com `.save()`

```python
import pyfil
from PIL import Image

# 1. Abrir a imagem
img = Image.open("foto.jpg")

# 2. Aplicar filtro
img_filtrada = pyfil.to_grayscale(img)

# 3. Salvar o resultado
img_filtrada.save("foto_cinza.jpg")
```

### Suporte a Múltiplos Formatos

A pyfil suporta diversos formatos de imagem através da PIL/Pillow. Você pode:

- **Abrir** imagens em formatos: JPEG, JPG, PNG, BMP, TIFF, GIF, WEBP, e outros
- **Salvar** o resultado em qualquer formato suportado
- **Converter formatos** automaticamente (ex: abrir JPG e salvar como PNG)

```python
# Exemplo: Abrir JPEG e salvar como PNG
img = Image.open("foto.jpg")           # Abre JPEG
img_sepia = pyfil.to_sepia(img)
img_sepia.save("foto_sepia.png")       # Salva como PNG

# Exemplo: Abrir PNG e salvar como JPEG
img = Image.open("imagem.png")         # Abre PNG
img_blur = pyfil.to_blur(img, intensity=3)
img_blur.save("imagem_blur.jpg")       # Salva como JPEG
```

**Nota:** O formato de saída é determinado pela extensão do arquivo no método `.save()`.

### Exemplo Básico Completo

```python
import pyfil
from PIL import Image

# Abrir uma imagem
img = Image.open("foto.jpg")

# Aplicar filtro de escala de cinza
img_gray = pyfil.to_grayscale(img)
img_gray.save("foto_cinza.jpg")

# Aplicar filtro sépia
img_sepia = pyfil.to_sepia(img)
img_sepia.save("foto_sepia.png")        # Salva em formato diferente

# Criar negativo
img_negative = pyfil.to_negative(img)
img_negative.save("foto_negativa.jpg")
```

### Exemplo com Múltiplos Filtros

```python
import pyfil
from PIL import Image

# Carregar imagem
original = Image.open("paisagem.jpg")

# Combinação de filtros: sépia + brilho reduzido
img_combo = pyfil.to_sepia(original)
img_combo = pyfil.to_bright(img_combo, factor=0.8)
img_combo.save("paisagem_vintage.jpg")
```

## Combinando Filtros

Um dos diferenciais da **pyfil** é a facilidade de combinar múltiplos filtros para criar efeitos personalizados:

### Efeito "Foto Antiga Assustadora"
```python
import pyfil
from PIL import Image

original = Image.open("foto.jpg")

# Pipeline: Sépia → Blur → Escurecimento
passo1 = pyfil.to_sepia(original)
passo2 = pyfil.to_blur(passo1, intensity=3)
resultado = pyfil.to_bright(passo2, factor=0.7)
resultado.save("foto_antiga_dark.jpg")
```

### Efeito "Sonho"
```python
# Pipeline: Blur → Iluminação → Blur suave
passo1 = pyfil.to_blur(original, intensity=2)
passo2 = pyfil.to_bright(passo1, factor=1.3)
resultado = pyfil.to_blur(passo2, intensity=1)
resultado.save("efeito_sonho.jpg")
```

### Efeito "Terror"
```python
# Pipeline: Grayscale → Negativo → Blur → Escurecimento intenso
passo1 = pyfil.to_grayscale(original)
passo2 = pyfil.to_negative(passo1)
passo3 = pyfil.to_blur(passo2, intensity=1)
resultado = pyfil.to_bright(passo3, factor=0.5)
resultado.save("efeito_terror.jpg")
```

### Efeito "Vintage Suave"
```python
# Pipeline: Sépia → Iluminação leve → Blur mínimo
passo1 = pyfil.to_sepia(original)
passo2 = pyfil.to_bright(passo1, factor=1.15)
resultado = pyfil.to_blur(passo2, intensity=1)
resultado.save("vintage_suave.jpg")
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
│   └── __init__.py
│
├── tests/
│   └── test.py           # Script de teste dos filtros
│
├── LICENSE               # Licença do projeto
├── README.md             # Este arquivo
└── pyproject.toml        # Configuração do projeto
```

## Requisitos do Sistema

- **Python**: 3.7 ou superior
- **Pillow**: 8.0 ou superior
- **NumPy**: 1.19 ou superior

## Tratamento de Erros

A biblioteca PyFil implementa validação robusta de entrada para garantir operações seguras:

### Validações Automáticas

Todas as funções validam automaticamente:
- **Tipo de entrada**: Verifica se o objeto é uma imagem PIL válida
- **Dimensões**: Garante que a imagem não está vazia (0×0)
- **Valores None**: Rejeita entradas nulas

### Exceções Específicas

**`TypeError`**: Lançado quando:
- A entrada não é um objeto PIL.Image
- Parâmetros têm tipo incorreto (ex: intensity não é int)

**`ValueError`**: Lançado quando:
- A imagem tem dimensões inválidas (0×0)
- Parâmetros têm valores inválidos (ex: intensidade do blur ou fator de brilho negativos)
  
## Fundamentos Técnicos

### Processamento de Imagens

A biblioteca utiliza representação matricial de imagens, onde cada pixel é tratado como um vetor de valores RGB (Red, Green, Blue) no intervalo [0, 255]. As operações são realizadas de forma vetorizada usando NumPy para garantir eficiência computacional.

### Conversão de Espaços de Cor

A função `to_grayscale` implementa a conversão RGB → Luminância seguindo o padrão ITU-R BT.601, que pondera os canais de acordo com a sensibilidade do olho humano às diferentes cores.

### Convolução e Filtragem Espacial

O filtro `to_blur` implementa uma convolução discreta 2D com kernel uniforme 3×3, aplicando média local para suavização da imagem. O tratamento de bordas utiliza padding por replicação de pixels extremos.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE) - veja o arquivo LICENSE para detalhes.

## Links

- **Repositório GitHub:** https://github.com/danielhenriquee/pyfil-library
- **Test PyPI:** https://test.pypi.org/project/pyfil/0.0.1/

---

## Autores

- **Daniel Henrique da Silva** - danielhenrique@edu.univali.br
- **Guilherme Melo** - guilherme.8576076@edu.univali.br
- **Leonardo Pinheiro de Souza** - leonardo.8557802@edu.univali.br

**Disciplina:** Introdução à Python
**Professor:** Evandro Chagas Ribeiro da Rosa  
**Instituição:** Universidade do Vale do Itajaí
