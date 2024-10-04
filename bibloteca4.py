import time 

inicio = time.perf_counter()  # Programa mostrará quanto tempo levará para ir de 0 a 999999


for x in range(100000): 
    continue

fim = time.perf_counter()

tempo_decorrido = fim - inicio 

print(f'Tempo decorrido:{tempo_decorrido:.6f} segundos')
