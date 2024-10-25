import os
import time
from termcolor import COLORS, colored
import math 
import random

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsVerticalWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x

    def hitsHorizontalWall(self, point):
        return round(point[1]) < 0 or round(point[1]) >= self._y
    
    def hitsWall(self, point):
        return self.hitsVerticalWall(point) or self.hitsHorizontalWall(point)

    def getReflection(self, point):
        return [-1 if self.hitsVerticalWall(point) else 1, -1 if self.hitsHorizontalWall(point) else 1]

    def setPos(self, pos, mark):
        try:
            self._canvas[round(pos[0])][round(pos[1])] = mark
        except Exception as e:
            raise TerminalScribeException('Could not set position to {} with mark'.format(pos,mark))

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))
    def go(self):
        '''
        Executes a sequence of moves for each scribe in self.scribes, synchronizing them based on the maximum number of moves any scribe has.
        
        For each move index up to the maximum number of moves:
            - Iterates over each scribe.
            - If the scribe has a move at the current index, it executes the move with the provided arguments.
            - Calls the print method to output the current state.
            - Pauses execution for the duration of self.framerate.
        
        Attributes:
            max_moves (int): The maximum number of moves any scribe has.
            i (int): The current move index being processed.
            args (list): The arguments for the current move, including the instance of the class.
        '''
        max_moves = max([len(scribe.moves) for scribe in self.scribes])
        for i in range(max_moves):
            for scribe in self.scribes:
                if len(scribe.moves) > i:
                    args = scribe.moves[i][1]+[self]
                    scribe.moves[i][0](*args)
            self.print()
            time.sleep(self.framerate)
class TerminalScribeException(Exception):
    def __init__(self, message=''):
        super().__init__(colored(message, 'red'))
class InvalidParameterException(TerminalScribeException):
    pass
class CanvasAxis(Canvas):
    # Pads 1-digit numbers with an extra space
    def formatAxisNumber(self, num):
        if num % 5 != 0:
            return '  '
        if num < 10:
            return ' '+str(num)
        return str(num)

    def print(self):
        self.clear()
        for y in range(self._y):
            print(self.formatAxisNumber(y) + ' '.join([col[y] for col in self._canvas]))

        print(' '.join([self.formatAxisNumber(x) for x in range(self._x)]))

class TerminalScribe:
    def __init__(self, canvas, color='red', mark='*', trail='.', pos=(0, 0), framerate=.05, direction=[0, 1]):
        self.moves = []

        if not issubclass(type(canvas),Canvas):
            raise InvalidParameterException('Canvas must be a subclass of Canvas')
        self.canvas = canvas
        if len(trail) != 1 or len(mark) != 1:
            raise InvalidParameterException('Trail and mark must be single characters')
        self.trail = trail
        self.mark = mark
        if not isinstance(framerate, (int, float)):
            raise InvalidParameterException('Framerate must be a number')
        self.framerate = framerate
        if len(pos) != 2:
            raise InvalidParameterException('Position must be a tuple of 2 integers')
        if not all(isinstance(i, int) for i in pos):
            raise InvalidParameterException('Position must be a tuple of 2 integers')
        self.pos = pos
        if color not in COLORS:
            raise InvalidParameterException('Invalid color , choose one of the following: {}'.format(', '.join(COLORS)))
        self.color=color
        self.direction = direction

    def setPosition(self, pos):
        self.pos = pos

    def setDegrees(self, degrees):
        def _setDegrees(self, degrees, _):
            self.direction = self.degreesToUnitDirection(degrees)
        self.moves.append((_setDegrees, [self, degrees]))
        '''
        Adjusts the direction of an object based on its position and the reflection
        properties of the canvas at that position.

        Parameters:
        pos (tuple): The current position of the object on the canvas.

        The method updates the object's direction by multiplying its current direction
        components with the reflection coefficients obtained from the canvas at the given position.
        '''
    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        self.direction = [self.direction[0] * reflection[0], self.direction[1] * reflection[1]]

    def forward(self, distance):
        def _forward(self, canvas):
            pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            if canvas.hitsWall(pos):
                self.bounce(pos, canvas)
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            self.draw(pos, canvas)
        
        for i in range(distance):
            self.moves.append((_forward, [self]))

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, self.color))
        self.canvas.print()
        time.sleep(self.framerate)

class PlotScribe(TerminalScribe):
    def plotX(self, function):
        for x in range(self.canvas._x):
            pos = [x, function(x)]
            if pos[1] and not self.canvas.hitsWall(pos):
                self.draw(pos)

class RobotScribe(TerminalScribe):
    def up(self, distance=1):
        self.direction = [0, -1]
        self.forward(distance)

    def down(self, distance=1):
        self.direction = [0, 1]
        self.forward(distance)

    def right(self, distance=1):
        self.direction = [1, 0]
        self.forward(distance)

    def left(self, distance=1):
        self.direction = [-1, 0]
        self.forward(distance)

    def drawSquare(self, size):
        self.right(size)
        self.down(size)
        self.left(size)
        self.up(size)

class RandomWalkScribe(TerminalScribe):
    def __init__(self, canvas, degrees=135, **kwargs):
        super().__init__(canvas, **kwargs)
        self.degrees = degrees
    
    def randomizeDegreeOrientation(self):
        self.degrees = random.randint(self.degrees-10, self.degrees+10)
        self.setDegrees(self.degrees)
    
    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        if reflection[0] == -1:
            self.degrees = 360 - self.degrees
        if reflection[1] == -1:
            self.degrees = 180 - self.degrees
        self.direction = [self.direction[0] * reflection[0], self.direction[1] * reflection[1]]

    def forward(self, distance):
        for i in range(distance):
            self.randomizeDegreeOrientation()
            super().forward(1)

def sine(x):
    return 5*math.sin(x/4) + 15

def cosine(x):
    return 5*math.cos(x/4) + 15


canvas = CanvasAxis(40, 40)
plotScribe = PlotScribe(canvas)
plotScribe.plotX(sine)

robotScribe = RobotScribe(canvas, color='blue')
robotScribe.drawSquare(10)

randomScribe = RandomWalkScribe(canvas, color='lavander', pos=(0, 0))
randomScribe.forward(100)



