# How to use

## Requirements
- Python 3.6 or more
- Windows*

## How to use
First install with pip
```commandline
pip install styleio
```
Now import
```python
import styleio
```
Now style that IO!

First, you need to think about how your IO will look like.
You can have text styled. Just simply enter one of bold, dim, italic, underline, blink, inverse, hidden,  or strikethrough

Now, color your text. Color is optional, but you have four color mode choices: rgb**, 256 colors**, 16 colors, and bright colors***

*I have not tested on an operating system without windows, feel free to open an issue with the readme saying otherwise on github
**RGB and 256 color modes do NOT support styled text
***Only terminals that support the aixterm specification (mine did) support brightcolors

If you have rgb colors, the mode will be 'rgb' and the color will be a tuple of (r, g, b), where 0 <= r, g, b, <= 255, and the mode will be 'rgb'
If you have 256 colors, the mode will be 'colors256' and the color will be an id 0 <= id <= 255, where each id means these colors:
![](https://user-images.githubusercontent.com/995050/47952855-ecb12480-df75-11e8-89d4-ac26c50e80b9.png)
0-7: standard colors (as in ESC [ 30–37 m)
8–15: high intensity colors (as in ESC [ 90–97 m)
16-231: 6 × 6 × 6 cube (216 colors): 16 + 36 × r + 6 × g + b (0 ≤ r, g, b ≤ 5). Some interpret these as constant increments, while others have specific values for each one
232-255: grayscale from dark to light in 24 steps.

With 16 colors (normal, recommended), the mode will be 'colors16', and color will be one of
'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'default'
Bright colors are just like 16 colors, its just that they will look brighter on the terminal and the mode is 'brightcolors'

## Styling the IO

First, specify the list of styles
```python
graphics = ['bold', 'italic']
```
Next, specify the color. Say I want bright red
```python
color = 'red'
mode = 'brightcolors'
```

Now, finally style the output

```python
string = style(
    graphics=graphics,
    color=color,
    mode=mode
)
print(string)
```