
def seven_segment_display(number_to_print:str)->str:
    """
    Función que imprime un número entero no negativo ingresado 
    por el usuario simulando un display 7 segmentos. Así:

        # ### ### # # ### ### ### ### ### ### 
      # #   #   # # # #   #     # # # # # # # 
        # ### ### ### ### ###   # ### ### # # 
        # #     #   #   # # #   # # #   # # # 
        # ### ###   # ### ###   # ### ### ###
    """
    row = 0
    line = []
    total = []
    end = 3
    start = 0
    jumps = [x for x in range(4,1000,3)]
    digits = {
        '0': [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1],
        '1': [0,0,1,1,0,1,0,0,1,0,0,1,0,0,1],
        '2': [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1],
        '3': [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1],
        '4': [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1],
        '5': [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1],
        '6': [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1],
        '7': [1,1,1,0,0,1,0,0,1,0,0,1,0,0,1],
        '8': [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1],
        '9': [1,1,1,1,0,1,1,1,1,0,0,1,1,1,1],
    }

    for r in range(5):
        for n in number_to_print:
            for d in digits[n][start:end]:
                line.append(d)
        end += 3
        start += 3
        total.append(line.copy())
        line = []

    for x in total:
        counter = 1
        for i in x:
            if counter in jumps:
                print(' ', end='')
            if row >= len(x):
                print()
                row = 0
            if i:
                print('#', end='')
            else:
                print(' ', end='')
            row += 1
            counter += 1

is_not_number = True
while is_not_number:
    value = input('Input a number: ')
    if value.isdigit():
        is_not_number = False
        seven_segment_display(value)
    elif value == 'q' or value == 'Q':
        print('  Turned off 7 segment Display :(')
        quit()
    else:
        print('Value should be a number, try again or exit typping letter Q.',end=' ')