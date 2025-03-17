import paho.mqtt as mqtt
from Code.broker.broker_config import mqtt_broker_config
from Code.controllers.funçoes.controlador_funcoes import controlador_funcoes
import json

def on_connect(client, userdata,flags,rc):
    print("\n Conectado com Sucesso" if rc == 0 else f"Erro ao se Conectar {rc}" )
    client.subscribe(topic=mqtt_broker_config["topico"],qos=1)
    client.subscribe(topic="sensor/adubo1",qos=1)
    client.subscribe(topic="sensor/adubo2",qos=1)

def on_subscribe(client, userdata, mid, granted_qos):
    print(f'\n Inscrito nos Topicos com sucesso, QOS:{granted_qos}')

def on_message(client, userdata,msg):
    controlador_funcoes(client=client,msg=msg)
    