from PIL import Image
import numpy as np
from typing import Union

def ensure_rgb(img: Image.Image) -> Image.Image:
    """Garante que a imagem esteja no formato RGB.

    Converte a imagem para RGB caso ela esteja em outro modo (L, RGBA, CMYK etc.),
    garantindo que todas as funções de filtragem da biblioteca operem com 3 canais.

    Args:
        img (PIL.Image.Image): Imagem de entrada.

    Returns:
        PIL.Image.Image: Imagem convertida para RGB.
    """
    if img.mode != "RGB":
        return img.convert("RGB")
    return img

def to_grayscale(img: Image.Image) -> Image.Image:
    """Converte a imagem RGB para escala de cinza mantendo 3 canais.

    A imagem é convertida usando a fórmula de luminância do padrão ITU-R BT.601:
        Y = 0.299*Red + 0.587*Green + 0.114*Blue
    O resultado é replicado para os três canais para manter compatibilidade
    com outros filtros da biblioteca.

    Args:
        img (PIL.Image.Image): Imagem RGB de entrada.

    Returns:
        PIL.Image.Image: Imagem em tons de cinza com 3 canais (RGB).
    """
    img = ensure_rgb(img)
    array = np.array(img)

    red = array[:, :, 0]
    green = array[:, :, 1]
    blue = array[:, :, 2]

    gray = (0.299*red + 0.587*green + 0.114*blue).astype(np.uint8)
    out = np.stack([gray, gray, gray], axis=2)
    return Image.fromarray(out)

def to_blur(img: Image.Image, intensity: int = 1) -> Image.Image:
    """Desfoca a imagem usando média simples em uma janela 3x3.

    O filtro calcula a média dos valores de cada canal dentro de uma janela 3x3.
    As bordas são tratadas por repetição do valor mais próximo (padding 'edge').
    Permite aplicar o filtro múltiplas vezes para aumentar a intensidade do blur.

    Args:
        img (PIL.Image.Image): Imagem RGB de entrada.
        intensity (int): Número de vezes que o filtro será aplicado (padrão = 1).

    Returns:
        PIL.Image.Image: Imagem borrada.
    """
    out = ensure_rgb(img)

    # Loop para aplicar o filtro múltiplas vezes conforme a intensidade desejada
    for _ in range(intensity):
        array = np.array(out)
        height, width, _ = array.shape

        # Padding de 1 pixel em cada lado para acomodar a janela 3x3
        padded = np.pad(array, ((1, 1), (1, 1), (0, 0)), mode="edge")
        img = np.zeros_like(array)

        for y in range(height):
            for x in range(width):
                # Recorte da janela 3x3
                patch = padded[y:y+3, x:x+3]
                img[y, x] = patch.mean((0, 1))
        
        out = Image.fromarray(img.astype(np.uint8))
    return out

def to_negative(img: Image.Image) -> Image.Image:
    """Gera o negativo da imagem, invertendo os valores RGB.

    A operação aplicada é:
        pixel_saida = 255 - pixel_entrada

    Args:
        img (PIL.Image.Image): Imagem RGB de entrada.

    Returns:
        PIL.Image.Image: Imagem com cores invertidas (efeito negativo).
    """
    img = ensure_rgb(img)
    array = np.array(img)

    out = 255 - array
    return Image.fromarray(out)

def to_sepia(img: Image.Image) -> Image.Image:
    """Aplica um filtro Sépia (tom envelhecido) na imagem.

    Utiliza uma matriz de transformação de cores para converter os pixels
    para tons de marrom/amarelo, simulando fotografia antiga.

    Args:
        img (PIL.Image.Image): Imagem RGB de entrada.

    Returns:
        PIL.Image.Image: Imagem com filtro sépia aplicado.
    """
    img = ensure_rgb(img)
    array = np.array(img)

    # Matriz de transformação padrão para Sépia
    sepia_matrix = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])

    # Multiplicação matricial nos canais de cor
    out = array.dot(sepia_matrix.T)

    # Garante que os valores fiquem no intervalo válido [0, 255]
    out = np.clip(out, 0, 255).astype(np.uint8)
    return Image.fromarray(out)

def to_bright(img: Image.Image, factor: Union[int, float]) -> Image.Image:
    """Ajusta o brilho da imagem multiplicando os pixels por um fator.

    Args:
        img (PIL.Image.Image): Imagem de entrada.
        factor (float): Fator de multiplicação.
                        1.0   -> mantém o brilho original
                        < 1.0 -> escurece a imagem (ex: 0.5 é metade do brilho)
                        > 1.0 -> clareia a imagem  (ex: 1.5 aumenta 50% o brilho)

    Returns:
        PIL.Image.Image: Imagem com brilho ajustado.
    """
    img = ensure_rgb(img)
    
    # Converte para float para evitar erros de arredondamento durante a multiplicação
    array = np.array(img, dtype=np.float32)

    out = array * factor
    
    # Garante que os valores fiquem no intervalo válido [0, 255]
    out = np.clip(out, 0, 255)
    return Image.fromarray(out.astype(np.uint8))