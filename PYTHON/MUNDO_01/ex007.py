#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua outra nota: '))
nf= (n1 + n2) / 2
print('A  média entre {:.1f} e {:.1f}  é {:.1f}'.format(n1, n2, nf))


