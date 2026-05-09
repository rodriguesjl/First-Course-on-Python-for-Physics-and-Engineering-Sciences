# 1) Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro.

def dovro(x):
    x = x**2
    return x

x = float(input('Digite um número'))
dovro(x)
print('O dobro do número digitado é: ',dovro(x))

###################################################################################################################################################################

# 2) Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.

def verifica_se(x):
    if (x>0):
        return 1
    elif (x<0):
        return -1
    elif (x==0):
        return 0
x = float(input('Digite um número'))
verifica_se(x)
print(' 1 se positivo\n -1 se negativo\n 0 se 0: \n', verifica_se(x))

###################################################################################################################################################################

# 3) Faça uma função que receba a distância em $km$ e a quantidade de litros de gasolina consumidos por um carro em um percurso, 
# calcule o consumo em $km/l$ e escreva uma mensagem de acordo com a tabela abaixo:

# | CONSUMO (Km/l) | MENSAGEM         |
# |----------------|------------------|
# | menor que 8    | Venda o carro!   |
# | entre 8 e 12   | Econômico!       |
# | maior que 12   | Super econômico! |

def kilom(km,lt):
    if (km/lt<8):
        return 'Venda o carro!'
        
    elif (8<=km/lt<=12):
        return 'Econômico'
        
    elif (km/lt>12):
        return 'Super econômico'

km = float(input('Digite a kilometragem'))
lt = float(input('Digite os litro'))

kilom(km, lt)
print(kilom(km,lt))

###################################################################################################################################################################

# 4) Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos e segundos, e retorne o valor total em segundos.

def retorno_sec(hora, minuto):
    #h(60min/h)(60s/min)
    hora = hora*60**2
    minuto = minuto*60
    return hora+minuto
hr = int(input('Digite a hora'))
mt = int(input('Digite o minuto'))
sc = int(input('Digite o segundo'))
retorno_sec(hr,mt)
print('O retorno da quantidade em segundo dos três é: ', (retorno_sec(hr,mt)+sc))

###################################################################################################################################################################

# 5) Faça uma função que receba um número inteiro e retorne True se este número é par ou False caso contrário.

def aval_pi(z):
    return z%2==0

num = int(input('Digite um número'))
print(aval_pi(num))

###################################################################################################################################################################

# 6) Faça uma função e um programa de teste para o cálculo do volume de uma esfera. O raio deve ser passado por parâmetro para a função.

def volume_esf(raio):
    return (4/3)*(3.1415926)*raio
    
r_1 = float(input('Digite o valor do raio'))
print('O volume da esfera de raio %.2f... é %.3f...'%(r_1,volume_esf(r_1)))

###################################################################################################################################################################

# 7) Sejam e os catetos de um triângulo. Faça uma função que receba os valores dos catetos e retorne o valor da hipotenusa.

def hipotenusa(a,b):
    return ('O valor da hipotenusa é %.2f...'%(a**2+b**2))
c_a = float(input('Digite o valor do coeficiente a'))
c_o = float(input('Digite o valor do coeficiente b'))
print(hipotenusa(c_a,c_o))

###################################################################################################################################################################

# 8) Faça uma função que receba a altura e o sexo de uma pessoa e calcule e retorne seu peso ideal, 
# utilizando as seguintes fórmulas (onde h corresponde à altura):

# - Homens: (72.7 ∗ h) − 58
# - Mulheres: (62.1 ∗ h)−44.7

def pes_id(sex):
    if (sex=='h'):
        h_h = float(input('Digite sua altura em metros, ex: 1.54 (para 1m54cm)\nResposta:'))
        return ('Seu peso ideal é %.2f kg'%(72.7*h_h-58))
    elif (sex=='m'):
        h_m = float(input('Digite sua altura em metros, ex: 1.54 (para 1m54cm)\nResposta:'))
        return ('Seu peso ideal é %.2f kg'%(62.1*h_m-44.7))
    else:
        return 'Digite um sexo válido'

sexo = input("Digite 'h' se homem.\nDigite 'm' se mulher\nResposta: ")
print(pes_id(sexo))

###################################################################################################################################################################

# 9) Faça uma função que receba três valores A, B e C. Verifique se eles podem ser valores dos lados de um triângulo e, se forem, 
# imprima se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:

# O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
# Chama-se equilátero o triângulo que tem três lados iguais.
# Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

def lad_tr(a,b,c):
    if (a<b+c)and(b<a+c)and(c<a+b):
        return('sim trata-se de um triângulo')
        if (a==b==c):
            return('o triângulo é equilátero')
        elif (a==b or a==c) or (b==c):
            return('O triângulo é isósceles')
        elif (a!=b)or(a!=c)or(b!=c):
            return('O triângulo é escaleno')
    else:
        return('Não se trata de um triângulo')

a = float(input('Lado a:'))
b = float(input('Lado b:'))
c = float(input('Lado c:'))
print(lad_tr(a,b,c))

###################################################################################################################################################################

# 10) Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. 
#Se a letra for A a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a média ponderada, com pesos 5, 3 e 2.

