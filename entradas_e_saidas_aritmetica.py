############# Os exercícios são de leitura e impressão adjunto à operações aritméticas ##############################


# 1) Leia três valores inteiros $a$, $b$ e $c$ e imprima a soma desses valores.

valor1 = int(input('Digite 3 valores inteiros 1/3'))
valor2 = int(input('Digite 3 valores inteiros 2/3'))
valor3 = int(input('Digite 3 valores inteiros 3/3'))

print('Soma', valor1+valor2+valor3)

####################################################################################################################

# 2) Leia um número real e imprima o quadrado desse número.

valor = float(input('Digite numero real'))
print('Quadrado', valor**2)

####################################################################################################################

# 3) Leia dois números inteiros e imprima o resto da divisão entre esses números

num1 = int(input('Digite:'))
num2 = int(input('Digite:'))
print('Resto:', num1%num2)

####################################################################################################################

# 4)  Leia os valores de comprimento, largura e altura de uma caixa e imprima o seu volume

# Volume = comprimento x largura x altura

comprimento = float(input('comprimento:'))
largura = float(input('largura:'))
altura = float(input('altura:'))

print('Volume:', comprimento*largura*altura)


altura = float(input('altura:'))

print('Volume:', comprimento*largura*altura)

####################################################################################################################

# 5) Leia uma velocidade em (quilômetros por hora) e apresente-a convertida para (metros por segundo)

vel = float(input('v = '))
print('conversão: %.2f m/s'%(vel/3.6))

####################################################################################################################

# 6) Leia uma distância em milhas e apresente-a como quilômetros

mil = float(input('digite mil:'))
print('conversão', mil*1.61)

####################################################################################################################

# 7) Leia um valor em real e a atual cotação do dólar. Em seguida, imprima o valor de entrada em dólares.

real =  float(input('Digite R$:'))
print('Cotação US$:', real/5.24)

####################################################################################################################

# 8) Leia três valores inteiros e imprima a soma dos quadrados desses valores.

valor1 = int(input('Digite 3 valores inteiros 1/3'))
valor2 = int(input('Digite 3 valores inteiros 2/3'))
valor3 = int(input('Digite 3 valores inteiros 3/3'))

print('Soma', (valor1+valor2+valor3)**2)

####################################################################################################################

# 9) Leia um número inteiro e imprima a soma do antecessor do seu triplo com o sucessor do seu dobro.

num = int(input('leia:'))
print('Resultado:', (3*num-1)+(2*num+1))

####################################################################################################################

# 10) Leia o salário de um funcionário. Imprima qual seria seu novo salário considerando um aumento de 25%

salar = float(input('Valor Salário:'))
print('Com aumento de 25pc: %.2f'% (salar + salar*0.25))

####################################################################################################################

# 11) Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que 
# solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida 
# que deverá ser paga, sabendo-se que sao descontados 8% para imposto de renda.

val = int(input('digite o num de dias trabalhados: '))
print('Valor a ser pago: R$', val*30 - (val*30*0.08))

####################################################################################################################

# 12) Escreva um programa para ajudar vendedores. A partir de um valor lido, mostre:

# O total a pagar com 10% de desconto
# O valor de cada parcela no parcelamento de 6x sem juros
# A comissão do vendedor caso venda a vista (5% sobre o valor com desconto)
# A comissão do vendedor caso venda a prazo (5% sobre o valor total)

valor = float(input('Digite o preço: '))
print('10 por cento de desconto: %.2f'% (valor - valor*.01))
print('6x sem juros, cada parcela: %.2f'% (valor/6))
print('Comissão à vista: %.2f'% ((valor - valor*.01)*0.05))
print('Comissão a prazo: %.2f'% (valor*0.05))

####################################################################################################################

# 13) Escreva um programa que recebe a idade de uma pessoa e o ano atual e calcula o ano de nascimento dessa pessoa.

ano_atual = int(input('Digite o ano atual:'))
idade = int(input('Digite sua idadde: '))
print('ano de nascimento: ', ano_atual - idade) 

