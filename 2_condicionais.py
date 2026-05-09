# 1) Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. 
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

#entrada
num = float(input('Digite um número'))

 #processamento

if num>=0: #se verdade
    print('A raíz quadrada de %f é %.2f'%(num, num**0.5))
else: #se falso
    print('O número é inválido')

#saída
print('fim')

##########################################################################################################################################################

# 2) O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. 
# A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.

# | CUSTO DE FÁBRICA              | % DO DISTRIBUIDOR | % DOS IMPOSTOS   |
# |-------------------------------|-------------------|------------------|
# | até 12.000,00                 | 5                 | isento           |
# | entre 12.000,00 e 25.000,00   | 10                | 15               |
# | acima de 25.000,00            | 15                |20                |

#início
valor = float(input('digite o valor pago'))

if 0<valor<=12600:
    print(' O valor de custo é %.2f \n A comissão paga foi de %.2f \n e os impostos são %s'%(valor - valor*0.05, valor*0.05, 'Isento'))
elif 15000<valor<=31250:
    print(' O valor de custo é %.2f \n A comissão paga foi de %.2f \n e os impostos são %s'%(valor - valor*0.1 - valor*0.15, valor*0.1, valor*0.15))
elif valor>=33750:
    print(' O valor de custo é %.2f \n A comissão paga foi de %.2f \n e os impostos são %s'%(valor - valor*0.15 - valor*0.2, valor*0.15, valor*0.2))
else:
    print('digite um valor positivo, ou um valor válido')

#saída

print('FIM')

##########################################################################################################################################################

# 3) Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês. 
# Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.

# Digite sua solução aqui
#Início
dia = int(input('Digite o dia'))
mes = int(input('Digite o mês'))
ano = int(input('Digite o ano'))

#Processamento
#Verificar se o ano é bissexto

if (0< ano <=2026):
    print('Ano válido')
else:
    print('Ano não válido')
    
if (1<=mes<=12):
    print('Mês válido')

else:
    print('Mês não válido')

if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
    if (0<dia<=31):
        print('Dia válido')

    else:
        print('Dia não válido para o mês %d que vai até dia 31'%mes)
    
elif (mes == 2): # SE TRUE
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        if (1<= dia <=28):
            print('Dia válido')
        else:
            print('Dia %d não válido de fevereiro de %d'% (dia, ano))
    else:
        if (1<=dia<=29):
            print('Dia válido')
        else:
            print('Dia %d não válido de fevereiro de %d'% (dia,ano))

elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
    if (0<dia<=30):
        print('Dia válido')

    else:
        print('Dia não válido para o mês %d que vai até dia 30'%mes)

##########################################################################################################################################################

# 4) Uma empresa vende o mesmo produto para quatro diferentes estados. 
# Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). 
# Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa 
# retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. 
# Se o estado digitado não for válido, mostrar uma mensagem de erro.

#Início
print('Digite o o valor do produto e depois estado, MG, SP, RJ ou MS')
valor = float(input("Digite o valor"))
estado = input('Digite o estado')

#processamento
if (estado == 'MG'):
    valor += valor*0.07
    print('Valor: R$%.2f'%valor)
elif (estado == 'SP'):
    valor += valor*0.12
    print('Valor: R$%.2f'%valor)
elif (estado == 'RJ'):
    valor += valor*0.15
    print('Valor: R$%.2f'%valor)
elif (estado == 'MS'):
    valor += valor*0.08
    print('Valor: R$%.2f'%valor)
else:
    print('ERRO!!! Digite um preço ou um estado válido')

#Fim do programa
print('FIM')

##########################################################################################################################################################

# 5) Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.

#entrada
num = int(input('Insira um inteiro'))

#processamento// condicional
if (num%2 == 0): #se True
    print('O número %d é par'%num)
else:
    print('O número %d é ímpar'%num)
#fim//saida
print('fim')

##########################################################################################################################################################

