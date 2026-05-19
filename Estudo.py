# Essa é uma calculadora de desconto e aumento em %.
# This is a discount and markup calculator in %

Operador = input('Escolha um operador (+ para adicionar e - para subtrair): ')
Valor = float(input('Digite um valor: '))
Porcentagem = float(input('Digite um valor para porcentagem: '))

# Após o usuário escolher o operador e os valores.
# After the user selects the operator and the values

# a máquina faz o resto do processo.
# After the user selects the operator and the values, the machine completes the rest of the process)

if Operador == '+':


    resultado = Valor + (Valor * Porcentagem / 100)

    print(f'O valor com aumento foi de R${resultado:.2f}')

#Esse aqui foi o de soma
#This one was the sum.

elif Operador == '-':

    resultado = Valor - (Valor * Porcentagem / 100)

    print(f'O valor com desconto foi de R${resultado:.2f}')

#Esse o de subtração
#That's the one for subtraction.

else:
    print('Operador inválido')

    #Esse em caso de um inválido

    # This system could be used in:
    # - stores
    # - supermarkets
    # - salary adjustments
    # - e-commerce promotions

    # Esse sistema poderia ser usado em:
    # - lojas
    # - supermercados
    # - reajuste salarial
    # - promoções em e-commerce

#Caso encontre algo para melhorar e/ou corrigir , mande um feedback.
#If you find anything to improve and/or correct, please send feedback.

#By Hugofreitaspy