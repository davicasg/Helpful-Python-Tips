"""
Simulación del juega tic tac toe o triqui

- Se juega contra la maquina, la cual realiza movimiento aleatorios
- El jugador ingresa un número que corresponde a la posición (1-9) que desee jugar
- El juego informa el resultado (empate, gana maquina o gana jugador)
- No es posible jugar en una posición ocupada.
"""

from random import randrange

def DisplayBoard(board):
    """
    La función acepta un parámetro el cual contiene el estado actual del tablero
    y lo muestra en la consola.
    """
    for x in board:
        print('+','+','+','+',sep=7*"-")
        print('|','|','|','|',sep=7*" ")
        for y in x:
            print('|',y,'',sep="   ",end='')
        print()
        print('|','|','|','|',sep=7*" ")
    print('+','+','+','+',sep=7*"-")
    return board

def EnterMove(board):
    """
    La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    """
    while True:
        try:
            pos = int(input('Ingresa tu movimiento o el número 0 para terminar: '))
            if pos == 0:
                return True
        except:
            print('Ingresa un número entre el 1 y el 9')
            continue
        if pos >= 1 and pos <= 9:
            if type(pos) is int:
                if pos >= 1 and pos <=3:
                    if type(board[0][pos-1]) is int:
                        board[0][pos-1] = 'O'
                        return board
                    
                elif pos >= 4 and pos <=6:
                    if type(board[1][pos-4]) is int:
                        board[1][pos-4] = 'O'
                        return board
                    
                else:
                    if type(board[2][pos-7]) is int:
                        board[2][pos-7] = 'O'
                        return board
                    
                print('Posición ocupada, verifique el tablero e ingrese un movimiento válido ')
        else:
            print('Posición fuera del rango, verifique e intente de nuevo')
    
        
def MakeListOfFreeFields(board):
    """    
    La función examina el tablero y construye una lista de todos los cuadros vacíos.
    La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    """
    for x in board:
        for y in x:
            if type(y) is int:
                return True#Jugadas disponible
    return False#Tablero lleno

def VictoryFor(board,sign):
    """
    La función analiza el estatus del tablero para verificar si
    el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    """
    
    if board[0][0] == sign and board [0][1] == sign and board[0][2] == sign:
        if sign == 'X':
            return 'Machine WIN'
        else:
            return 'Ganaste !!!'
    
    if board[1][0] == sign and board [1][1] == sign and board[1][2] == sign:
        if sign == 'X':
            return 'Machine WIN'
        else:
            return 'Ganaste !!!'
            
    if board[2][0] == sign and board [2][1] == sign and board[2][2] == sign:
        if sign == 'X':
            return 'Machine WIN'
        else:
            return 'Ganaste !!!'
            
    if board[0][0] == sign and board [1][0] == sign and board[2][0] == sign:
        if sign == 'X':
            return 'Machine WIN'
        else:
            return 'Ganaste !!!'
            
    if board[0][1] == sign and board [1][1] == sign and board[2][1] == sign:
        if sign == 'X':
            return 'Machine WIN'
        else:
            return 'Ganaste !!!'
                    
    if board[0][2] == sign and board [1][2] == sign and board[2][2] == sign:
        if sign == 'X':
            return 'Machine WIN'
        else:
            return 'Ganaste !!!'
                
    if board[0][0] == sign and board [1][1] == sign and board[2][2] == sign:
        if sign == 'X':
            return 'Machine WIN'
        else:
            return 'Ganaste !!!'
    
                
    if board[0][2] == sign and board [1][1] == sign and board[2][0] == sign:
        if sign == 'X':
            return 'Machine WIN'
        else:
            return 'Ganaste !!!'
    
    return False


def DrawMove(board):
    """
    La función dibuja el movimiento de la máquina y actualiza el tablero.
    """
    
    while True :
        pos = randrange(1,10)
        if pos >= 1 and pos <=3:
            if type(board[0][pos-1]) is int:
                board[0][pos-1] = 'X'
                return board
            continue
        elif pos >= 4 and pos <=6:
            if type(board[1][pos-4]) is int:
                board[1][pos-4] = 'X'
                return board
            continue
        else:
            if type(board[2][pos-7]) is int:
                board[2][pos-7] = 'X'
                return board
            continue

##/////****//////*****##

board = [[1,2,3],[4,'X',6],[7,8,9]]
print('Inicia el juego, comienza la maquina:')
DisplayBoard(board)#First Movement 
while True:
    
    if MakeListOfFreeFields(board) is False:
        print('Juego terminado, Empate')
        break

    mov_user = EnterMove(board)#Movimiento del usuario
    if mov_user is True:
        print('Has terminado el juego !')
        break
    print('Tu jugada:')
    upt_board = DisplayBoard(mov_user)#Dibuja la jugada del usuario
    win_user = VictoryFor(upt_board,'O')#Se valida si el usuario ganó

    if win_user:
        print(win_user)
        break
    if MakeListOfFreeFields(board) is False:
        print('Juego terminado, Empate')
        break
    
    print('Turno de la maquina:')
    mov_machine = DrawMove(upt_board)#Movimiento de la maquina
    upt_board = DisplayBoard(mov_machine)#Dibuja la jugada de la maquina
    win_machine = VictoryFor(upt_board,'X')#Se valida si la maquina ganó
    if win_machine:
        print(win_machine)
        break