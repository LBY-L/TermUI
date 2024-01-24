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
        #print(key)
        if key == 115:
            posY += 1
        if key == 97:
            posX -= 1
        if key == 100:
            posX += 1

Term.Wrapper(func=Main, asciiMode=True)
