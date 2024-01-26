from os import get_terminal_size
from sys import stdout
from re import compile, findall

class screen:
    def _NoAnsi(self, text):  
        noAnsi = compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        Ansi = findall(r"\x1B\[[0-?]*[ -/]*[@-~]", text)
        return noAnsi.sub("", text), Ansi

    def _Buffer(self, x, y):
        Buffer = [[" "] * x for _ in range(y)]
        return Buffer

    def _Plotter(self, matrix, y, x, win):
        winy, winx = len(matrix), len(matrix[0])
        for i in range(winy):
            for j in range(winx):
                # Calcular las coordenadas en la matriz grande
                xmain, ymain = x + i, y + j
                # Verificar si las coordenadas están dentro de la amatriz grande
                if 0 <= xmain < len(win) and 0 <= ymain < len(win[0]):
                    win[xmain][ymain] = matrix[i][j]

    def Update(self):
        stdout.buffer.write(bytes("\x1b[H" + '\n'.join([''.join(n) for n in self.Stdscr]), encoding="utf-8"))
        
    def Init(self, width=get_terminal_size().columns, height=get_terminal_size().lines):
        
        self.width, self.height = width, height
        self.Stdscr = self._Buffer(width, height)

        return [0, 0, self.Stdscr] # Return stdscr properties
    
    def Wrapper(self, func, asciiMode=False):
        self.asciiMode = asciiMode
        stdout.buffer.write(b"\x1b[?1049h\x1b[?25l")
        func()
        stdout.buffer.write(b"\x1b[?1049l\x1b[?25h") # Reset to normal

    def Cols(self):
        return self.width
    
    def Lines(self):
        return self.height

    def Clear(self, win=list):
        Win = win[2]
        for i, n in enumerate(Win): # Some weird problem in memory
            Win[i] = [" "] * len(Win[0])
    
    def Win(self, x=int, y=int, x1=int, y1=int):
        height, width = y1 - y, x1 - x
        Win = self._Buffer(width, height)
        return [x, y, Win]
    
    def WinMove(self, x=int, y=int, win=list):
        win[0], win[1] = x, y
    
    def WRefresh(self, win=list):
        x, y, Win = win[0], win[1], win[2]
        self._Plotter(Win, x, y, self.Stdscr)
    
    def Corners(self, win=list, color=""):
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
        Win = win[2]
        toPlot = color + "".join(yourChr[:1]) + "\x1b[0m"
        self._Plotter([[toPlot]], x, y, Win)

    def AddStr(self, x=int, y=int, yourStr=str, win=int, color=""):
        Win = win[2]
        toPlot = [f"{color}{i}\x1b[0m" for i in [*yourStr]]
        self._Plotter([toPlot], x, y, Win)
