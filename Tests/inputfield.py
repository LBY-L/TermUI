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

