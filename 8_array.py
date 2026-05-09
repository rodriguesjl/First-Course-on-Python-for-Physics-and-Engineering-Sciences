#Crie uma lista de 100 elementos inteiros aleatórios entre -50 e 50

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
