#!/usr/bin/python

N1 = int(input('digite a nota')) * 2
N2 = int(input('digite a nota')) * 3
N3 = int(input('digite a nota')) * 4
N4 = int(input('digite a nota')) * 1

media = [N1+N2+N3+N4/10]
if media >= 7:
    print('voce foi aprovado')
elif media < 5:
    print('aluno reprovado')
else:
    print('aluno em exame')
    