#1) Crie uma lista de 100 elementos inteiros aleatórios entre -50 e 50

#Converta e redimensione essa lista para um array de dimensões 10 x 10

#Crie novos arrays contendo:

#Apenas os valores negativos do array
#As linhas pares do array (incluindo zero)
#O quadrado dos valores positivos do array

import random as rd
import numpy as np

arr = np.array([rd.randint(-50,50) for i in range(100)]).reshape(10,10)
neg = arr[arr<0]
arr_neg = np.array(arr[arr<0])
arr_lpar = np.array(arr[:11:2,:])
arr_qd = np.array(arr[arr>=0]**2)
print('Array 10x10:\n',arr,'\n')
print('Array dos pares de 10x10\n',arr_neg,'\n')
print('Array das linhas pares de 10x10\n',arr_lpar,'\n')
print('Array do quadrado dos pares:\n',arr_qd)

#2) Crie um array numpy de dimensões 5 x 5 com o valor das bordas iguais a 1 e o centro com valores 0, como apresentado a seguir. 

array = np.zeros((5,5))
#linhas
array[:1,], array[4:,] = (1,1)
#colunas
array[:,:1],array[:,4:] = (1,1)
print(array)

#3) Crie dois arrays (A e B) de dimensões 5x5 com valores inteiros aleatórios, e seguintes operações:

    #a. Imprima a média da soma de A e B
    #b. Imprima a matriz resultante da multiplicação das duas primeiras linhas da matriz A com as duas últimas colunas da matriz B.
    #c. Imprima o array contendo a união dos valores de ambas as matrizes (sem repetição)
    #d. Imprima o array contendo a intersecção dos valores de ambas as matrizes (sem repetição)

import numpy as np
import random as rd

matriz_1 = np.array([rd.randint(0,50) for i in range(25)]).reshape(5,5)
matriz_2 = np.array([rd.randint(0,50) for i in range(25)]).reshape(5,5)

print(matriz_1,'\n\n',matriz_2,'\n\n')
matriz_medsom = np.mean(matriz_1+matriz_2)
print(matriz_medsom,'\n\n')
#print(matriz_1[:2,:],'\n',matriz_2[:,3:],'\n\n')
matriz_mult = np.dot(matriz_1[:2,:],matriz_2[:,3:])
print(matriz_mult)
array = np.array(matriz_1[matriz_1!=matriz_2[:,:]]) 
array = np.append(array, matriz_2[matriz_2!=matriz_1[:,:]])
array = np.append(array, matriz_2[matriz_2==matriz_1[:,:]])
array_int = np.array(matriz_1[matriz_1==matriz_2[:,:]])

print('\n\n Array união de tamanho {}\n{}:'.format(len(array),array))
print('\n\n Array intersecção de tamanho {}\n{}:'.format(len(array_int),array_int))
