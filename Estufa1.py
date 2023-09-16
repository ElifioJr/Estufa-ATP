import paho.mqtt.client as mqtt
import time
from hal import temperatura, temperatura2, aquecedor
from InfoDev import client_Id, user, password,server,port

def mensagem(client, userdata, msg):
    vetor = msg.payload.decode().split(',')
    aquecedor('on' if vetor[1] == '1' else 'off')
    client.publish(f'v1/{user}/things/{client_Id}/response',f'ok,{vetor[0]}')
    print(vetor)

# Connection Initial
client = mqtt.Client(client_Id)
client.username_pw_set(user, password)
client.connect(server, port)

# Passa a informação de status do Aquecedor ao Cayenne.
client.on_message = mensagem
client.subscribe('v1/'+user+'/things/'+client_Id+'/cmd/2')
client.loop_start()

# Passa as informações de temperatura captadas pelo sensor Hal e envia ao Cayenne.
while True:
    client.publish('v1/'+user+'/things/'+client_Id+'/data/0', temperatura())
    client.publish('v1/'+user+'/things/'+client_Id+'/data/1', temperatura2())
    time.sleep(10)
    