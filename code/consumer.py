from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer('quickstart-events')

for message in consumer:
        message = message.value #Es un valor binario b'msg'
        msg_int = int(message.decode('UTF-8'))
        print('------------')
        #print('Precio recibido $', msg_int)
        print('------------')
        if msg_int > 1408500: #Cuartil 75%
                print("ALERTA - LIMITE SOBREPASADO: $", msg_int)
        elif msg_int < 1406300: #Cuartil 25%
                print("ALERTA - PRECIO DEMASIADO BAJO: $", msg_int)
        else:
                print('Precio recibido $', msg_int)
