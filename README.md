🚗 Automotive CAN Bus Simulator
Python • RabbitMQ • CAN Signals • Cybersecurity • Multi-ECU System
<p align="center"> <img src="https://raw.githubusercontent.com/<your-username>/<repo-name>/main/assets/banner.png" width="80%" /> </p> <p align="center"> <a href="#"><img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python"></a> <a href="#"><img src="https://img.shields.io/badge/RabbitMQ-Fanout_Exchange-orange?logo=rabbitmq"></a> <a href="#"><img src="https://img.shields.io/badge/Automotive-CAN_Bus-yellow?logo=car"></a> <a href="#"><img src="https://img.shields.io/badge/Status-Active-success"></a> <a href="#"><img src="https://img.shields.io/badge/License-MIT-green"></a> </p>

🧩 Project Summary

This project simulates a realistic automotive CAN Bus system using:

Multiple Python ECUs

RabbitMQ as the CAN network layer

Signal encoding/decoding

Basic cybersecurity (MAC integrity validation)

It demonstrates how real ECUs in a vehicle publish and subscribe to CAN frames.

🏎️ Included ECUs
ECU	Function
Engine ECU	Publishes Vehicle Speed + RPM
Brake ECU	Publishes Brake Status
Cluster ECU	Displays Speed + RPM
Telematics ECU	Monitors traffic, validates MACs, detects anomalies

🏗️ System Architecture
![Automotive CAN Architecture](assets/architecture.png)

                   ┌──────────────────────────────┐
                   │   RabbitMQ (CAN Bus Layer)   │
                   │ Fanout Exchange → can_bus     │
                   └───────────────┬──────────────┘
                                   │ Broadcasts to all ECUs
     ┌─────────────────────────────┼────────────────────────────┐
     │                             │                            │
     ▼                             ▼                            ▼
┌──────────────┐           ┌────────────────┐          ┌────────────────┐
│ ENGINE ECU   │           │ BRAKE ECU      │          │ TELEMATICS ECU │
│--------------│           │----------------│          │----------------│
│ • Speed      │           │ • Brake Status │          │ • MAC Verify   │
│ • RPM        │           │ • Signal Encode│          │ • Alerts       │
│ • MAC Add    │           │ • MAC Add      │          │                │
└───────┬──────┘           └────────┬───────┘          └────────┬───────┘
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    ▼
                         ┌────────────────────┐
                         │   CLUSTER ECU      │
                         │--------------------│
                         │ • Display Speed    │
                         │ • Display RPM      │
                         └────────────────────┘

📂 Project Structure
automotive-can-sim/
│
├── ecus/
│   ├── engine.py
│   ├── brake.py
│   ├── cluster.py
│   └── telematics.py
│
├── common/
│   └── utils.py          # Signal encoding/decoding + MAC
│
├── config/
│   └── db.json           # Signal definitions (mini-DBC)
│
├── assets/
│   └── banner.png         # GitHub project banner
│
├── README.md
├── LICENSE
└── requirements.txt

🔥 Key Features
✔️ Multi-ECU Communication

Each ECU publishes CAN-like messages using RabbitMQ.

✔️ Realistic Signal Encoding

Scaling, bit lengths, raw byte encoding—similar to a DBC workflow.

✔️ CAN-Bus Style Broadcast

RabbitMQ fanout exchange simulates:

"One publishes → All ECUs receive"

✔️ Automotive Cybersecurity

Each ECU adds a SHA256 MAC, validated by the Telematics ECU.

✔️ Anomaly Detection

Telematics ECU performs:

🚨 High Speed Alert

🚨 High RPM Alert

🚨 MAC Tamper Detection

⚙️ Installation
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start RabbitMQ

Option A — Local server:

rabbitmq-server


Option B — Docker (recommended):

docker run -d --hostname rabbit --name rabbitmq \
  -p 5672:5672 -p 15672:15672 rabbitmq:3-management


Management UI:
👉 http://localhost:15672

User: guest | Password: guest

🚀 Run ECUs (each in separate terminal)
python ecus/engine.py
python ecus/brake.py
python ecus/cluster.py
python ecus/telematics.py


You will see:

Speed / RPM updates

Brake presses

Cluster ECU displays live data

Telematics ECU warns about abnormal signals or tampered MACs