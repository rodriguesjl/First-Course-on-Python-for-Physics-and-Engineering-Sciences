# 1) Você fará um programa que recebe uma string no formato CSV referente a transações entre clientes de um banco e retorna o saldo de cada cliente. 
# Para isso, crie um dicionário e adicione os clientes a medida que eles apareçam no CSV. 
# Para novos clientes adicionados, assuma saldo inicial de 10000 (dez mil reais).

corda = (
            'joao;maria;5000.00\njose;joao;100.00\nmaria;joana;1300.00\njoana;jose;2200.00\njose;joao;100.00\n'
            'jose;joao;100.00\njose;joao;100.00\njose;joana;500.00\nmaria;jose;1123.50\njose;joao;100.00\n'
            'maria;joana;1300.00\njoana;jose;1200.00\n'
        )
nomes = {}

lista = corda.split('\n')
lista = [lista[i].split(';') for i in range(len(lista))]
lista.pop(-1)

for i in range(len(lista)):
    nomes[lista[i][0]] = nomes.get(lista[i][0],10000) - float(lista[i][2])
    
for j in range(len(lista)):
    nomes[lista[i][1]] = nomes.get(lista[i][1],nomes[lista[j][1]])+float(lista[i][2])
    
print(nomes)

##########################################################################################################################################

# 2) 2. Devido a cortes financeiros, a Universidade Monstros S.A. não vai conseguir pagar a bolsa de todos os monstrinhos. 
#Sua função é desenvolver um programa para definir quais dos monstrinhos aprovados com bolsa realmente vão receber o seu pagamento.

#Seu programa vai receber um conjunto de entradas também no formato CSV, 
#onde cada linha contém o nome do monstro e o status de aprovação de bolsa: APROVADO ou REPROVADO.

#Entrada 1:

#Boo;APROVADO\nMike;REPROVADO\nSullivan;APROVADO\nFungus;APROVADO
#nCelia;APROVADO\nRex;REPROVADO\nRoz;APROVADO\nBoggs;REPROVADO\nSq uibbles;APROVADO

#Com essas informações, crie uma lista de tuplas: [(Nome1, Status1), (Nome2, Status2), ...]

#Para te ajudar na decisão, te enviaram em seguida as notas de cada monstro no PosComp, critério escolhido para desempate.

#Entrada 2:

#Boo;35.20\nMike;33.40\nSullivan;27.9\nFungus;30.30\nCelia;26.60\n Rex;28.0\nRoz;24.90\nBoggs;35.10\nSquibbles;32.70


candidatos = (
                'Boo;APROVADO\nMike;REPROVADO\nSullivan;APROVADO\nFungus;APROVADO'
                '\nCelia;APROVADO\nRex;REPROVADO\nRoz;APROVADO\nBoggs;REPROVADO\nSquibbles;APROVADO'
            )

lista = candidatos.split('\n')
lista = [lista[i].split(';') for i in range(len(lista))]

dicio = {}
for v,k in lista:
    dicio[v] = k
situ = dicio.items()

Notas = 'Boo;35.20\nMike;33.40\nSullivan;27.9\nFungus;30.30\nCelia;26.60\nRex;28.0\nRoz;24.90\nBoggs;35.10\nSquibbles;32.70'
lista_notas = Notas.split('\n')
lista_notas = [lista_notas[i].split(';') for i in range(len(lista_notas))]

notas = {}

for i in range(len(lista_notas)):
    if dicio[lista_notas[i][0]] == 'APROVADO':
        notas[lista_notas[i][1]] = notas.get(lista_notas[i][1],lista_notas[i][0])

tps = sorted(notas.items(), reverse = True)
del tps[int(len(tps)/2):len(tps)]

contemplados = {}
for k,v in tps:
    contemplados[k] = v

print('Os contemplados foram: {}'.format(', '.join(contemplados.values())))
Com essas informações, crie um dicionário onde os nomes dos candidatos são as chaves e o conteúdo é a sua nota do PosComp. Exemplo: { “Boo”: 35.20, “Mike”: 28.80 }

Sabendo que apenas 50% dos aprovados poderão receber a bolsa, e que elas serão atribuídas para os aprovados com as maiores notas, imprima os nomes dos contemplados.
