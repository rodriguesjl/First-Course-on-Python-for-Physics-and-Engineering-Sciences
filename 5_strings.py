#1) Faça um programa que leia um nome e imprima as 4 primeiras letras do nome.

a = input('')
b = ''
for i in range(4):
    b+=a[i]
print(b)

############################################################################################################################################################

#2) Faça um programa que conte o número de 1’s que aparecem em um string.

corda = input('Entrada:\n   ')
soma = 0
for i in range(len(corda)):
    if corda[i]=='1':
        soma+=1
print('Saída\n   %d'%soma)

############################################################################################################################################################

#3) Faça uma função que receba uma frase (string) e retorne quantos caracteres são espaços em brancos.

def qtd_char():
    corda = input('Entrada: ')
    soma = 0
    for i in range(len(corda)):
        if (corda[i]==' '):
            soma+=1
    return 'Saída: '+str(soma)
print(qtd_char())

############################################################################################################################################################

#4) Escreva um programa que leia a idade e o primeiro nome de n pessoas.
#Seu programa deve terminar quando uma idade negativa for digitada. 
#Ao terminar, seu programa deve escrever o nome da pessoa mais jovem e da mais velha.

Id_max = 0
Id_min = 100
nome_max = ''
nome_min = ''
while True:
    nome = input('Digite nome')
    idade = int(input('Digite sua idade'))
    if(idade<0):
        break
    if(idade>Id_max):
        Id_max = idade
        nome_max = nome
    if(idade<Id_min):
        Id_min = idade
        nome_min = nome
print('Saída:\n','Mais velho:',nome_max,'\n Mais novo',nome_min)

############################################################################################################################################################

#5) Escreva uma função que, dada uma string, retorne True se é um palı́ndromo e False, caso contrário. 
#Lembrando que um palı́ndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita. 
#Sua função deve ignorar símbolos, pontuação e espaços.

def palindromo():
    palavra = input('Digite a Palavra')
    vazio = ''
    palavra = palavra.replace(' ','')
    palavra = palavra.lower()
    print(palavra)
    for i in range(len(palavra)):
        vazio+=palavra[-(i+1)]
    if vazio == palavra:
        return 'Palíndromo'
    else:
        return 'Não é palíndromo'
print(palindromo())

############################################################################################################################################################

#6) Construa um programa que leia duas strings fornecidas pelo usuário.
#Verifique se a segunda string lida esta contida no final da primeira, retornando o resultado da verificação.

str_1 = input('Digite a primeira string')
str_2 = input('Digite a segunda string')
str_1 = str_1.lower()
str_1 = str_1.replace(' ','')
str_2 = str_2.lower()
str_2 = str_2.replace(' ','')
print(str_2 in str_1)

############################################################################################################################################################

#7) Escreva uma função que leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para 3 variáveis inteiras. 
#Antes disso, verifique se as barras estão no lugar certo, e se DD, MM e AAAA são numéricos.

def ler_char():
    data = input('Coloque a data da forma DD/MM/AAAA')
    print((data[2]=='/' and data[5]=='/'))
    print(data[0:2].isnumeric())
    print(data[3:5].isnumeric())
    print(data[6:10].isnumeric())
    var_1 = int(data[0:2])
    var_2 = int(data[3:5])
    var_3 = int(data[6:10])
    return str(var_1)+'/'+str(var_2)+'/'+str(var_3)
print(ler_char())

############################################################################################################################################################

#8) Faça uma função que receba uma sequência de digitos (em formato string) e encontre o conjunto de 3 dı́gitos consecutivos que gere o maior produto. 
#A função deve retornar uma string com os três digitos consecutivos encontrados. 
#A função deve retornar a primeira sequência encontrada, no caso de mais de uma válida.

def maior_prod():
    num_st = input('Digite o número')
    prod = 1
    base = 0
    if num_st.isnumeric():
        print('Você digitou somente números')
        for i in range(len(num_st)-2):
            prod = int(num_st[i])*int(num_st[i+1])*int(num_st[i+2])
            if prod>base:
                base = prod
        return prod
    else:
        return 'Você não digitou somente números'

print(maior_prod())

############################################################################################################################################################

#9) Faça um programa que leia os nomes de 3 pessoas e os imprima em ordem alfabética.

def simplifica(a,b):
    mult=1
    if(b==0):
        return 'Impossível divisão por zero'
    for i in range(1,min(a,b)+1):
        if (a%i==0)and(b%i==0):
            mult*=i
            a/=i
            b/=i
    return ('Numerador = %d\nDenominador = %d\nFator de max = %d'%(a,b,mult))

a = int(input(''))
b = int(input(''))
print(simplifica(a,b))
