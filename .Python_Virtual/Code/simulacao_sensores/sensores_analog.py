from Code.variaveis import variaveis_globais
import random
import asyncio

async def sensor_caixa_adubo_1():
    while True:
        tempo = random.randint(10,100)
        distancia = (tempo / 2) * 5 /10
        distancia_int = int(distancia)
        variaveis_globais.sensor_caixa_adubo_1 = distancia_int
        await asyncio.sleep(0.5)

async def sensor_caixa_adubo_2():
    while True:
        tempo = random.randint(10,100)
        distancia = (tempo / 2) * 5 /10
        distancia_int = int(distancia)
        variaveis_globais.sensor_caixa_adubo_2 = distancia_int
        await asyncio.sleep(0.5)



