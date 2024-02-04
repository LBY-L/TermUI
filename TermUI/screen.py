from os import get_terminal_size
from sys import stdout
from re import compile
from os import name
from TermUI.keys import getchar

class screen:
    def _NoAnsi(self, text):  
        noAnsi = compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        return noAnsi.sub("", text)

    def _Buffer(self, x, y):
        Buffer = [[" "] * x for _ in range(y)]
        return Buffer

    def _Plotter(self, matrix, y, x, win):
        winy, winx = len(matrix), len(matrix[0])
        for i in range(winy):
            for j in range(winx):
                # Matrix size
                xmain, ymain = x + i, y + j
                # Window cordinates comprobation
                if 0 <= xmain < len(win) and 0 <= ymain < len(win[0]):
                    win[xmain][ymain] = matrix[i][j]

    def Update(self):
        """
        Update: Write the contents to the screen
        """
        if name == "nt": # Just a random error
            print("\x1b[H" + '\n'.join([''.join(n) for n in self.Stdscr]), end="", flush=True) # Too fast for windows terminal
        else:
            stdout.buffer.write(bytes("\x1b[H" + '\n'.join([''.join(n) for n in self.Stdscr]), encoding="utf-8"))
        
    def _Init(self):
        self.width, self.height = get_terminal_size().columns, get_terminal_size().lines 
        self.Stdscr = self._Buffer(self.width, self.height)

        return [0, 0, self.Stdscr] # Return stdscr properties
    
    def Wrapper(self, func, asciiMode=False):
        """
        Wrapper: Run TermUI programs also sets the to use extended ascii mode or not
        """

        self.asciiMode = asciiMode

        stdout.buffer.write(b"\x1b[?1049h\x1b[?25l") # Set alt-buffer and disapears cursor
        func(screen=self._Init())
        stdout.buffer.write(b"\x1b[?1049l\x1b[?25h") # Reset to normal

    def Cols(self):
        """
        Cols: Return the number of cols of the screen
        """
        return self.width
    
    def Lines(self):
        """
        Lines: Return the number of lines of the screen
        """
        return self.height

    def Clear(self, win=list):
        """
        Clear: clear the buffer off screen
        """
        Win = win[2]
        for i, n in enumerate(Win): # Some weird problem in memory
            Win[i] = [" "] * len(Win[0])

    def SetCursor(self, x=int, y=int, win=list):
        """
        SetCursor: Set a simulated cursor not a real cursor at x and y cordinates
        """
        Background = ""
        if 0 <= y < len(win[2]) and 0 <= x < len(win[2][0]):
            Background = self._NoAnsi(win[2][y][x])

        Cursor = [str(f"\x1b[47;30m{Background}\x1b[0m")]
        self._Plotter([Cursor], x, y, win[2])
        #return [x, y] Idk i want to make a return

    def Win(self, x=int, y=int, x1=int, y1=int):
        """
        Win: Creates a window object x1 and y1 size of the window
        """
        height, width = y1, x1
        Win = self._Buffer(width, height)
        return [x, y, Win]
    
    def WinMove(self, x=int, y=int, win=list):
        """
        WinMove: Move window to x and y cordinates
        """
        win[0], win[1] = x, y
        
    def WRefresh(self, win=list, screen=None):
        if screen == None:
            screen = self.Stdscr
        else:
            screen = screen[2]
        """
        WRefresh: Refresh the windows to a screen "Note: Doesn't update the actual screen"
        """
        x, y, Win = win[0], win[1], win[2]
        self._Plotter(Win, x, y, screen)
    
    def Corners(self, win=list, color=""):
        """
        Corners: Set corners to a windows also can set a corner color
        """
        Win = win[2]

        if self.asciiMode:
            bordersX, bordersY = f"{color}-\x1b[0m", f"{color}|\x1b[0m"
            cornersX = f"{color}+\x1b[0m"
            cornersX1, cornersY, cornersY1 = cornersX, cornersX, cornersX 
        else:
            bordersX, bordersY = f"{color}─\x1b[0m", f"{color}│\x1b[0m"
            cornersX, cornersX1 = f"{color}┌\x1b[0m", f"{color}┐\x1b[0m"
            cornersY, cornersY1 = f"{color}└\x1b[0m", f"{color}┘\x1b[0m"

        for i in range(len(Win)): Win[i][0], Win[i][-1] = bordersY, bordersY
        for i in range(len(Win[0])): Win[0][i], Win[-1][i] = bordersX, bordersX

        Win[0][0], Win[0][-1] = cornersX, cornersX1
        Win[-1][0], Win[-1][-1] = cornersY, cornersY1

    def AddChr(self, x=int, y=int, yourChr=str, win=list, color=""):
        """
        AddChr: Add a chr at x and y at win also with a color
        """
        Win = win[2]
        toPlot = [f"{color}{''.join(yourChr[:1])}\x1b[0m"]
        self._Plotter([toPlot], x, y, Win)

    def AddStr(self, x=int, y=int, yourStr=str, win=int, color=""):
        """
        AddStr: Add a str at x and y at win also with a color
        """
        Win = win[2]
        toPlot = [f"{color}{i}\x1b[0m" for i in [*yourStr]]
        self._Plotter([toPlot], x, y, Win)
