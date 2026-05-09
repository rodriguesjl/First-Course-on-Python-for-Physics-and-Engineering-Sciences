#1) Crie uma função recursiva que recebe um valor inteiro n e calcula o somatório de valores entre 0 e n

def somatorio(n):
    if n==0:
        return 0
    else:
        return n+somatorio(n-1)

x = int(input('Digite o valor a ser somado'))
print('%d é o resultado da soma de %d e seus antecessores'%(somatorio(x),x))

#2) Crie uma função recursiva que recebe dois inteiros k e n e calcula k^2

def exponencial(k,n):
    if n==0:
        return k
    else:
        return k*exponencial(k,n-1)

base = int(input('Digite a base'))
expoente = int(input('Digite o expoente'))
print(exponencial(base,expoente))

#3) Crie uma função recursiva que recebe um inteiro n e calcula a suaquantidade de dígitos.

def qtd(n):
    if n==0:
        return 0
    else:
        return qtd(n//10)+1
x = int(input('Digite o numero que queres saber a quantidade de dígitos'))
print(qtd(x))

#4) Crie uma função recursiva que recebe um inteiro n e informa o nésimo termo da sequência: {3, 5, 7, 9, 11, 13, 15, ... }

def impar(n):
    if n==0:
        return 0
    else:
        return 2 + int(1/n) + impar(n-1)
num = int(input('Digite o valor que queres saber da sequencia'))
print(impar(num))
