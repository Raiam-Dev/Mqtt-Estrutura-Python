from Code.controllers.funçoes.decoder_json import decoder_json
from Code.variaveis import variaveis_globais
import json

def controlador_funcoes(client,msg):
    mensagem = decoder_json(msg=msg)

    leitura_porta_digital(client=client,porta=mensagem.porta) if mensagem.read == True else print("Erro")

def leitura_porta_digital(client,porta:str):
   
    retorno = {
        "name":"",
        "porta":porta,
        "value": "",
        "status": "200"
    }

    match porta:

        case "A0.0":
            retorno["name"] = "sensor_caixa_adubo_1"
            retorno["value"] = variaveis_globais.sensor_caixa_adubo_1
            client.publish("retorno/sensor/adubo1",json.dumps(retorno, indent=4))

        case "A0.1":
            retorno["name"] = "sensor_caixa_adubo_2"
            retorno["value"] = variaveis_globais.sensor_caixa_adubo_2
            client.publish("retorno/sensor/adubo2",json.dumps(retorno, indent=4))


    