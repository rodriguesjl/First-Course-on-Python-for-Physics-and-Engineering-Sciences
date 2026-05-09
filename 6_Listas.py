# 1) Faça um programa para ler n valores inteiros positivos ou negativos e armazená-los em uma lista (peça n do usuário). Em seguida imprima:
#a. O índice correspondente ao maior valor da lista
#b. O índice correspondente ao menor valor da lista
#c. A média dos valores positivos

lista = []
soma = 0
cont = 0
indice_m = 0
indice_M = 0
#preenchimento da lista
while True:
    num = input('Digite sair para para parar')
    if num == 'sair':
        break
    else:
        num = int(num)
        lista.append(num)

#particularidades
for i in range(len(lista)):
    if lista[i]>lista[i-1]:
        indice_M = i
    if lista[i]<lista[i-1]:
        indice_m = i
    if lista[i]>=0:
        soma+=lista[i]
        cont+=1

media = soma/cont
print('Maior: %d\nMenor: %d\nMédia: %2.f'%(indice_M,indice_m,media))

# 2) Escreva a função fibonacci() que recebe um valor inteiro n, e retorna uma lista com os n primeiros elementos da sequência de fibonacci. 
#No programa principal, chame a sua função e imprima o resultado.

def fibonacci(n):
    fib_list = [0,1]
    for i in range(2, n):
        termo_i = fib_list[i-2]+fib_list[i-1]
        fib_list.append(termo_i)
    return fib_list
num = int(input('digite o numero'))
print(fibonacci(num))

# 3) Dada uma lista qualquer, encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del Exemplo:
#nums = [19, 22, -10, 4, -2, -3, 5, 6, -17, -4, -1, 67, 98, -23, -6]

nums = [19, 22, -10, 4, -2, -3, 5, 6, -17, -4, -1, 67, 98, -23, -6]
ind_init = 0
final = 0
menor = 0
lista = []

for i in range(len(nums)): 
    if nums[i]<0:
        ind_init = i
        final = i
        for j in range(i+1,len(nums)):
            if nums[j]>=0:
                break
            elif nums[j]<0:
                final +=1
        if (final - ind_init)>menor:
            lista = []
            menor = final - ind_init
            lista.append(ind_init)
            lista.append(final+1)
        
del nums[lista[0]:lista[1]]
print(nums)

# 5) Preencha duas listas (lista1, lista2) com 50 valores inteiros aleatórios de 0 a 100. 
#Em seguida crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas.

import random as rd
lista_1 = [rd.randint(0,100) for i in range(50)]
lista_2 = [rd.randint(0,100) for i in range(50)]
lista_3 = [lista_1[i] for i in range(50) if lista_1[i] in lista_2]
print(lista_1,'\n',lista_2,'\n',lista_3)

# 4) Sabendo que você vai receber strings com nomes de páginas na internet que sempre começam com www. e terminam com .com.br 
#implemente um programa usando somente fatiamento de listas que imprime na tela apenas o nome do site, sem os prefixos e sufixosExemplo:
#Entrada: www.google.com.br
#Saída: google

site = input('Digite o endereço do Site:\n')
nomes = site.split('.')
print(nomes[1:len(nomes)-2])

# 5) Dada uma string, crie uma lista com todos os números contidos nela usando somente compreensão de listas

entrada = 'Isabela tem 2 pássaros e 1 cachorro'
nums = [int(entrada[n]) for n in range(len(entrada)) if (entrada[n].isnumeric())]
print(nums)

# 6) Usando compreensão de listas:
#Gere 100 números inteiros aleatórios entre -50 e 50
#Crie uma lista apenas com os números positivos
#Calcule a média dos números positivos com a segunda lista

import random as rd
lista_1 = [rd.randint(-50,50) for i in range(100)]
lista_2 = [i for i in range(len(lista_1)) if lista_1[i]>=0]
print('Média: %.2f'%(sum(lista_2)/len(lista_2)))

# 7) Receba uma string contendo números separados por vírgula, a quantidade será sempre par. 
#Utilizando compreensão de lista, crie uma lista que contenha a raíz dos números da string. 
#Em seguida, utilize o fatiamento de lista para criar duas listas, 
#uma contendo a primeira metade dos números e a outra contendo a segunda metade e print essas duas listas.

import math as mt
lista = [4,9,16,25,36,49,64,81]
raiz = [mt.sqrt(n) for n in lista]
print(raiz[0:int(len(raiz)/2)],'\n',raiz[int(len(raiz)/2):len(raiz)+1])

# 8) Utilizando a compreensão de listas, crie uma lista com 20 números aleatórios entre -50 e 50. 
#Em seguida, utilize o fatiamento de lista para criar uma outra lista contendo a maior sequência de números positivos da lista original. 
#Em seguida mostre a lista original seguida da lista com a maior sequência de positivos. Observe os exemplos de saída.

lista_rand = [rd.randint(-50,50) for i in range(20)]

ind_init = 0
final = 0
maior = 0
lista = []

for i in range(len(lista_rand)): 
    if lista_rand[i]>0:
        ind_init = i
        final = i
        for j in range(i+1,len(lista_rand)):
            if lista_rand[j]<0:
                break
            elif lista_rand[j]>0:
                final +=1
        if (final - ind_init)>maior:
            lista = []
            maior = final - ind_init
            lista.append(ind_init)
            lista.append(final)

print(lista_rand,'\n',lista_rand[lista[0]:lista[1]])