# 6) Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. 
#Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, 
#este fato deve ser informado ao usuário e o programa termina.

nota_1 = float(input('Digite a nota 1'))
nota_2 = float(input('Digite a nota 2'))
if (0<=nota_1<=10) and (0<=nota_2<=10):
    print('A média das notas é %.1f'%((nota_1+nota_2)/2))
else:
    print('ERRO!! As notas devem ser entre 0 e 10')

##########################################################################################################################################################

# 7) Leia o salário de um trabalhador e o valor da prestação de um empréstimo. 
#Se a prestação for maior que 20% do salário imprima: "Empréstimo não concedido", caso contrário imprima: "Empréstimo concedido".

salr = float(input('Digite o valor do salário'))
parc = float(input('Digite o valor da parcela'))
if (parc>(salr+salr*0.2)):
    print('Empréstimo não concedido, valor máximo do empréstimo %.2f'% (salr+salr*0.2))
else:
    print('Empréstimo concedido')

##########################################################################################################################################################

# 8) Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, 
#utilizando as seguintes fórmulas (onde $h$ corresponde à altura):

# - Homens: (72.7 ∗ h) − 58
# - Mulheres: (62.1 ∗ h) − 44.7

altura = float(input('Digite sua altura'))
sexo = input('Digite o gênero, H para masculino & M para feminino')

if (sexo == 'H'):
    print('peso ideal: %.2f'%(72.7*altura-58))
elif (sexo == 'M'):
    print('peso ideal: %2.f'%(62.1*altura-44.7))
else:
    print('Digite o sexo válido')

##########################################################################################################################################################

# 9) Dados três valores, A, B e C verificar se eles podem ser valores dos lados de um triângulo e, se forem, 
# se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:

# O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
# Chama-se equilátero o triângulo que tem três lados iguais.
# Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

#entrada
print('Escreva o comprimento dos lados do triângulo')

a = float(input('Lado a:'))
b = float(input('Lado b:'))
c = float(input('Lado c:'))

#processamento
if (a<b+c)and(b<a+c)and(c<a+b):
    print('sim trata-se de um triângulo')

    if (a==b==c):
        print('o triângulo é equilátero')
    elif (a==b or a==c) or (b==c):
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Não se trata de um triângulo')
#saída
print('fim do programa')

##########################################################################################################################################################

# 10) Leia a distância em $km$ e a quantidade de litros de gasolina consumidos por um carro em um percurso, 
# calcule o consumo em $km/l$ e escreva uma mensagem de acordo com a tabela abaixo:

# | CONSUMO (Km/l) | MENSAGEM         |
# |----------------|------------------|
# | menor que 8    | Venda o carro!   |
# | entre 8 e 12   | Econômico!       |
# | maior que 12   | Super econômico! |

kil = float(input('Digite o valor da kilometragem'))
lt = float(input('Digite quantos litros foram consumidos'))
if(kil/lt<8):
    print('Venda o carro!')
elif(8<=kil/lt<=12):
    print('Econômico')
elif(kil/lt>12):
    print('Super Econômico')
else:
    print('Digite valores válidos')

##########################################################################################################################################################

# 11) Leia um número inteiro e verifique se é par ou ímpar, imprima a informação

#entrada
num = int(input('Insira um inteiro'))

#processamento// condicional
if (num%2 == 0): #se True
    print('O número %d é par'%num)
else:
    print('O número %d é ímpar'%num)
#fim//saida
print('fim')

##########################################################################################################################################################

# 12) Leia os coeficientes de uma equação de segundo grau e imprima se existem raízes reais

#entrada
print('Escreva os coeficientes a, b e c da equação de segundo grau')

a = float(input('Escreva os números do coeficiente a:'))
b = float(input('Escreva os números do coeficiente b:'))
c = float(input('Escreva os números do coeficiente c:'))

#processamento
delta = b**2 - (4*a*c)

