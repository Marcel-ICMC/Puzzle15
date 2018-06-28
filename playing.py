from collections import deque
import puzzle15


class Solver():
    def __init__(self):
        self.puzzle = puzzle15.puzzle()
    
    def recreate(original):
        new = Solver()
        new.puzzle.copy(original.puzzle)
        return new

    def Solve(self):
        queue = deque([self])
        aux = Solver()
        aux.puzzle.copy(queue.popleft().puzzle)
        
        while (aux.puzzle.isSolved() == 0):
            if aux.puzzle.moveDown():
                queue.append(Solver.recreate(aux))
                aux.puzzle.moveUp()
            
            if aux.puzzle.moveUp():
                queue.append(Solver.recreate(aux))
                aux.puzzle.moveDown()
            
            if aux.puzzle.moveLeft():
                queue.append(Solver.recreate(aux))
                aux.puzzle.moveRight()
            
            if aux.puzzle.moveRight():
                queue.append(Solver.recreate(aux))
                aux.puzzle.moveLeft()
        
            aux.puzzle.copy(queue.popleft().puzzle)
        
        return aux

x = Solver()
x.puzzle.Shuffle()
x.puzzle.printPuzzle()
print()
x.Solve()
x.puzzle.printPuzzle()
