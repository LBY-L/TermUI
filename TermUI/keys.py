def getchar():
    # Returns a single character from standard input
    import os
    ch = ''
    if os.name == 'nt': # how it works on windows
        import msvcrt
        ch = msvcrt.getch()
    else:
        import tty, termios, sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ord(ch)

# Source: https://gist.github.com/jasonrdsouza/1901709
# Account Name: mvaganov