if (delta>=0): #se verdade
    print('raíz 1 = %.2f' % ((-b+(delta)**0.5)/(2*a)))
    print('raíz 2 = %.2f' % ((-b-(delta)**0.5)/(2*a)))
else: #se mentira
    print('Nào existem raízes reais')

##########################################################################################################################################################

# 13) Leia 3 valores representando o comprimento do lado de um triângulo e imprima se é escaleno, isósceles ou equilatero

#entrada
print('Escreva o comprimento dos lados do triângulo')

a = float(input('Lado a:'))
b = float(input('Lado b:'))
c = float(input('Lado c:'))

#processamento

if (a==b==c):
    print('o triângulo é equilátero')
elif (a==b or a==c) or (b==c):
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')
#saída
print('fim do programa')

##########################################################################################################################################################

# 14) Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas básicas (soma, subtração, multiplicação e divisão). 
# O usuário escolhe uma das opções e então o seu programa pede dois valores numéricos e apresenta o resultado da operação solicitada

num_1 = float(input('digite um  número'))
num_2 = float(input('digite outro  número'))
escolha = input('Escolha e digite o escolhido (+, -, *, /): ')

if (escolha == '+'):
    print('Você escolheu soma, o resultado de %.2f+%.2f é %.2f'%(num_1, num_2, num_1+num_2))
elif (escolha == '-'):
    print('Você escolheu subtração, o resultado de %.2f-%.2f é %.2f'%(num_1, num_2, num_1-num_2))
elif (escolha == '*'):
    print('Você escolheu multiplicação, o resultado de %.2fx%.2f é %.2f'%(num_1, num_2, num_1*num_2))
elif (escolha == '/'):
    if (num_2!=0):
        print('Você escolheu divisão, o resultado de %.2f÷%.2f é %.2f'%(num_1, num_2, num_1/num_2))
    else:
        print('Não pode-se dividir por zero')
else:
    print('Entre com dados válidos')

##########################################################################################################################################################

# 15) Escreva um programa que leia a data de hoje e a data de nascimento de uma pessoa. 
# Imprima quantos anos a pessoa tem e se ela já fez aniversário esse ano. Não é necessário verificar se as datas são válidas.
# Digite sua solução aqui
#Início
dia_hoje = int(input('Digite o dia de hoje: '))
mes_hoje = int(input('Digite o mês de hoje: '))
ano_hoje = int(input('Digite o ano de hoje: '))

#Processamento
#Verificar se o ano é bissexto#################### Verificando se a data é valida

if (0< ano_hoje <=2026):
    print('Ano válido')
else:
    print('Ano não válido')
    
if (1<=mes_hoje<=12):
    print('Mês válido')

else:
    print('Mês não válido')

if (mes_hoje == 1) or (mes_hoje == 3) or (mes_hoje == 5) or (mes_hoje == 7) or (mes_hoje == 8) or (mes_hoje == 10) or (mes_hoje == 12):
    if (0<dia_hoje<=31):
        print('Dia válido')

    else:
        print('Dia não válido para o mês %d que vai até dia 31'%mes_hoje)
    
elif (mes_hoje == 2): # SE TRUE
    if (ano_hoje%4==0 and ano_hoje%100!=0) or (ano_hoje%400==0):
        if (1<= dia_hoje <=28):
            print('Dia válido')
        else:
            print('Dia %d não válido de fevereiro de %d'% (dia_hoje, ano_hoje))
    else:
        if (1<=dia_hoje<=29):
            print('Dia válido')
        else:
            print('Dia %d não válido de fevereiro de %d'% (dia_hoje,ano_hoje))

elif (mes_hoje == 4) or (mes_hoje == 6) or (mes_hoje == 9) or (mes_hoje == 11):
    if (0<dia_hoje<=30):
        print('Dia válido')

    else:
        print('Dia não válido para o mês %d que vai até dia 30'%mes_hoje)

####################################################################################################