def notas_alunos(a,b,c,lt):
    if(lt=='A'):
        return ('Você escolheu aritmética\nResultado: %.2f'%((a+b+c)/3))
    elif(lt=='P'):
        return ('Você escolheu ponderada\nResultado: %.2f'%((a*5+b*3+c*2)/3))
    else:
        return 'Digite A para média aritmética e P para ponderada'


a = float(input('Nota a:'))
b = float(input('Nota b:'))
c = float(input('Nota c:'))
lt = input('Digite A para média aritmética e P para ponderada\n Resposta: ')
print(notas_alunos(a,b,c,lt))

###################################################################################################################################################################

# 11) Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os seus algarismos. 
#Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1) Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".

def soma_algarismos(n):
    soma=0
    while True:
        a = n%10
        soma+=a
        n//=10
        if n<1:
            return soma
            break
            
num = int(input('Digite o número'))
print(soma_algarismos(num)) 

###################################################################################################################################################################

# 12) Faça uma função que receba dois valores numéricos e um sı́mbolo. 
# Este sı́mbolo representará a operação que se deseja efetuar com os números. 
# Se o sı́mbolo for '+' deverá ser realizada uma adição, se for uma subtração, se for '/' uma divisão e se for '*' será efetuada uma multiplicação. 
# A função deverá retornar o resultado da operação.

def op_art(a,b,op):
    if(op=='+'):
        return ('Você escolheu adição\nResultado: %.2f'%(a+b))
    elif(op=='-'):
        return ('Você escolheu subtração\nResultado: %.2f'%(a-b))
    elif(op=='*'):
        return ('Você escolheu multiplicação\nResultado: %.2f'%(a*b))
    elif(op=='/'):
        if (b!=0):
            return ('Você escolheu divisão\nResultado: %.2f'%(a/b))
        else:
            return 'Divisão por zero!'
    else:
        return 'Digite valores válidos'
num_1 = float(input('Digite o primeiro valor\nResposta: '))
num_2 = float(input('Digite o primeiro valor\nResposta: '))
opp = input('Digite + para soma\nDigite - para subtração\nDigite * para multiplicação\nDigite / para divisão\nResposta:')
print(op_art(num_1,num_2,opp))

###################################################################################################################################################################

# 13) Escreva uma função que receba duas coordenadas cartesianas e retorne as coordenadas polares.

import math

def cart2polar(x, y):
    dist = math.sqrt(x**2 + y**2)
    angulo = math.atan2(y, x)
    print(dist)
    print(angulo)
    return dist, angulo
    
d_polar, a_polar = cart2polar(3, 1)

print(d_polar)
print(a_polar)

###################################################################################################################################################################

# 14) Faça uma função que receba um valor n e retorne o fatorial desse número

num = int(input('Escreva o número que queiras saber o fatorial'))

def fatorial(num):
    fat = 1
    for i in range(1,num+1):
        fat*=i
    return fat
    
print('O fatorial de %d é %d'%(num, fatorial(num)))

###################################################################################################################################################################

# 15) Cria a função inverteValor() que recebe um inteiro de qualquer tamanho e retorna esse valor invertido usando apenas operações aritméticas.

#Entrar com o número
def inverteValor(x):
    num_p = num
    num_n = num
    i=0
    novo_num = 0
    while True:
        num_p/=10
        i+=1
        if(num_p<10):
            j = 0
            while j<=i:
                num_n//=(10**(i-j))
                novo_num+=(num_n*(10**j))
                num_n = num - ((num//(10**(i-j)))*(10**(i-j)))
                j+=1
            break
    return novo_num
    
num = int(input('Digite o inteiro'))
inverteValor(num)
print('O contrário do número que você quis foi: ', inverteValor(num))

# 16) Crie a função verificaInverso() que recebe o valor original e o valor invertido 
# e retorna verdadeiro se ambos forem igualmente par ou igualmente ímpar. Retorne falso caso contrário.

def verificaInverso(y,s):
    if ((y%2==0) and (s%2==0)) or ((y%2!=0) and (s%2!=0)):
        V = 'Verdadeiro'
        return V
    else:
        return 'Falso'

num_1 = int(input('Digite o inteiro'))
num_2 = inverteValor(num_1)
verify = verificaInverso(num_1, num_2)

print(verify)

# 17) No programa principal, peça um valor do usuário e imprima o retorno de ambas as funções.

def inverteValor(x):
    num_p = num
    num_n = num
    i=0
    novo_num = 0
    while True:
        num_p/=10
        i+=1
        if(num_p<10):
            j = 0
            while j<=i:
                num_n//=(10**(i-j))
                novo_num+=(num_n*(10**j))
                num_n = num - ((num//(10**(i-j)))*(10**(i-j)))
                j+=1
            break
    return novo_num

def verificaInverso(y,s):
    if ((y%2==0) and (s%2==0)) or ((y%2!=0) and (s%2!=0)):
        V = 'Verdadeiro'
        return V
    else:
        return 'Falso'


leia = int(input('Digite um número qualquer'))
inverso = inverteValor(leia)
print('O inverso do número dado é: ', inverso)

verifica = verificaInverso(inverso, leia)


print('É %s que tanto %d e seu inverso são pares ou ímpares'%(verifica, leia))
