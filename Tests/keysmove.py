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
