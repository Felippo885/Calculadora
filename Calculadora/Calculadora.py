def calculate():
    operation = input('''
Digite a operação matemática que você gostaria de completar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um operador válido, por favor execute o programa novamente.')

     # Adicionar novamente () função para calcular() função
    again()

def again():
    calc_again = input('''
Quer calcular de novo?
Por favor, digite S para SIM ou N para NÃO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até logo.')
    else:
        again()

calculate()
    
    
    
    
    
    
    
 