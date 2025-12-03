import json
import hashlib

#Load database

with open('./config/db.json', 'r') as f:
    DB = json.load(f)

#Encoding and decoding functions
def encode_signal(signal_name,value):
    sig = DB[signal_name]['signals']
    raw_val = int(value/sig[list(sig.keys())[0]]['factor'])
    length = sig[list(sig.keys())[0]]['length']
    #Currently support upyo 16 bits
    if length <=8:
        return[raw_val & 0xFF]
    else:
        return[(raw_val >> 8) & 0xFF, raw_val & 0xFF]

def decode_signals(signal_name,data):
    sig = DB[signal_name]['signals']
    length = sig[list(sig.keys())[0]]['length']
    factor = sig[list(sig.keys())[0]]['factor']
    if length <= 8:
        raw_val = data[0]
    else:
        raw_val = (data[0] << 8) | data[1]
    return raw_val * factor

def generate_mac(data):
    return hashlib.sha256(bytes(data)).hexdigest()[:8]