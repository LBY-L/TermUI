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

Term.Wrapper(func=Main, asciiMode=False)
