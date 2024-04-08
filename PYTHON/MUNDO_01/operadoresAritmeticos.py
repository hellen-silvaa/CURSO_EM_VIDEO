'''
== testar se algo é igual
= atribuir algo, leia-se como "recebe"
operando são os números utilizados na operação
+ -> Adição
- -> Subtração
* -> Multiplicação
/ -> Divisão
**-> Potência
//-> Divisão Inteira
% -> Resto da divisão

Ordem de procedência:
1º ()
2º **
3º '*' -> '/' -> '//' -> '%'
4º '+' -> '-'

nome=input('Diga seu nome: ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
'''

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \no produto é {}, a divisão é {:.3f}'.format(s,m,d), end='')
print('Divisão inteira {} e potência {}'.format(di,e))

# end=' ' -> não quebra linha mesmo tendo 2 prints
# \n -> quebra linha