dia_ani = int(input('Digite o dia de nascimento: '))
mes_ani = int(input('Digite o mês de nascimento: '))
ano_ani = int(input('Digite o ano de nascimento: '))

######################################### verificação#############################################
if (0< ano_ani <=2026):
    print('Ano válido')
else:
    print('Ano não válido')
    
if (1<=mes_ani<=12):
    print('Mês válido')

else:
    print('Mês não válido')

if (mes_ani == 1) or (mes_ani == 3) or (mes_ani == 5) or (mes_ani == 7) or (mes_ani == 8) or (mes_ani == 10) or (mes_ani == 12):
    if (0<dia_ani<=31):
        print('Dia válido')

    else:
        print('Dia não válido para o mês %d que vai até dia 31'%mes_ani)
    
elif (mes_ani == 2): # SE TRUE
    if (ano_ani%4==0 and ano_ani%100!=0) or (ano_ani%400==0):
        if (1<= dia_ani <=28):
            print('Dia válido')
        else:
            print('Dia %d não válido de fevereiro de %d'% (dia_ani, ano_ani))
    else:
        if (1<=dia_ani<=29):
            print('Dia válido')
        else:
            print('Dia %d não válido de fevereiro de %d'% (dia_ani,ano_ani))

elif (mes_ani == 4) or (mes_ani == 6) or (mes_ani == 9) or (mes_ani == 11):
    if (0<dia_ani<=30):
        print('Dia válido')

    else:
        print('Dia não válido para o mês %d que vai até dia 30'%mes_ani)

########################################################################################################################
if (ano_hoje<ano_ani):
    print('ERRO!! ANO DE NASCIMENTO POSTERIOR A DATA DE HOJE --- VIAJANTE DO FUTURO??!!')
elif (mes_ani > mes_hoje):
    print('\nSeu aniversário ainda não aconteceu, sua idade é %d'%(ano_hoje-ano_ani-1))
elif (mes_ani == mes_hoje) and (dia_ani > dia_hoje):
    print('\nSeu aniversário ainda não aconteceu, está próximo, sua idade é %d'%(ano_hoje-ano_ani-1))   
elif (mes_ani == mes_hoje) and (dia_ani == dia_hoje):
    print('\nParabéns!! Hoje é seu aniversário, estás a fazer %d anos'%(ano_hoje-ano_ani))
elif (mes_ani == mes_hoje) and (dia-ani < dia_hoje):
    print('\nSeu aniversário ainda já aconteceu, recentemente, sua idade é %d'%(ano_hoje-ano_ani))
elif (mes_ani < mes_hoje):
    print('\nSeu aniversário ainda já aconteceu, sua idade é %d'%(ano_hoje-ano_ani))
        
##########################################################################################################################################################

# 16) Escreva um programa que recebe como entrada 4 notas de um aluno,
# calcula e imprime a sua média além de informar sua situação na
# disciplina de acordo com as seguintes regras:\n
# ● Abaixo de 40 pontos: reprovado\n
# ● Entre 40 e 60: exame especial\n
# ● Acima de 60: aprovado\n

# | Entrada          |       Saída           |
# |------------------|-----------------------|
# | 80, 52, 50, 40   |55.5 -- Exame especial |
# | 100, 80, 94, 70  | 86.0, APROVADO!       |

nota_1 = int(input('Digite a nota 1: '))
nota_2 = int(input('Digite a nota 2: '))
nota_3 = int(input('Digite a nota 3: '))
nota_4 = int(input('Digite a nota 4: '))

media = (nota_1+nota_2+nota_3+nota_4)/4

if (media<40):
    print('REPROVADO!! Media: %.1f'% media)
elif (40<=media<=60):
    print('Exame especial!! Media: %.1f' %media)
elif (60<=media):
    print('APROVADO!! Media: %.1f'%media)
else:
    print('Digite valores válidos, números inteiros!')
