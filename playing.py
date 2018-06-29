from collections import deque
import puzzle15


class Solver():
    def __init__(self):
        self.puzzle = puzzle15.puzzle()
        self.moves = "FLAG"

    #retorna a string com todos os movimentos feitos
    def getMoves(self):
        return self.moves

    def addMove(self, move):
        self.moves = self.moves + move

    def deleteMove(self):
        self.moves = self.moves[:- 1]

    #recria um solver e retorna a copia
    def recreate(original):
        new = Solver()
        new.puzzle.copy(original.puzzle)
        new.moves = original.moves

        return new

    #printa o estado em que a solucao esta
    def printSolution(self):
        print("It takes " + str(len(self.moves) - 4) + "moves  " + self.moves[4:])
        self.puzzle.printPuzzle()

    def Solve(self):
        queue = deque([self])
        aux = Solver()
        aux.puzzle.copy(queue.popleft().puzzle)
        
        while (aux.puzzle.isSolved() == 0):
            if aux.moves[-1] != 'U' and aux.puzzle.moveDown():
                aux.addMove("D")
                queue.append(Solver.recreate(aux))
                aux.puzzle.moveUp()
                aux.deleteMove()
            
            if aux.moves[-1] != 'D' and aux.puzzle.moveUp():
                aux.addMove("U")
                queue.append(Solver.recreate(aux))
                aux.deleteMove()
                aux.puzzle.moveDown()
            
            if aux.moves[-1] != 'R' and aux.puzzle.moveLeft():
                aux.addMove("L")
                queue.append(Solver.recreate(aux))
                aux.deleteMove()
                aux.puzzle.moveRight()
            
            if aux.moves[-1] != 'L' and aux.puzzle.moveRight():
                aux.addMove("R")
                queue.append(Solver.recreate(aux))
                aux.deleteMove()
                aux.puzzle.moveLeft()
        
            aux = Solver.recreate(queue.popleft())
            

        return aux

x = Solver()
x.puzzle.Shuffle()
x.puzzle.printPuzzle()
print()
solved = x.Solve()
solved.printSolution()
