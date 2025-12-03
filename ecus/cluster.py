import pika
import json
import random
import time
from common.utils import encode_signal,decode_signals,generate_mac

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='can_bus', exchange_type='fanout')

result = channel.queue_declare(queue='',exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='can_bus',queue=queue_name)

print("[Cluster ECU] Listening for speed and rpm....")

def callback(ch,mehtod,properties,body):
    msg = json.loads(body)
    if msg['id'] == 512:
        speed = decode_signals("VehicleSpeed", msg['data'])
        print(f"[Cluster] Vehicle Speed: {speed:.1f} km/hr")
    elif msg['id'] == 513:
        rpm = decode_signals("EngineRPM",msg['data'])
        print(f"[Cluster] Engine RPM: {rpm}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()