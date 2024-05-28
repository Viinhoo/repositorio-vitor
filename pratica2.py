numeros = int

numero1 = input("primeiro numero: ")
int1 = int(numero1)
numero2 = input('segundo numero: ')
int2 = int(numero2)
numero3 = input('terceiro numero: ')
int3 = int(numero3)

if int3 >= 1:
    print('Deseja continuar? ')
numero4 = input('se sim, digite o quarto numero, se nao, digite "0": ')
int4 = int(numero4)

if int4 >= 1:
    print('À partir de agora, você vai receber uma confirmação se irá querer continuar ou caucular, para isso, pressione enter quando o mesmo aparecer')
    print(input('PRESSIONE ENTER'))

elif numero4 == '0':
    print((f'Sua média é de: {(int1 + int2 + int3) / 3:.2f}')), exit()

confirmacao = input('"C" continuar e "CC" para caucular: ')
if confirmacao == 'C':
    print(input('PRESSIONE ENTER'))

elif confirmacao == 'CC':
    print((f'Sua média é de: {(int1 + int2 + int3 + int4) / 4:.2f}')), exit()

numero5 = input('quinto numero: ')
int5 = int(numero5)

if int5 >= 1:
    print(input('PRESSIONE ENTER'))
else:
    print('#ERRO#')

ccc = input('"C" para continuar e "CC" para caucular: ' )

if ccc == 'C':
    print(input('PRESSIONE ENTER)'))
elif ccc == 'CC':
    print((f'Sua média é de: {(int1 + int2 + int3 + int4 + int5) / 5:.2f}')), exit()

numero6 = input('sexto numero: ') 
int6 = int(numero6)

if int6 >= 1:
    print(input('PRESSIONE ENTER'))
else:
    print('#ERRO#')

CCC1 = input('"C" para continuar e "CC" para caucular: ' )

if CCC1 == "C":
    print(input('PRESSIONE ENTER'))
elif CCC1 == 'CC':
    print((f'Sua média é de: {(int1 + int2 + int3 + int4 + int5 + int6) / 6:.2f}')), exit()

numero7 = input('setimo numero: ') 
int7 = int(numero7)

if int7 >= 1:
    print(input('PRESSIONE ENTER'))
else:
    print('#ERRO#')

CCC2 = input('"C" para continuar e "CC" para caucular: ' )
if CCC2 == "C":
    print(input('PRESSIONE ENTER'))
elif CCC2 == 'CC':
    print((f'Sua média é de: {(int1 + int2 + int3 + int4 + int5 + int6 + int7) / 7:.2f}')), exit()

numero8 = input('oitavo numero: ') 
int8 = int(numero8)

if int8 >= 1:
    print(input('PRESSIONE ENTER'))
else:
    print('#ERRO#')

CCC3 = input('"C" para continuar e "CC" para caucular: ' )
if CCC3 == "C":
    print(input('PRESSIONE ENTER'))
elif CCC3 == 'CC':
    print((f'Sua média é de: {(int1 + int2 + int3 + int4 + int5 + int6 + int7 + int8) / 8:.2f}')), exit()

numero9 = input('nono numero: ') 
int9 = int(numero9)

if int9 >= 1:
    print(input('PRESSIONE ENTER'))
else:
    print('#ERRO#')

CCC4 = input('"C" para continuar e "CC" para caucular: ' )
if CCC4 == "C":
    print(input('PRESSIONE ENTER'))
elif CCC4 == 'CC':
    print((f'Sua média é de: {(int1 + int2 + int3 + int4 + int5 + int6 + int7 + int8 + int9) / 9:.2f}')), exit()
    
numero10 = input('decimo numero: ') 
int10 = int(numero10)

if int10 >= 1:
    print(input('PRESSIONE ENTER'))
else:
    print('#ERRO#')

CCC5 = input('"C" para continuar e "CC" para caucular: ' )
if CCC5 == "C":
    print(input('PRESSIONE ENTER'))
elif CCC5 == 'CC':
    print((f'Sua média é de: {(int1 + int2 + int3 + int4 + int5 + int6 + int7 + int8 + int9 + int10) / 10:.2f}')), exit()