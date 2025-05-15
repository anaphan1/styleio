from .codes import codes

def end(code):
    return code + 'm'

START = '\033['
RESET = end(START + '0')

def _generate_code(graphics=None, color=None, mode='colors16'):
    if not isinstance(mode, str):
        raise TypeError("Mode must be string")
    if graphics is None:
        graphics = []
    if color is None:
        color = ''
    code = START

    if color and mode == 'rgb':
        if not isinstance(color, tuple) and not isinstance(color, list):
            raise TypeError("With mode 'rgb' color must be list")
        elif len(color) != 3:
            raise ValueError("With mode 'rgb' color must have 3 elements (r, g, and b)")
        r, g, b = color
        code += f'38;2;{r};{g};{b}'
    elif color and mode == 'colors256':
        if not 0 <= int(color) < 256:
            raise ValueError("With mode 'colors256' color must be from 0 - 255")
        code += f'38;5;{color}'
    else:
        for graphic in graphics:
            if graphic not in codes['graphics']:
                raise ValueError(f"Invalid graphic: {graphic}")
            code += codes['graphics'][graphic] + ';'

        code = code[:-1]
        if color and (mode == 'brightcolors' or mode == 'colors16'):
            if not isinstance(color, str):
                raise ValueError("With mode 'brightcolors' or 'colors16' color must be of type str")
            if color not in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'default']:
                raise ValueError("Color must be one of 'black', 'red', 'green', 'yellow', 'blue', 'magneta', 'cyan', 'white'")
            code += f';{codes[mode][color]}'
        else:
            raise ValueError("Mode not one of 'rgb', 'colors256', 'colors16', or 'bright colors'")
    return end(code)

def style(text, *args, **kwargs):
    return _generate_code(*args, **kwargs) + text + RESET
