from Code.mqtt_config.mqtt_client_connection import MqttClientConnection
from Code.broker.broker_config import mqtt_broker_config
from time import sleep 

mqtt_connect = MqttClientConnection(
    broker=mqtt_broker_config["broker"],
    topico=mqtt_broker_config["topico"],
    porta=mqtt_broker_config["porta"],
    client_id=mqtt_broker_config["client_id"],
    keepalive=mqtt_broker_config["keepalive"]
)
mqtt_connect.start_connection()
