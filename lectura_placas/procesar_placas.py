# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:57:41 2020

@author: jcarl
"""

import redis
import os
import time
import random

import procesar_metodos as metodos


#Restringe redis a codificar-decodificar los mensajes como string con "charset='utf-8', decode_responses=True"
r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=6379, db=0, charset='utf-8', decode_responses=True)
redis_ready = False

while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print('waiting for redis')
        time.sleep(3)
        
print('setup:redis alive')
print('setup:espera 3 segundos')
time.sleep(3)


while True:    
    radiofonico, alfabeto = '', ''
    cadena = r.lpop('queue_elementos')

    if cadena is None:
        print('se agotaron los elementos')
        break

    print('------------------------------')    
    print(cadena + ' ---', metodos.listar_cadena(cadena))

    for x in cadena:
        if (x.isdigit()):
            alfabeto = metodos.convertir_numero(x)
        else:
            alfabeto = metodos.convertir_caracter(x)

        print(' ... ', x, ': ', alfabeto)
        radiofonico += {True: alfabeto, False: '-' + alfabeto} [radiofonico == '']

    print(cadena + ' ---', radiofonico)
    time.sleep(random.randint(2, 6)/2)