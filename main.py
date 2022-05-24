import PIL
from PIL import Image


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

L_RED = (255, 192, 192)
RED = (255, 0, 0)
D_RED = (192, 0, 0)

L_YELLOW = (255, 255, 192)
YELLOW = (255, 255, 0)
D_YELLOW = (192, 192, 0)

L_GREEN = (192, 255, 192)
GREEN = (0, 255, 0)
D_GREEN = (0, 192, 0)

L_CYAN = (192, 255, 255)
CYAN = (0, 255, 255)
D_CYAN = (0, 192, 192)

L_BLUE = (192, 192, 255)
BLUE = (0, 0, 255)
D_BLUE = (0, 0, 192)

L_MAGENTA = (255, 192, 255)
MAGENTA = (255, 0, 255)
R_MAGENTA = (192, 0, 192)


COLORS = {
    "r": RED,
    "R": D_RED,
    "y": YELLOW,
    "Y": D_YELLOW,
    "g": GREEN,
    "G": D_GREEN,
    "c": CYAN,
    "C": D_CYAN, 
    "b": BLUE,
    "B": D_BLUE,
    "m": MAGENTA,
    "M": R_MAGENTA,
    "0": L_RED,
    "1": L_YELLOW,
    "2": L_GREEN,
    "3": L_CYAN,
    "4": L_BLUE,
    "5": L_MAGENTA,
    "#": BLACK,
    ".": WHITE
    }


def text_to_image(text):
    lines = text.split('\n')
    width = max(len(line) for line in lines)
    height = len(lines)
    image = Image.new('RGB', (width, height))
    pixels = image.load()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            pixels[x, y] = COLORS[c]
    return image



def main():
    with open("text.txt", "r") as f:
        data = f.read()
    image = text_to_image(data)
    image.save("output.png")


if __name__ == '__main__':
    main()