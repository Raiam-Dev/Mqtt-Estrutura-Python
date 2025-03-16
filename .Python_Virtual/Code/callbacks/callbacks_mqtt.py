import paho.mqtt as mqtt
from Code.broker.broker_config import mqtt_broker_config
import json

def on_connect(client, userdata,flags,rc):
    print("Conectado com Sucesso" if rc == 0 else f"Erro ao se Conectar {rc}" )
    client.subscribe(topic=mqtt_broker_config["topico"],qos=1)

def on_subscribe(client, userdata, mid, granted_qos):
    print(f'Inscrito no Topico: {mqtt_broker_config["topico"]} com sucesso, QOS:{granted_qos}')

def on_message(client, userdata,msg):
    mensagem = json.loads(msg.payload.decode())
    print(json.dumps(mensagem, indent=4))
    