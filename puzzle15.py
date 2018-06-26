import random

#A ideia neste codigo eh implementar o jogo dos 15 ou 15 puzzle
class puzzle():
    #0 eh a posicao livre
    puzzle = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0])
    empty = [3, 3]#ordem em linha, coluna

    #move a posicao vazia para a direita
    def moveRight(self):
        if self.empty[1] != 3:
            self.puzzle[self.empty[0]][self.empty[1]] = self.puzzle[self.empty[0]][self.empty[1] + 1]
            self.puzzle[self.empty[0]][self.empty[1] + 1] = 0
            self.empty[1] = self.empty[1] + 1

    #move a posicao vazia para a esquerda
    def moveLeft(self):
        if self.empty[1] != 0:
            self.puzzle[self.empty[0]][self.empty[1]] = self.puzzle[self.empty[0]][self.empty[1] - 1]
            self.puzzle[self.empty[0]][self.empty[1] - 1] = 0
            self.empty[1] = self.empty[1] - 1

    #move a posicao vazia para cima
    def moveUp(self):
        if self.empty[0] != 0:
            self.puzzle[self.empty[0]][self.empty[1]] = self.puzzle[self.empty[0] - 1][self.empty[1]]
            self.puzzle[self.empty[0] - 1][self.empty[1]] = 0
            self.empty[0] = self.empty[0] - 1
    
    #move a posicao vazia para baixo
    def moveDown(self):
        if self.empty[0] != 3:
            self.puzzle[self.empty[0]][self.empty[1]] = self.puzzle[self.empty[0] + 1][self.empty[1]]
            self.puzzle[self.empty[0] + 1][self.empty[1]] = 0
            self.empty[0] = self.empty[0] + 1

    #mistura todo o quebra-cabeca
    def shuffle(self):
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

    #mostra o atual quebra-cabeca na tela
    def printPuzzle(self):
        for line in range(0, 4):
            for column in range(0, 4):
                print(str(self.puzzle[line][column]), end = ' ')
            print()
