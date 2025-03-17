from Code.mqtt_config.mqtt_client_connection import MqttClientConnection
from Code.broker.broker_config import mqtt_broker_config
from Code.variaveis import variaveis_globais
from Code.simulacao_sensores.sensores_analog import sensor_caixa_adubo_1,sensor_caixa_adubo_2 
from time import sleep 
import asyncio

mqtt_connect = MqttClientConnection(
    broker=mqtt_broker_config["broker"],
    topico=mqtt_broker_config["topico"],
    porta=mqtt_broker_config["porta"],
    client_id=mqtt_broker_config["client_id"],
    keepalive=mqtt_broker_config["keepalive"]
)
mqtt_connect.start_connection()

async def loop_main():
    while True:
        asyncio.gather(sensor_caixa_adubo_1(),sensor_caixa_adubo_2())
        await asyncio.sleep(1) 
asyncio.run(loop_main())