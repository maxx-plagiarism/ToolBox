from math import ceil


def cmyk2rgb(c, m, y, k):
    """
    Convert CMYK to RGB
    args:
        c: Cyan 0.0 - 1.0
        m: Magenta 0.0 - 1.0
        y: Yellow 0.0 - 1.0
        k: Key 0.0 - 1.0
    ruturns RGB as tuple
    """
    r = ceil(255 * (1 - c) * (1 - k))
    g = ceil(255 * (1 - m) * (1 - k))
    b = ceil(255 * (1 - y) * (1 - k))

    return (r, g, b)


def hex2rgb(h):
    """
    Convert HEX to RGB
    args:
        h: HEX string 'abcdef'
    ruturns RGB as tuple
    """
    tmp = list()
    rgb = list()
    if len(h) == 3:
        d = 1
    if len(h) == 6:
        d = 2
    for i in range(3):
        tmp.append(h[i * d: i * d + d])
    for i in tmp:
        rgb.append(int(i, 16))

    return (rgb)


def hsl2rgb(h, s, l):
    """
    Convert HSL to RGB
    args:
        h: Hue 0..359
        s: Saturation 0.0 - 1.0
        l: Lightnes 0.0 - 1.0
    ruturns RGB as tuple
    """
    h = h % 360

    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    if h >= 0 and h < 60:
        rgb = ((c + m) * 255, (x + m) * 255, m * 255)
    if h >= 60 and h < 120:
        rgb = ((x + m) * 255, (c + m) * 255, m * 255)
    if h >= 120 and h < 180:
        rgb = (m * 255, (c + m) * 255, (x + m) * 255)
    if h >= 180 and h < 240:
        rgb = (m * 255, (x + m) * 255, (c + m) * 255)
    if h >= 240 and h < 300:
        rgb = ((x + m) * 255, m * 255, (c + m) * 255)
    if h >= 300 and h < 360:
        rgb = ((c + m) * 255, m * 255, (x + m) * 255)

    rgb = (ceil(rgb[0]), ceil(rgb[1]), ceil(rgb[2]))

    return rgb


def hsv2rgb(h, s, v):
    """
    Convert HSV to RGB
    args:
        h: Hue 0..359
        s: Saturation 0.0 - 1.0
        v: Value 0.0 - 1.0
    ruturns RGB as tuple
    """
    h = h % 360

    c = float(v * s)
    x = float(c * (1 - abs((h / 60) % 2 - 1)))
    m = float(v - c)
    if h >= 0 and h < 60:
        rgb = ((c + m) * 255, (x + m) * 255, m * 255)
    if h >= 60 and h < 120:
        rgb = ((x + m) * 255, (c + m) * 255, m * 255)
    if h >= 120 and h < 180:
        rgb = (m * 255, (c + m) * 255, (x + m) * 255)
    if h >= 180 and h < 240:
        rgb = (m * 255, (x + m) * 255, (c + m) * 255)
    if h >= 240 and h < 300:
        rgb = ((x + m) * 255, m * 255, (c + m) * 255)
    if h >= 300 and h < 360:
        rgb = ((c + m) * 255, m * 255, (x + m) * 255)

    rgb = (ceil(rgb[0]), ceil(rgb[1]), ceil(rgb[2]))

    return rgb


def rgb2cmyk(r, g, b):
    """
    Convert RGB to CMYK
    args:
        r: Red 0 - 255
        g: Green 0 - 255
        b: Blue 0 - 255
    ruturns CMYK as tuple
    """

    r /= 255.0
    g /= 255.0
    b /= 255.0

    k = 1 - max(r, g, b)
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)

    return (c, m, y, k)


def rgb2hex(r, g, b):
    """
    Convert RGB to HEX
    args:
        r: Red 0 - 255
        g: Green 0 - 255
        b: Blue 0 - 255
    ruturns HEX as string 'abcdef'
    """

    r = hex(r)[2:]
    if len(r) < 2:
        r = "0" + r
    g = hex(g)[2:]
    if len(g) < 2:
        g = "0" + g
    b = hex(b)[2:]
    if len(b) < 2:
        b = "0" + b

    return r + g + b


def rgb2hsl(r, g, b):
    """
    Convert RGB to HSL
    args:
        r: Red 0 - 255
        g: Green 0 - 255
        b: Blue 0 - 255
    ruturns HSL as tuple
    """

    r /= 255.0
    g /= 255.0
    b /= 255.0

    c_max = max(r, g, b)
    c_min = min(r, g, b)

    delta = c_max - c_min

    lt = (c_max + c_min) / 2

    if delta == 0:
        s = 0
        h = 0
    else:
        s = delta / (1 - abs(2 * lt - 1))
        if c_max == r:
            h = 60 * (((g - b) / delta) % 6)
        if c_max == g:
            h = 60 * (((b - r) / delta) + 2)
        if c_max == b:
            h = 60 * (((r - g) / delta) + 4)

    return (h, s, lt)


def rgb2hsv(r, g, b):
    """
    Convert RGB to HSV
    args:
        r: Red 0 - 255
        g: Green 0 - 255
        b: Blue 0 - 255
    ruturns HSV as tuple
    """
    r /= 255.0
    g /= 255.0
    b /= 255.0

    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min

    v = c_max
    if c_max == 0:
        s = 0
    else:
        s = delta / c_max

    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * (((b - r) / delta) + 2)
    elif c_max == b:
        h = 60 * (((r - g) / delta) + 4)

    return (h, s, v)


def int2rgb(val):
    r = (val & 16711680) >> 16
    g = (val & 65280) >> 8
    b = val & 255
    return (r, g, b)


def rgb2int(r, g, b):
    return (r << 16) + (g << 8) + b


def main():
    print(f'R: 170\tG: 85\tB: 170\t{rgb2int(170, 85, 170):,d}')
    r, g, b = int2rgb(11163050)
    print(f'{11163050:,d}\tR: {r}\tG: {g}\tB: {b}')


if __name__ == "__main__":
    main()
