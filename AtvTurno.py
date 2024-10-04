print('Vamos descobrir em que turno você estuda!\n')

TurnoM = 'M'
TurnoV = 'V'
TurnoN = 'N'

turno= str(input('Digite M-matutino, V-vespertino ou N-noturno:\n')).upper()
if turno == TurnoM:
    print('Você está matriculado no turno matutino.  Bom dia !!')
elif turno == TurnoV:
    print('Você está matriculado no turno verpestino. Boa tarde!!')
elif turno == TurnoN:
    print('Você está matriculado no turno noturno .Boa noite!!')
else: 
    print('Opção inválida!!') 
