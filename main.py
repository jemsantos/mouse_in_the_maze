import queue

from Maze import Maze


def main():
    print(" ")
    print("Mouse in the Maze")

    try:
        # implementa filas de múltiplos produtores e vários consumidores
        nums = queue.Queue()
        nums.put("")
        add = ""
        maze = Maze(2)  # qual dos laberintos criar

        maze.printMaze(add)

        while not maze.findEnd(add):
            add = nums.get()
            # print(add)
            for j in ["L", "R", "U", "D"]:
                put = add + j
                if maze.valid(put):
                    nums.put(put)

    except ValueError as erro:
        print("Erro na execução! Acione o Suporte.")


# metodo main só será executado se "main.py" for executado e não importado
if __name__ == "__main__":
    main()
