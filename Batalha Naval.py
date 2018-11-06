import random

def inicializarGrid():
    grid = []
    for i in range(10):
            linha = []
            for j in range(10):
                    linha.append(".")
            grid.append(linha)
    return grid
                    
def imprimir(grid):
    for i in range(10):
            for j in range(10):
                    print(grid[i][j], end=" ")
            print("\n")

def imprimirHide(grid):
    for i in range(10):
            for j in range(10):
                    if grid[i][j] != 'X' and grid[i][j] != 'x' and grid[i][j] != '.':
                            print('.', end = ' ')
                    else:
                            print(grid[i][j], end = " ")
            print("\n")
                    
def posiciona_porta_avioes(grid, lin, col, pos):
    if not pos and col<6 and lin<10:
            for i in range(col, col+5):
                    if grid[lin][i] != '.':
                            #print('Espaço ocupado!\nVerifique a posição escolhida')
                            return False
            for i in range(col, col+5):
                    grid[lin][i] = "P"
            return True
    elif pos and lin<6 and col<10:
            for i in range(lin, lin+5):
                    if grid[i][col] != '.':
                            #print('Espaço ocupado!\nVerifique a posição escolhida')
                            return False
            for i in range(lin, lin+5):
                    grid[i][col] = "P"
            return True
    else:
            #print("Não é possível posicionar o Porta Aviões")
            return False

def posiciona_encouracado(grid, lin, col, pos):
    if not pos and col<7 and lin<10:
            for i in range(col, col+4):
                    if grid[lin][i] != '.':
                            #print('Espaço ocupado!\nVerifique a posição escolhida')
                            return False
            for i in range(col, col+4):
                    grid[lin][i] = "E"
            return True
    elif pos and lin<7 and col<10:
            for i in range(lin, lin+4):
                    if grid[i][col] != '.':
                            #print('Espaço ocupado!\nVerifique a posição escolhida')
                            return False
            for i in range(lin, lin+4):
                    grid[i][col] = "E"
            return True
    else:
            #print("Não é possível posicionar o Encouraçado")
            return False

def posiciona_cruzador(grid, lin, col, pos):
    if not pos and col<8 and lin<10:
            for i in range(col, col+3):
                    if grid[lin][i] != '.':
                            #print('Espaço ocupado!\nVerifique a posição escolhida')
                            return False
            for i in range(col, col+3):
                    grid[lin][i] = "C"
            return True
    elif pos and lin<8 and col<10:
            for i in range(lin, lin+3):
                    if grid[i][col] != '.':
                            #print('Espaço ocupado!\nVerifique a posição escolhida')
                            return False
            for i in range(lin, lin+3):
                    grid[i][col] = "C"
            return True
    else:
            #print("Não é possível posicionar o Cruzador")
            return False

def posiciona_submarino(grid, lin, col, pos):
    if not pos and col<9 and lin<10:
            for i in range(col, col+2):
                    if grid[lin][i] != '.':
                            #print('Espaço ocupado!\nVerifique a posição escolhida')
                            return False
            for i in range(col, col+2):
                    grid[lin][i] = "S"
            return True
    elif pos and lin<9 and col<10:
            for i in range(lin, lin+2):
                    if grid[i][col] != '.':
                            #print('Espaço ocupado!\nVerifique a posição escolhida')
                            return False
            for i in range(lin, lin+2):
                    grid[i][col] = "S"
            return True
    else:
            #print("Não é possível posicionar o Submarino")
            return False
    
def atirar(grid,lin,col):
    if grid[lin][col] == 'x' or grid[lin][col] == 'X':
            print('Você já atirou nessa posição!')
            return False
    elif grid[lin][col] == '.':
            grid[lin][col] = 'x'
            return True
    else:
            grid[lin][col] = 'X'
            return True

def aleatorio(maximo):
    pos = random.choice([True, False])
    if pos:
            lin = random.randint(0,maximo)
            col = random.randint(0,10)
    else:
            col = random.randint(0,maximo)
            lin = random.randint(0,10)
    return col,lin,pos
            
def preencherAleatorioSubmarino(grid):
    verificador = False
    while verificador == False:
            col,lin,pos = aleatorio(9)
            verificador = posiciona_submarino(grid,lin,col,pos)

def preencherAleatorioCruzador(grid):
    verificador = False
    while verificador == False:
            col,lin,pos = aleatorio(8)
            verificador = posiciona_cruzador(grid,lin,col,pos)

def preencherAleatorioEncouracado(grid):
    verificador = False
    while verificador == False:
            col,lin,pos = aleatorio(7)
            verificador = posiciona_encouracado(grid,lin,col,pos)

def preencherAleatorioPortaAvioes(grid):
    verificador = False
    while verificador == False:
            col,lin,pos = aleatorio(6)
            verificador = posiciona_porta_avioes(grid,lin,col,pos)
    
    
def main():
    grid = inicializarGrid()
    imprimir(grid)
    preencherAleatorioPortaAvioes(grid)
    preencherAleatorioEncouracado(grid)
    preencherAleatorioCruzador(grid)
    preencherAleatorioSubmarino(grid)        
    #print('\n')
    #imprimir(grid)
    '''
    posiciona_porta_avioes(grid,2,2,True)
    posiciona_encouracado(grid,8,2,False)
    posiciona_cruzador(grid,3,4,False)
    posiciona_submarino(grid,0,0,True)
    #Tenta posicionar em posição ocupada
    posiciona_porta_avioes(grid,8,2,False)
    print("\n")
    imprimir(grid)
    imprimirHide(grid)
    '''
    for i in range(20,0,-1):
            verificador = False
            while verificador == False:
                    print('Atirar - Chances: ', i)
                    linha = int(input('Digite a linha: '))
                    coluna = int(input('Digite a coluna: '))
                    verificador = atirar(grid,linha,coluna)
                    imprimirHide(grid)
    print('Fim de Jogo')
    imprimir(grid)

main()
