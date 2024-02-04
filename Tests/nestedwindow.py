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

Term.Wrapper(func=Main, asciiMode=False)