<h1 align="center">TermUI</h1>
<h3 align="center">
A text based library, ncurses like, fully written in python without external libraries</h3>

## Table of funcions and clases
### Styling
| Function | What does?        |
| ---      | ---               | 
| Green    | Green Foreground  |
| GreenBG  | Green Background  |
| Blue     | Blue Foreground   |
| BlueBG   | Blue Background   |
| Cyan     | Cyan Foreground   |
| CyanBG   | Cyan Background   |
| Yellow   | Yellow Foreground |
| YellowBG | Yellow Background |
| Magenta  | Magenta Foreground|
| MagentaBG| Magenta Background|
| Red      | Red Foreground    |
| RedBG    | Red Background    |
| Black    | Black Foreground  |
| BlackBG  | Black Background  |
| White    | White Foreground  |
| WhiteBG  | White Background  |
### Input
| Function | What does?                    |
| ---      | ---                           | 
| getchar  | Get the key presses in numbers|
### Screen
| Class  | Function | What does?                               |
| ---    | ---      | ---                                      |
| screen | Init     | Initializes de main window               |
| screen | Win      | Initializes a windows in the main window |
| screen | WinMove  | Move a window                            |
| screen | WRefresh | Refresh the window in main window        |
| screen | Corners  | Put corners in a window object           |
| screen | AddChr   | Add a single character to a window object|
| screen | AddStr   | Add a string in a window object          |
| screen | Clear    | Clear a window object                    |
| screen | Update   | Print the windows in the screen          |
| screen | Wrapper  | Usa function to execute                  |
| screen | Cols     | Return main window width                 |
| screen | Lines    | Retunr main window height                |  

### Showcase
![](https://github.com/LBY-L/TermUI/blob/main/showcase.gif)
---

### Demos 
**/Test/keysmove.py**
```python
import TermUI
from time import sleep
Term = TermUI.screen()

def Main():
    stdscr = Term.Init()
    posX = 1
    posY = 1
    while True:
        Term.Corners(stdscr)
        Term.AddChr(posX, posY, "i", stdscr, color=TermUI.Green())
        Term.Update()
        Term.Clear(stdscr)
        key = TermUI.getchar()
        if key == 3:
            break
        if key == 119:
            posY -= 1
        if key == 115:
            posY += 1
        if key == 97:
            posX -= 1
        if key == 100:
            posX += 1

Term.Wrapper(func=Main, asciiMode=False)
```
---

**/Tests/windows.py**
```python
import TermUI
from time import sleep
Term = TermUI.screen()

def Main():
    stdscr = Term.Init()
    while True:
        Term.Corners(stdscr)
        window = Term.Win(1, 1, 40, 20)
        Term.Corners(window)
        Term.WRefresh(window)
        Term.Update()
        key = TermUI.getchar()
        if key == 3:
            break

Term.Wrapper(func=Main, asciiMode=True)
```
