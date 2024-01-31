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
