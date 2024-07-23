#Condições Aninhadas sãp condições dentro de outras condições

#elif é a junção de else com if, ou seja, se a primeira condição não for atendida, ele verifica a segunda condição
#------------------------------------------------
#aula 12:
nome = str(input('Qual é o seu nome?'))
if nome == 'Hellen':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')