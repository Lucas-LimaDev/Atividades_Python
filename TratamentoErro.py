# TRY EXCEPT 
while True:
      try:
            nr = int(input('Digite um número ou -1 para encerrar : '))
            if nr == -1:
                  break
            s = nr * 3
            print(s)
            q = 12/s
      except ValueError:
                  print('Digite um número válido!')
      except ZeroDivisionError:
            
            print('Valor não pode ser o 0!')
            
      else:
                    
            print(q)
      finally:
            
            print('Obrigrado por usar o programa! ')