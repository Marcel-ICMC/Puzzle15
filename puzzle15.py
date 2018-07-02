import random

#A ideia neste codigo eh implementar o jogo dos 15 ou 15 puzzle
class puzzle():
    #0 eh a posicao livre
    def __init__(self):
        self.puzzle = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0])
        self.empty = [3, 3]#ordem em linha, coluna

    def setPuzzle(self, p, e):
        self.puzzle = p
        self.empty = e

    def getPuzzle(self):
        return self.puzzle

    def getEmpty(self):
        return self.empty

    def copy(self, original):
        for line in range(0, 4):
            for column in range(0, 4):
                self.puzzle[line][column] = original.puzzle[line][column]
        self.empty[0] = original.empty[0]
        self.empty[1] = original.empty[1]


    #Os quatro metodos de movimentacao retornam 1 se moveu e 0 se nao eh possivel mover
    #move a posicao vazia para a direita
    def moveRight(self):
        if self.empty[1] != 3:
            self.puzzle[self.empty[0]][self.empty[1]] = self.puzzle[self.empty[0]][self.empty[1] + 1]
            self.puzzle[self.empty[0]][self.empty[1] + 1] = 0
            self.empty[1] = self.empty[1] + 1
            return 1
        return 0
    
    #move a posicao vazia para a esquerda
    def moveLeft(self):
        if self.empty[1] != 0:
            self.puzzle[self.empty[0]][self.empty[1]] = self.puzzle[self.empty[0]][self.empty[1] - 1]
            self.puzzle[self.empty[0]][self.empty[1] - 1] = 0
            self.empty[1] = self.empty[1] - 1
            return 1
        return 0

    #move a posicao vazia para cima
    def moveUp(self):
        if self.empty[0] != 0:
            self.puzzle[self.empty[0]][self.empty[1]] = self.puzzle[self.empty[0] - 1][self.empty[1]]
            self.puzzle[self.empty[0] - 1][self.empty[1]] = 0
            self.empty[0] = self.empty[0] - 1
            return 1
        return 0

    #move a posicao vazia para baixo
    def moveDown(self):
        if self.empty[0] != 3:
            self.puzzle[self.empty[0]][self.empty[1]] = self.puzzle[self.empty[0] + 1][self.empty[1]]
            self.puzzle[self.empty[0] + 1][self.empty[1]] = 0
            self.empty[0] = self.empty[0] + 1
            return 1
        return 0

    #mistura todo o quebra-cabeca
    def Shuffle(self):
        for moves in range(0, 100):
            rand = random.randint(0,3)
            if rand == 0:
                self.moveRight()
            if rand == 1:
                self.moveLeft()
            if rand == 2:
                self.moveUp()
            if rand == 3:
                self.moveDown()

    def isSolved(self):
        if(self.puzzle == ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0])):
            return 1
        return 0

    #mostra o atual quebra-cabeca na tela
    def printPuzzle(self):
        for line in range(0, 4):
            for column in range(0, 4):
                print(str(self.puzzle[line][column]), end = " ")
            print()
