import pika
import json
import random
import time
from common.utils import encode_signal,decode_signals,generate_mac

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='can_bus', exchange_type='fanout')

print("[Engine ECU] Started.......")

speed = 0
rpm = 800

while True:
    # Simulate Speed and RPM changes
    speed += random.randint(-1,3)
    speed = max(0,min(speed,200))

    rpm += random.randint(-50,100)
    rpm = max (800, min(rpm,7000))

    #Encoding messages
    speed_data = encode_signal('VehicleSpeed', speed)
    rpm_data = encode_signal('EngineRPM',rpm)

    #Send speed
    msg_speed = {"ecu": "ECU_ENGINE","id":512,"data": speed_data,"mac":generate_mac(speed_data)}
    channel.basic_publish(exchange='can_bus',routing_key='',body=json.dumps(msg_speed))

    #Send rpm
    msg_rpm = {"ecu": "ECU_ENGINE","id":513,"data": rpm_data,"mac":generate_mac(rpm_data)}
    channel.basic_publish(exchange='can_bus',routing_key='',body=json.dumps(msg_rpm))

    print(f"[ENGINE] Sent speed={speed:.1f} km/h, RPM={rpm}")
    time.sleep(0.3)