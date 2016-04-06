# in spanish.. c:
from datetime import datetime

ahora = datetime.now()

dia = ahora.day # El dia del mes
mes = ahora.month # El mes del ano
ano = ahora.year # El ano, basicamente.
hora = ahora.hour # La hora
minuto = ahora.minute # La minuto
segundo = ahora.second # La segundo.. de.. esta... hora? (Me tarde como 3 segundos xD)

print(dia)
print(mes)
print(ano)
print("Dia y Hora con formato del los Estados Unidos")
print '%s-%s-%s' % (mes, dia, ano)
print("Hora militar")
print '%s:%s:%s' % (hora, minuto, segundo)

wait(5)
print("Toda en una vez")
print '%s/%s/%s %s:%s:%s' % (mes, dia, ano, hora, minuto, segundo)

#Todo es en tu zona appropriada. Hora militar!
