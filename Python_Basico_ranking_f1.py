# -*- coding: utf-8 -*-

#**Proyecto final 2 Introducción a Python**

 En este proyecto vamos a crear un ranking para las pruebas contrareloj de las clasificaciones de fórmula 1.

Al final debemos tener una función llamada clasificación que, introduciendole como parámetro un diccionario que contenga el nombre y apellidos de un piloto y el tiempo que ha tardado en completar 3 vueltas distintas, nos devuelva la clasificación de salida.

#Crear el diccionario

El diccionario llamado piloto_tiempos tendrá como clave el nombre del piloto y como valor una lista con sus 3 tiempos (los tiempos mostrarán los segundos por encima del minuto).

Y deberá contener los siguientes datos:

F. Alonso : 30.863, 30.595, 30.249]


C. Sainz Jr. : [31.653, 30.009, 30.215]

M. Verstappen : [30.499, 30.318, 28.997]
"""

#crea el diccionario piloto_tiempos

piloto_tiempos = {'F. Alonso':[30.863,	30.595,	30.249],
                  'C. Sainz Jr.':[31.653,	30.009,	30.215],
                  'M. Verstappen':[30.499,	30.318,	28.997]}

print(piloto_tiempos)

#@title Comprueba el diccionario piloto_tiempos
def check():
  if piloto_tiempos['F. Alonso']==[30.863, 30.595, 30.249] and piloto_tiempos['M. Verstappen']==[30.499,	30.318,	28.997]:
    return 'Correcto'
  else:
    return 'Incorrecto'
check()

"""#Función agregar_piloto

Una vez creado el diccionario e introducidos los 3 primeros pilotos crea la función agregar_piloto que, recibiendo un diccionario, un nombre de piloto y una lista de tiempos por parámetros; agrege ese piloto y sus tiempos al diccionario.


"""

#Crea la función agregar piloto con sus parámetros necesarios
def agregar_piloto(dic,nombre,tiempos):
  dic[nombre]=tiempos
  return f'El piloto {nombre} ha sido agregado'




agregar_piloto(piloto_tiempos,'L. Hamilton',[30.617,	30.085,	29.385])
agregar_piloto(piloto_tiempos,'V. Bottas',[31.200,	30.186,	29.586])

print(piloto_tiempos)

def check2():
  try:
    agregar_piloto(piloto_tiempos,'Charles Leclerc',[30.691, 30.010, 29.678])
  except:
    return 'Incorrecto'
  else:
    if len(piloto_tiempos)==6 and piloto_tiempos['Charles Leclerc']==[30.691, 30.01, 29.678]:
      return 'Correcto'
check2()

"""##Función ranking

La función ranking, recibiendo un diccionario como parámetro debe devolver una tupla con la lista ordenada desde vuelta más rápida a más lenta (cogeindo el mejor de sus 3 tiempos) con el nombre de los pilotos y otra lista con sus tiempos.

Entrada

      ranking(piloto_tiempos)


Salida

      (['M. Verstappen',
      'L. Hamilton',
      'V. Bottas',
      'Charles Leclerc',
      'C. Sainz Jr.',
      'F.alonso'],
    [28.997, 29.385, 29.586, 29.678, 30.009, 30.249])
"""

def ranking(dic):
  times=[]
  piloto=[piloto for piloto in dic.keys()]
  result=[]
  for tiempos in dic.values():
    times.append(min(tiempos))
  order_times=sorted(times)
  for i in order_times:
    result.append(piloto[times.index(i)])
  return (result, order_times)
ranking(piloto_tiempos)

pilot, record_time=ranking(piloto_tiempos)
print(pilot==['M. Verstappen', 'L. Hamilton', 'V. Bottas', 'Charles Leclerc', 'C. Sainz Jr', 'F. Alonso'])
pilot

['M. Verstappen','L. Hamilton','V. Bottas','Charles Leclerc','C. Sainz Jr.','F. Alonso']

#@title Comprueba la función ranking
pilot, record_time = ranking(piloto_tiempos)

def check3():
  if pilot==['M. Verstappen', 'L. Hamilton', 'V. Bottas', 'Charles Leclerc', 'C. Sainz Jr', 'F. Alonso'] and record_time==[28.997, 29.385, 29.586, 29.678, 30.009, 30.249]:
    return 'Correcto'
  else:
    return 'Incorrecto'

check3()
