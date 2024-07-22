#ANSI escape sequence para cores no terminal
# \033[style;text;backgroundm
#0 = sem estilo
#1 = negrito
#4 = sublinhado
#7 = negativo (inverter as cores)
#------------------------------------------------
#TEXTO
#30 = branco
#31 = vermelho
#32 = verde
#33 = amarelo
#34 = azul
#35 = magenta
#36 = ciano
#37 = cinza
#------------------------------------------------
#FUNDO
#40 = branco
#41 = vermelho
#42 = verde
#43 = amarelo
#44 = azul
#45 = magenta
#46 = ciano
#47 = cinza
#------------------------------------------------
# Exemplo: \033[0;33;44m (sem estilo; texto amarelo; fundo azul)
# Exemplo: \033[1;31;43m (negrito; texto vermelho; fundo amarelo)
#------------------------------------------------
#aula 11: 
print ('\033[1;31;43mOlá, Mundo!\033[m')
print ('\033[7;30mOlá, Mundo!\033[m')
print ('\033[0;33;44mOlá, Mundo!\033[m')
print ('\033[7;33;44mOlá, Mundo!\033[m')
print ('\033[1;31;43mOlá, Mundo!\033[m')
print ('\033[1;30;43mOlá, Mundo!\033[m')
#------------------------------------------------
nome = input('Qual é o seu nome? ')
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
print(f'Olá! Muito prazer em te conhecer, \033[4;34m{nome}\033[m!')
#------------------------------------------------
