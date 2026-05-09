#1) Escreva um programa que calcula o fatorial de um valor n (n!) dado pelo usuário.

num = int(input('Digite o fatorial'))
fat = 1
n = 0
while n<num:
    n+=1
    fat*=n

print('O fatorial do número é: ',fat)

################################################################################################################################################################

#2) Escreva um programa que leia um valor inteiro e imprima a soma de todos os inteiros pares de zero até esse valor.

num = int(input('Digite o número'))
n = 0
soma = 0
while n<num:
    n+=1
    if(n%2==0):
        soma+=n

print('Soma dos pares: ',soma)

################################################################################################################################################################

#3) Escreva um programa para ler n valores inteiros e calcular a média apenas dos valores positivos (ignorando qualquer valor negativo).
#Nota: O valor de n não será informado, implemente um laço que realize leituras até que o usuário digite um valor flag (flag: 0). 
#A flag é apenas um valor pré-definido que indica o fim das entradas, interrompendo o laço de leitura.

media = 0
soma = 0
while True:
    x = int(input('Digite um número'))
    
    if(x==0):
        break
    elif (x>=0):
        soma +=x
        media+=1
        print('Soma:',soma)
        print('razao:',media)
        
print('Média dos números pares:',soma/media)

################################################################################################################################################################

#4) Crie uma função menu ( ) que imprima na tela o menu de opções a seguir e retorne o valor digitado pelo usuário. 
#Sua função deve verificar se o valor digitado é válido, e caso não seja, pedir que o usuário digite um novo valor.

#>Adição
#>Subtração
#>Multiplicação
#>Divisão
#>Saída

#Ao retornar da chamada da função, você deve solicitar do usuário os números que serão operados, 
#exibir o resultado da expressão escolhida e retornar ao menu de opções. O programa só termina quando for escolhida a opção 5 (saída)

def menu():

    while True:
        x = int(input("Digite o número associado à operação desejada\n 1. Adição\n 2. Subtração\n 3. Multiplicação\n 4. Divisão\n 5. Saída \n"))
        if (x==5):
            break
        elif (x==1):
            alg_1 = int(input('Digite o primeiro algarismo'))
            alg_2 = int(input('Digite o segundo algarismo'))
            print('%d + %d = %d \n'% (alg_1, alg_2, alg_1+alg_2))
        elif (x==2):
            alg_1 = int(input('Digite o primeiro algarismo'))
            alg_2 = int(input('Digite o segundo algarismo'))
            print('%d - %d = %d \n'% (alg_1, alg_2, alg_1-alg_2))
        elif (x==3):
            alg_1 = int(input('Digite o primeiro algarismo'))
            alg_2 = int(input('Digite o segundo algarismo'))
            print('%d x %d = %d \n'% (alg_1, alg_2, alg_1*alg_2))
        elif (x==4):
            alg_1 = int(input('Digite o primeiro algarismo'))
            alg_2 = int(input('Digite o segundo algarismo'))
            if (alg_2==0):
                print('DIVISÃO POR ZERO! \n')
            else:
                print('%d ÷ %d = %.2f \n'% (alg_1, alg_2, alg_1/alg_2))
menu()
print('FIM - OBRIGADO POR USAR')                                                                                                    

################################################################################################################################################################

#5) Escreva uma função intitulada *floyd* que recebe um número positivo N e imprime N linhas do triângulo de Floyd. 
#Escreva também o programa principal para ler *N* do usuário. <br>
#Nota: O triângulo de Floyd é um triângulo retângulo formado por números naturais. 
#Para criá-lo, basta iniciar a primeira linha com o número 1 e incrementar a quantidade de elementos das linhas subsequentes, 
#bem como os valores contidos nas linhas.

Exemplo:

Entrada:
    6
Saida:
    1 
    2 3 
    4 5 6 
    7 8 9 10 
    11 12 13 14 15 
    16 17 18 19 20 21 

def floyd(n):
    k=0
    for i in range(1,n+1):
        conc = ''
        for j in range(i):
            k+=1
            conc += str(k)+' '
        print(conc)
    return ''

A = int(input('Entre com a quantidade de linhas do triângulo'))
print(floyd(A))

################################################################################################################################################################

#6) Escreva uma função chamada escalas que recebe três parâmetros: inicio, fim e passo, referentes a um intervalo de temperatura em graus Celsius. 
#Sua função deve imprimir n linhas contendo uma tabela de conversão de graus Celsius para Fahrenheit e Kelvin nessa ordem. 
#Escreva também o código principal (fora da função) onde os valores inicio, fim e passo serão lidos do usuário.

print('Entrada:')

inicio = int(input(''))
fim = int(input(''))
passo = int(input(''))
print('Celsius | Fahrenheit | Kelvin\n--------------------')


for i in range(inicio, fim+1, passo):
    far = (i*(9/5))+32
    kel = i+273
    print(i,'   |',far,'   |',kel)
  
################################################################################################################################################################

#7) Escreva a função mdc4(a,b,c,d) que retorna o máximo divisor comum entre a, b, c e d.

def mdc(A,B,C):
    a = 0
    if (A>B) and (A>C):
        for i in range(1,A+1):
            if (A%i==0) and (B%i==0) and (C%i==0):
                a=i
    elif (B>A) and (B>C):
        for i in range(1,B+1):
            if (A%i==0) and (B%i==0) and (C%i==0):
                a=i
    elif (C>A) and (C>B):
        for i in range(1,C+1):
            if (A%i==0) and (B%i==0) and (C%i==0):
                a=i
    return a

A = int(input('Digite o primeiro número'))
B = int(input('Digite o segundo número'))
C = int(input('Digite o terceiro número'))

print(mdc(A,B,C))

################################################################################################################################################################

#8) Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de 1.5%. 
#A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. 
#Faça um programa que determine o salário atual do funcionário.

ano = 1998
sal_init = 2000
sal_aume = (0.015*sal_init)
print('Aumento: ',sal_aume)
aumento = 1
while ano<=2026:
    ano+=1
    aumento *= (2*sal_aume)
    print(aumento)
print('Salário atual: ', sal_init+sal_aume+aumento)

################################################################################################################################################################

#9) Escreva um programa para ler n valores inteiros e calcular:

#A soma de todos os números
#O maior número digitado
#O menor número digitado
#A média dos números pares
#A quantidade de primos na sequência

#Nota: O valor de n não será informado, implemente um laço que realize leituras até que o usuário digite um valor flag (flag: 0). 
#A flag é apenas um valor pré-definido que indica o fim das entradas, interrompendo o laço de leitura.

num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
soma = 0
cont = 0
primo = 0
j=0
while True:
    num = int(input(''))
    if num==0:
        break
    soma+=num
    if num>num_1:
        num_1=num 
    if num<num_2:
        num_2=num 
    if(num%2==0):
        num_4+=num 
        cont+=1
    j=0
    for i in range(1,num+1):
        if (num%i==0):
            j+=1 #declarar
    if (j==2):
        primo+=1
    

print(' A soma de todos os números: %d\nO maior número digitado: %d\n'
'Menor número digitado: %d \nA média dos números pares %.2f\n'
'A quantidade de primos: %d'%(soma,num_1,num_2,(num_4/cont),primo))
