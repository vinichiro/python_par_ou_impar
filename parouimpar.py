import random
from time import sleep

print('\033[31m                             ATENÇÃO!!!!')

print('NESSE JOGO SÓ PODEMOS USAR COISAS ESCRITAS CORRETAMENTE SEMPRE COM ACENTO E SEMPRE MINÚSCULO!!!!')

print('\033[m-'*48)
print('Esse jogo só pode ser jogado com números até 5!')
print('-'*48)

computador = random.randint(1,5)

numero = str(input('Você quer par ou ímpar?!: '))

jogador = int(input('Escreva um número para tentar ganhar do computador!: '))

soma = jogador+computador

print('PAR')
sleep(0.8)
print('OU')
sleep(0.8)
print('ÍMPAR!')
sleep(0.8)

print('-'*20)
print('O computador jogou {}'.format(computador))

print('Você jogou {}'.format(jogador))

print('-'*20)

resultado = ''

if soma % 2 == 0:
    resultado = 'par'
else:
    resultado = 'ímpar'

print('O resulta foi {} e {} é {}'.format(soma, soma, resultado))

if resultado == numero:
    print('Parabéns, você ganhou!')
else:
    print('Você perdeu, mais sorte na próxima!')
