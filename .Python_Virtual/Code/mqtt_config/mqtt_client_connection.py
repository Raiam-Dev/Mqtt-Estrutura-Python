import paho.mqtt.client as mqtt
from Code.callbacks.callbacks_mqtt import on_connect, on_subscribe, on_message

class MqttClientConnection:
    def __init__(self, broker:str, topico:str, porta:int, keepalive:int, client_id:str):
        self.broker = broker
        self.topico = topico 
        self.porta = porta 
        self.keepalive = keepalive
        self.client_id = client_id
    
    def start_connection(self):
        client = mqtt.Client(client_id=self.client_id,reconnect_on_failure=True) 

        client.on_connect = on_connect
        client.on_subscribe = on_subscribe
        client.on_message = on_message

        client.connect_async(host=self.broker, port=self.porta, keepalive=self.keepalive)
        client.loop_forever()