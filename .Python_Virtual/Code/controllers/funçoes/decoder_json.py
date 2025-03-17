import json
from Code.controllers.mapper_json.mapper_json import MapperJson

def decoder_json(msg):
    msg_json = json.loads(msg.payload.decode())
    print(f"{json.dumps(msg_json, indent=4)}")
    
    return MapperJson(
        topico=msg_json["topico"],
        porta=msg_json["porta"],
        read=msg_json["read"],
        write=msg_json["write"],
        value=msg_json["value"]
    )
