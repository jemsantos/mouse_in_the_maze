# maze, mouse, cheese
# labirinto, rato, queijo


class Maze:

    def __init__(self, cod_maze=1, row=9, column=7):
        self._row = row
        self._column = column
        self._cod_maze = cod_maze
        self._maze = []

        if cod_maze == 1:
            self.createMaze1()
        elif cod_maze == 2:
            self.createMaze2()

        print(f"Laberinto Iniciado com as dimensões: {self._row} X {self._column}")
        print(" ")

    def getMaze(self) -> list:
        return self._maze

    def createMaze1(self) -> None:
        self._maze.append(["#", "#", "#", "#", "#", "M", "#"])
        self._maze.append(["#", " ", " ", " ", "#", " ", "#"])
        self._maze.append(["#", " ", "#", " ", "#", " ", "#"])
        self._maze.append(["#", " ", "#", " ", " ", " ", "#"])
        self._maze.append(["#", "C", "#", "#", "#", " ", "#"])
        self._maze.append(["#", " ", "#", "#", " ", "#", "#"])
        self._maze.append(["#", " ", " ", " ", "#", " ", "#"])
        self._maze.append(["#", " ", " ", " ", " ", " ", "#"])
        self._maze.append(["#", "#", "#", "#", "#", "#", "#"])

    def createMaze2(self) -> None:
        self._maze.append(["#", "#", "#", "#", "#", "M", "#", "#", "#"])
        self._maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
        self._maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
        self._maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
        self._maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
        self._maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
        self._maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
        self._maze.append(["#", " ", "#", " ", "#", " ", "#", "C", "#"])
        self._maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
        self._maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
        self._maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
        self._maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#"])

    def valid(self, moves) -> bool:
        start = 0
        for x, pos in enumerate(self._maze[0]):
            if pos == "P":
                start = x

        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
            if not (0 <= i < len(self._maze[0]) and 0 <= j < len(self._maze)):
                return False
            elif self._maze[j][i] == "#":
                return False

        return True

    def printMaze(self, path="") -> None:
        start = 0
        for x, pos in enumerate(self._maze[0]):
            if pos == "P":
                start = x

        i = start
        j = 0
        pos = set()
        for move in path:
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
            pos.add((j, i))

        for j, row in enumerate(self._maze):
            for i, col in enumerate(row):
                if (j, i) in pos:
                    print("+ ", end="")
                else:
                    print(col + " ", end="")
            print()

    def findEnd(self, moves) -> bool:
        start = 0
        for x, pos in enumerate(self._maze[0]):
            print(x, pos)

            if pos == "P":
                start = x

        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1

        if self._maze[j][i] == "Q":
            print("Found: " + moves)
            self.printMaze(self._maze, moves)
            return True

        return False

    def __str__(self):
        return f"Laberinto com as dimensões: {self._row} X {self._column}"
