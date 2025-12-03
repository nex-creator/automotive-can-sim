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

print("[Telematics ECU] Monitoring CAN Traffic....")

def callback(ch,mehtod,properties,body):
    msg = json.loads(body)
    data = msg['data']
    received_mac = msg['mac']
    actual_mac = generate_mac(data)
    if actual_mac != received_mac:
        print(f"[SECURITY ALERT] MAC mismatch from {msg['ecu']}")
        return
    if msg['id'] == 512:
        speed = decode_signals("VehicleSpeed", data)
        if speed > 180:
            print(f"[WARNING] High speed detected: {speed} km/h")
    elif msg["id"] == 513:
        rpm = decode_signals("EngineRPM", data)
        if rpm > 6500:
            print(f"[WARNING] High RPM: {rpm}")
    elif msg["id"] == 768:
        brake = decode_signals("BrakeStatus", data)
        print(f"[TELEMATICS] Brake status: {brake}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()