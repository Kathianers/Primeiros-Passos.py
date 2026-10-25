#LISTA DE EXERCÍCIOS COM IFS - Exercício 01
#BIDU - Votação para saber o melhor dia da semana para realização das lives: segunda, terça, quarta, quinta ou sexta
#Número de colaboradores
#Validar a possibilidade de empate.


colaboradores = int(input("Informe a quantidade de colaboradores na equipe: "))

segunda = 0
terça = 0
quarta = 0
quinta = 0
sexta = 0

for x in range (1, colaboradores +1):
    voto = input("Informe a preferência do colaborador (segunda, terça, quarta, quinta ou sexta): ")
    if voto == "segunda":
        segunda = segunda + 1
    elif voto == "terça":
        terça = terça + 1
    elif voto == "quarta":
        quarta = quarta + 1
    elif voto == "quinta":
        quinta = quinta + 1
    elif voto == "sexta":
        sexta = sexta + 1
    else:
        print("Você informou um dia inválido")

if segunda > terça and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia escolhido foi Segunda-feira")
elif terça > segunda and terça > quarta and terça > quinta and terça > sexta:
    print("O dia escolhido foi Terça-feira")
elif quarta > segunda and quarta > terça and quarta > quinta and quarta > sexta:
    print("O dia escolhido foi Quarta-feira")
elif quinta > segunda and quinta > terça and quinta > quarta and quinta > sexta:
    print("O dia escolhido foi Quinta-feira")
elif sexta > segunda and sexta > terça and sexta > quarta and sexta > quinta:
    print("O dia escolhido foi Sexta-feira")
else:
    print("Houve um empate, realize um novo sorteio")
