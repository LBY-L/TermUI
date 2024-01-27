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
