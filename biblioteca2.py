import random


media_altura = 1.75
desvio_padrao_altura = 0.15
populacao = [0]*100


#populacao = [random.gauss(media_altura, desvio_padrao_altura)for x in range(100)]


for i in range(100):
    populacao[i]= random.gauss(media_altura, desvio_padrao_altura)

for i in range(50):
    print(f'Pessoas {i}: {populacao[i]:.2f} metros')




