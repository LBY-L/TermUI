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
![](https://github.com/LBY-L/TermUI/blob/main/showcaseW.gif)
---

## Demos 
**/Tests/keysmove.py**
```python
import TermUI
Term = TermUI.screen()

def Main(screen):
    posX = 1
    posY = 1
    x = Term.Cols()
    y = Term.Lines()
    Term.Corners(screen)
    Term.AddStr(1, 0, "Move cursor with arrow keys!", screen, color=TermUI.Cyan())
    while True:
        Term.AddStr(x-14, y-1, "Exit Ctrl + C", screen, color=TermUI.Red())
        Term.AddChr(posX, posY, "x", screen, color=TermUI.Green())
        
        Term.Update()

        Term.Clear(screen) # Clear the buffer off screen
        Term.Corners(screen)
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

        Term.AddStr(1, 0, f"Code = {str(key)} Key = {chr(key)}", screen, color=TermUI.Blue())

Term.Wrapper(func=Main, asciiMode=False)
```

**/Tests/windows.py**
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

**/Tests/cursormove.py**
```python
import TermUI
Term = TermUI.screen()

def Main(screen):
    posX = 1
    posY = 1
    x = Term.Cols()
    y = Term.Lines()
    Term.Corners(screen)
    Term.AddStr(1, 0, "Move with wasd!", screen, color=TermUI.Cyan())
    while True:
        # This si in the loop 'cause will be re-written
        Term.AddStr(1,1,"This is a little bit of text", screen, color=TermUI.Red())
        Term.AddStr(1,2,"This is a more text that its really cool", screen, color=TermUI.Magenta())
        Term.AddStr(1,3,"Finally this is all text", screen, color=TermUI.Blue())
        
        Term.AddStr(x-14, y-1, "Exit Ctrl + C", screen, color=TermUI.Red())
        Term.SetCursor(posX, posY, screen)
        
        Term.Update()

        Term.Clear(screen) # Clear the buffer off screen
        Term.Corners(screen) 
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

Term.Wrapper(func=Main, asciiMode=False)```

**/Tests/winscroll.py**
```python
import TermUI
Term = TermUI.screen()

def Main(screen):
    posX = 1
    posY = 1
    x = Term.Cols()
    y = Term.Lines()
    Window = Term.Win(1, 1, 14, 7)
    Term.Corners(Window, color=TermUI.Cyan())
    Term.AddStr(1, 1, "Some content", Window, color=TermUI.Blue())

    Term.Corners(screen)
    Term.AddStr(1, 0, "Move with wasd!", screen, color=TermUI.Blue())
    while True:
        Term.AddStr(x-14, y-1, "Exit Ctrl + C", screen, color=TermUI.Red())
        Term.WinMove(posX, posY, Window)
        
        Term.WRefresh(Window)
        Term.Update()

        Term.Clear(screen) # Clear the buffer off screen
        Term.Corners(screen)
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

**/Tests/inputfield.py**
```python
import TermUI
Term = TermUI.screen()

def Main(screen):
    text = ""
    posX = 0
    posY = 0
    x = Term.Cols()
    y = Term.Lines()
    width = 40
    Field = Term.Win(8, 1, width, 1)
    Term.Corners(screen)
    Term.AddStr(1, 0, "Move cursor with arrow keys!", screen, color=TermUI.Cyan())
    Term.AddStr(0, 0, " " * (width-1) , Field, color="\x1b[4m")

    Term.AddStr(1, 2, "Text: "+ str(text), screen)

    while True:
        Term.AddStr(1, 1, "Field:", screen)
        Term.AddStr(x-14, y-1, "Exit Ctrl + C", screen, color=TermUI.Red())

        Term.SetCursor(posX, posY, Field)
        Term.WRefresh(Field)

        Term.Update()

        Term.Clear(screen) # Clear the buffer off screen
        Term.Clear(Field)
        Term.Corners(screen)

        key = TermUI.getchar()
        
        if key == 3:
            break
        
        if not(key == 27 or key == 91 or key == 126 or key == 13):
            if key == 68:
                posX -= 1
            elif key == 67:
                posX += 1
            elif key == 127:
                text = text[:posX-1] + text[posX:]
                posX -= 1
            elif key == 51:
                text = text[:posX] + text[posX+1:]
            else:
                posX += 1
                text = text[:posX-1] + chr(key) + text[posX-1:] 
                text = text[0:width-1]
        
        if posX < 0:
            posX = 0
        elif posX > width-1:
            posX = width-1
        elif posX > len(text):
            posX = len(text)

        Term.AddStr(0, 0, str(text).ljust(width-1, " "), Field, color="\x1b[4m")
        
        Term.AddStr(1, 2, "Text: "+ str(text), screen)

Term.Wrapper(func=Main, asciiMode=False)

```

**/Tests/nestedwindow.py**
```python
import TermUI
Term = TermUI.screen()

def Main(screen):
    y = Term.Lines()
    x = Term.Cols()
    Term.Corners(screen)
    Term.AddStr(x-14, y-1, "Exit Ctrl + C", screen, color=TermUI.Red())
    while True:
        
        window = Term.Win(1, 1, x-2, y-2)
        window2 = Term.Win(5, 2, 100, 20)
        window3 = Term.Win(17, 1, 50, 10)

        Term.Corners(window2, color=TermUI.Red())
        Term.Corners(window3, color=TermUI.Blue())
        Term.Corners(window, color=TermUI.Green())

        Term.AddStr(1, 1, "This is TermUI", window, color=TermUI.Green())
        Term.AddStr(1, 1, "This is a window", window2, color=TermUI.Red())
        Term.AddStr(1, 1, "This is other window", window3, color=TermUI.Blue())

        Term.WRefresh(window)
        Term.WRefresh(window2, window) # Refresh win2 to win
        Term.WRefresh(window3, window2) # Refresh win3 to win2
        Term.WRefresh(window2, window) # Refreshes win2 to win for show the changes in win3
        Term.WRefresh(window) # Refreshes win for show the changes in win2 nested: win3

        Term.Update()

        key = TermUI.getchar()
        if key == 3: # Key 3 = Ctrl + C
            break

Term.Wrapper(func=Main, asciiMode=False)```
