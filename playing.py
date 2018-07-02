from math import ceil
from queue import PriorityQueue
from collections import deque
import puzzle15


class Solver():
	def __init__(self):
		self.puzzle = puzzle15.puzzle()
		self.moves = "FLAG"

	def __lt__(self, other):
		if self.moves[-1] == other.moves[-1]:
			return False
		return self.moves[-1] < other.moves[-1]

	#retorna a string com todos os movimentos feitos
	def getMoves(self):
		return self.moves

	#adiciona um movimento a string moves
	def addMove(self, move):
		self.moves = self.moves + move

	#deleta o ultimo movimento feito
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
		print("It takes " + str(len(self.moves) - 4) + " moves  " + self.moves[4:])
		self.puzzle.printPuzzle()

	#solver de forca bruta
	def BFSolver(self):
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

	#retorna a soma das diferencas entre coluna e linha atual e a coluna ideal de num
	def distanceSolution(self, num, line, column):
		nline = ceil((num-1)/4)
		ncolumn = (num - 1) % 4

		return abs(line - nline) + abs(column - ncolumn)

        #retorna quantos estao fora de sua posicao
	#mais a quantidade atual de movimentos necessarios para chegar nesta situacao
	def heuristicSolution(self):
		counter = 0
		for line in range(0, 4):
			for column in range(0,4):
				#if self.puzzle.puzzle[line][column] == (line*4) + column + 1:
				#	counter += 1
				counter += self.distanceSolution(self.puzzle.puzzle[line][column], line, column)
		return int(counter) + int(len(self.moves))

	def heuristicSolver(self):
		heap = PriorityQueue()
		aux = []
		heap.put((self.heuristicSolution(), Solver.recreate(self)))
		aux = heap.get()

		while len(aux[1].moves) < 100:
			#print(str(aux[0]))
			#print(str(len(aux[1].moves)))
			#print("\n")
			#aux[1].puzzle.printPuzzle()
			#print("\n")
			if aux[1].moves[-1] != 'U' and aux[1].puzzle.moveDown():
				aux[1].addMove("D")
				heap.put((aux[1].heuristicSolution(), Solver.recreate(aux[1])))
				aux[1].puzzle.moveUp()
				aux[1].deleteMove()
            
			if aux[1].moves[-1] != 'D' and aux[1].puzzle.moveUp():
				aux[1].addMove("U")
				heap.put((aux[1].heuristicSolution(), Solver.recreate(aux[1])))
				aux[1].deleteMove()
				aux[1].puzzle.moveDown()
            
			if aux[1].moves[-1] != 'R' and aux[1].puzzle.moveLeft():
				aux[1].addMove("L")
				heap.put((aux[1].heuristicSolution(), Solver.recreate(aux[1])))
				aux[1].deleteMove()
				aux[1].puzzle.moveRight()
            
			if aux[1].moves[-1] != 'L' and aux[1].puzzle.moveRight():
				aux[1].addMove("R")
				heap.put((aux[1].heuristicSolution(), Solver.recreate(aux[1])))
				aux[1].deleteMove()
				aux[1].puzzle.moveLeft()
			
			aux = heap.get()		
			if aux[1].puzzle.isSolved():
				break
		return aux

	#esta funcao calcula e retorna um deque de todos os movimentos possiveis ate um numero n de passos
	def BFSolver(self):
		queue = deque([self])
		aux = Solver()
		aux.puzzle.copy(queue.popleft().puzzle)
		nmoves = 0        

		while (aux[0] < 5):
			if aux.moves[-1] != 'U' and aux.puzzle.moveDown():
				aux.addMove("D")
				queue.append((aux[0] + 1, Solver.recreate(aux)))
				aux.puzzle.moveUp()
				aux.deleteMove()
            
			if aux.moves[-1] != 'D' and aux.puzzle.moveUp():
				aux.addMove("U")
				queue.append((aux[0] + 1, Solver.recreate(aux)))
				aux.deleteMove()
				aux.puzzle.moveDown()
            
			if aux.moves[-1] != 'R' and aux.puzzle.moveLeft():
				aux.addMove("L")
				queue.append((aux[0] + 1, Solver.recreate(aux)))
				aux.deleteMove()
				aux.puzzle.moveRight()
            
			if aux.moves[-1] != 'L' and aux.puzzle.moveRight():
				aux.addMove("R")
				queue.append((aux[0] + 1, Solver.recreate(aux)))
				aux.deleteMove()
				aux.puzzle.moveLeft()

			aux = Solver.recreate(queue.popleft())
		return aux

	    
x = Solver()
x.puzzle.setPuzzle(([0, 15, 9, 2], [10, 12, 11, 6], [5, 7, 13, 4], [1, 14, 3, 8]), [0, 0,])
#x.puzzle.Shuffle()
#x.puzzle.moveUp()
#x.puzzle.moveLeft()
#x.puzzle.moveUp()
x.puzzle.printPuzzle()
print()
solved = x.heuristicSolver()
solved[1].printSolution()
