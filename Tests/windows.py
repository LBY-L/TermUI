import TermUI
from time import sleep
Term = TermUI.screen()

def Main():
    stdscr = Term.Init()
    while True:
        Term.Corners(stdscr)
        y = Term.Lines()
        x = Term.Cols()
        window = Term.Win(1, 1, x-2, (y-2)//2)
        window2 = Term.Win(1, y//2, (x-2)//2, (y-2)//2)
        window3 = Term.Win(x//2, y//2, (x-2)//2, (y-2)//2)
        Term.Corners(window)
        Term.Corners(window2)
        Term.Corners(window3)
        Term.WRefresh(window)
        Term.WRefresh(window2)
        Term.WRefresh(window3)
        Term.Update()
        key = TermUI.getchar()
        if key == 3:
            break

Term.Wrapper(func=Main, asciiMode=False)