####################################################################################################################

# 14) Leia um valor inteiro em segundos e imprima o equivalente em horas, minutos e segundos

sec = int(input('Digite os segundos:'))
print('em horas: ', sec/(60*60))
print('em minutos', sec/60)
print('em segundos', sec)

####################################################################################################################

# 15) Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido 
# proporcionalmente ao valor que cada um deu para a realização da aposta. 
# Faça um programa que leia quanto cada apostador investiu, o valor do premio, 
# e imprima quanto cada um ganharia do prêmio com base no valor investido.

v_a = float(input('valor apostado por a: '))
v_b = float(input('valor apostado por b: '))
v_c = float(input('valor apostado por c: '))
v_t = v_a+v_b+v_c
print('Parte do prêmio de US$ 5250652.41 recebido por a: US$ %.2f' % ((v_a/v_t)*5250652.41))
print('Parte do prêmio de US$ 5250652.41 recebido por b: US$ %.2f' % ((v_b/v_t)*5250652.41))
print('Parte do prêmio de US$ 5250652.41 recebido por c: US$ %.2f' % ((v_c/v_t)*5250652.41))

####################################################################################################################

# 16) Faça a leitura de três valores inteiros e apresente como resultado a soma dos quadrados dos três valores.

valor1 = int(input('Digite 3 valores inteiros 1/3'))
valor2 = int(input('Digite 3 valores inteiros 2/3'))
valor3 = int(input('Digite 3 valores inteiros 3/3'))

print('Soma', (valor1**2+valor2**2+valor3**2))

####################################################################################################################

# 17) Escreva um programa que 
#leia um valor inteiro referente a um 
#valor em reais e calcule a menor quantidade 
#possível de notas necessárias para pagar aquele valor. 
#As notaspossíveis são: 100, 50, 20, 10, 5, 2, 1

#Entrada
val = int(input('Digite o valor total:'))

#Processamento
notas_cem = val//100
n1 = val - (notas_cem*100)

notas_cinq = n1//50
n2 = n1 - (notas_cinq*50)

notas_vint = n2//20
n3 = n2 - (notas_vint*20)

notas_dez = n3//10
n4 = n3 - (notas_dez*10)

notas_cinc = n4//5
n5 = n4 - (notas_cinc*5)

notas_dois = n5//2
n6 = n5 - (notas_dois*2)

notas_um = n6//1

#Saída
print('%d nota(s) de 100,00' % notas_cem)
print('%d nota(s) de 50,00' % notas_cinq)
print('%d nota(s) de 20,00' % notas_vint)
print('%d nota(s) de 10,00' % notas_dez)
print('%d nota(s) de 5,00' % notas_cinc)
print('%d nota(s) de 2,00' % notas_dois)
print('%d nota(s) de 1,00' % notas_um)

####################################################################################################################

# 18) Escreva um programa que leia do usuário um valor inteiro em segundos, e imprima-o em horas, minutos e segundos

#ENTRADA
sec = int(input('digite a quantidade de segundos: '))

#PROCESSAMENTO
#Armazenamento de variáveis
    #Quantidade de horas
horas = sec//3600
    #subtrair de sec a quantidade de segundas em horas
sec_1 = sec - (horas*3600)
    # transformar sec_1 em minutos
minutos = sec_1//60
    #subtrair de sec_1 a quantidade de segundo que restou dos minutos
seg = sec_1 - (minutos*60)

print('Tranformação, %02d:%02d:%02d'% (horas, minutos, seg))

####################################################################################################################

# 19) Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua distância da origem (0,0).

#entrada
cor_x = float(input("coordenada x:"))
cor_y = float(input("coordenada y:"))

#processamento
# formula da distancia é d = sqrt((x-x0)^2+(y-y0)^2), x0 = y0 = 0
# fica d = sqrt(x^2+y^2) no caso x = cor_x e y = cor_y
dist = (cor_x**2+cor_y**2)**0.5

#saída
print("A distância do ponto P(x,y) à origem é approx %.2f (com duas casas decimais de precisão)" % dist)
