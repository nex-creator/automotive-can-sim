🚗 Automotive CAN Bus Simulator (Python + RabbitMQ)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-Message%20Broker-orange)
![Automotive](https://img.shields.io/badge/Domain-Automotive%20Cybersecurity-red)
![CAN Bus](https://img.shields.io/badge/Protocol-CAN%20Bus-green)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![Status](https://img.shields.io/badge/Project-Active-success)

A multi-ECU automotive CAN communication simulator with signal encoding, decoding, and cybersecurity validation

This project simulates a realistic automotive CAN (Controller Area Network) environment using Python and RabbitMQ.
It models how multiple ECUs communicate over a CAN Bus, including signal publishing, decoding, validation, and security checks.

This project is designed for learning, portfolio showcase, and interview demonstration for roles in:

Automotive Embedded Systems

Vehicle Diagnostics

Automotive Cybersecurity

Automotive Testing / Validation

Python Automation

System / Hardware-in-loop simulation

📌 Project Overview

In a real vehicle, multiple ECUs (Engine, Brake, Cluster, Telematics, etc.) exchange sensor and actuator information over the CAN Bus.

This project simulates that behavior:

ECUs included in this simulation:
ECU Name	Function
Engine ECU	Publishes Vehicle Speed and Engine RPM
Brake ECU	Publishes Brake Status (pressed / released)
Cluster ECU	Listens to CAN and displays Speed + RPM
Telematics ECU	Security validation + anomaly detection

🧠 What this project demonstrates
✔ CAN message creation

Each ECU generates realistic signals (speed, rpm, brake status), converts them to raw CAN bytes, and assigns an ID.

✔ Signal encoding/decoding

Uses scaling factors and bit-lengths similar to a DBC file.

✔ Message broadcasting using RabbitMQ

Simulates the CAN network using:

Fanout exchange → broadcasts messages to all ECUs (similar to CAN Bus broadcast nature)

✔ Lightweight cybersecurity

Each CAN frame includes:

MAC (Message Authentication Code)

Telematics ECU validates MAC integrity

✔ Multi-process, scalable design

Each ECU runs independently and can scale like real vehicle architectures.

🖼 System Architecture Diagram (Project Banner)
                        ┌───────────────────────────┐
                        │        RabbitMQ           │
                        │    (CAN Bus Simulator)    │
                        │  Fanout Exchange: can_bus │
                        └──────────────┬────────────┘
                                       │
             ┌─────────────────────────┼──────────────────────────┐
             │                         │                          │
             ▼                         ▼                          ▼

 ┌──────────────────┐       ┌──────────────────┐       ┌────────────────────┐
 │   Engine ECU     │       │    Brake ECU     │       │   Telematics ECU   │
 │------------------│       │------------------│       │--------------------│
 │ Publishes:       │       │ Publishes:       │       │ Listens to ALL ECUs│
 │  - Vehicle Speed │       │  - Brake Status  │       │ Validates MAC      │
 │  - Engine RPM    │       │                  │       │ Detects anomalies  │
 │ Encodes signals  │       │ Encodes signals  │       │ - High speed alert │
 │ Adds MAC         │       │ Adds MAC         │       │ - High RPM alert   │
 └─────────┬────────┘       └────────┬─────────┘       └───────────┬────────┘
           │                         │                             │
           └─────────────────────────┼─────────────────────────────┘
                                     │
                                     ▼
                         ┌──────────────────────┐
                         │     Cluster ECU      │
                         │----------------------│
                         │ Displays:            │
                         │  - Speed             │
                         │  - RPM               │
                         │ Decodes signals      │
                         └──────────────────────┘



📂 Project Structure
automotive-can-simulator/
│
├── ecus/
│   ├── engine.py
│   ├── brake.py
│   ├── cluster.py
│   └── telematics.py
│
├── common/
│   └── utils.py
│
├── config/
│   └── db.json        # Signal definitions (similar to a DBC)
│
├── README.md
└── requirements.txt

🛠 Tech Stack

Python 3

RabbitMQ (Fanout Exchange)

CAN Signal Encoding/Decoding

SHA-256 Based MAC Validation

Multi-process system simulation

🚀 How to Run the Project
1. Start RabbitMQ

Ensure RabbitMQ is running:

rabbitmq-server


OR using Docker:

docker run -d --hostname rabbit --name rabbitmq \
  -p 5672:5672 -p 15672:15672 rabbitmq:3-management


RabbitMQ dashboard:
👉 http://localhost:15672

User: guest | Password: guest

2. Install Dependencies
pip install pika json hashlib


(Or use pip install -r requirements.txt)

3. Run ECUs (in separate terminals)
python ecus/engine.py
python ecus/brake.py
python ecus/cluster.py
python ecus/telematics.py