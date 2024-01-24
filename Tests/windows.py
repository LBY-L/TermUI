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

Term.Wrapper(func=Main, asciiMode=False)
