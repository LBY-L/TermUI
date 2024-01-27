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

## Showcase
![](https://github.com/LBY-L/TermUI/blob/main/showcase.gif)
---

## Demos 
**/Test/windows.py**
```python
import TermUI
Term = TermUI.screen()

def Main(screen):
    y = Term.Lines()
    x = Term.Cols()
    Term.Corners(screen)
    Term.AddStr(x-14, y-1, "Exit Ctrl + C", screen, color=TermUI.Red())
    while True:
        
        window = Term.Win(1, 1, x-2, (y-2)//2)
        window2 = Term.Win(1, y//2, (x-2)//2, (y-2)//2)
        window3 = Term.Win(x//2, y//2, (x-2)//2, (y-2)//2)

        Term.Corners(window, color=TermUI.Green())
        Term.Corners(window2, color=TermUI.Red())
        Term.Corners(window3, color=TermUI.Blue())

        Term.AddStr(1, 1, "This is TermUI", window, color=TermUI.Green())
        Term.AddStr(1, 1, "This is a window", window2, color=TermUI.Red())
        Term.AddStr(1, 1, "This is other window", window3, color=TermUI.Blue())

        Term.WRefresh(window)
        Term.WRefresh(window2)
        Term.WRefresh(window3)

        Term.Update()

        key = TermUI.getchar()
        if key == 3: # Key 3 = Ctrl + C
            break

Term.Wrapper(func=Main, asciiMode=False)
```
---
**/Test/keysmove.py**
```python
import TermUI

Term = TermUI.screen()

def Main(screen):
    posX = 1
    posY = 1
    x = Term.Cols()
    y = Term.Lines()
    mystr = "Move with wasd!"
    while True:
        Term.Corners(screen) # This si in the loop 'cause will be re-written
        Term.AddStr(1, 0, mystr, screen, color=TermUI.Cyan()); mystr = ""
        
        Term.AddStr(x-14, y-1, "Exit Ctrl + C", screen, color=TermUI.Red())
        Term.AddChr(posX, posY, "x", screen, color=TermUI.Green())
        
        Term.Update()

        Term.Clear(screen) # Clear the buffer off screen
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
