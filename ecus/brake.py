import pika
import json
import random
import time
from common.utils import encode_signal,decode_signals,generate_mac

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='can_bus', exchange_type='fanout')

print("[BRAKE ECU] Started...")

brake_status = 0  # 0=off, 1=pressed

while True:
    brake_status = random.randint(0,1)
    data = encode_signal("BrakeStatus", brake_status)
    msg = {"ecu":"ECU_BRAKE","id":768,"data":data,"mac":generate_mac(data)}
    channel.basic_publish(exchange='can_bus', routing_key='', body=json.dumps(msg))
    print(f"[BRAKE] Sent brake status={brake_status}")
    time.sleep(1)