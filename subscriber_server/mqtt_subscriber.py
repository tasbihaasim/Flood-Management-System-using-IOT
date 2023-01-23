import paho.mqtt.client as mqtt #import the client1
import time
Data = []
# def on_message(client, userdata, message):
#     print("message received " ,str(message.payload.decode("utf-8")))
#     print("message topic=",message.topic)
#     print("message qos=",message.qos)
#     print("message retain flag=",message.retain)

# broker_address="localhost"
# client = mqtt.Client("P1")
#
# client.on_message=on_message
# client.connect(broker_address) #connect to broker
# client.loop_start()
# client.subscribe("Indus/inflow/sensor1")
# publish()
# client.loop_stop()

# def on_message(client, userdata, message):
#     print("message received " ,str(message.payload.decode("utf-8")))
#     print("message topic=",message.topic)
#     print("message qos=",message.qos)
#     print("message retain flag=",message.retain)
# ########################################
# broker_address="localhost"
# client = mqtt.Client("P1") #create new instance
# client.on_message=on_message #attach function to callback
# client.connect(broker_address) #connect to broker
# client.loop_start() #start the loop
# client.subscribe("Indus/inflow/sensor1")
# publish()
# #print("message received ", str(client.on_message.payload.decode("utf-8")))
# time.sleep(4) # wait
# python3.6

import random

from paho.mqtt import client as mqtt_client

import csv

f = open('C:/Users/Tasbiha/Iot/rawdata.csv', 'a', newline='')
writer = csv.writer(f)

# broker = 'broker.emqx.io'
broker="localhost"
port = 1883
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        #Data.append((msg.payload.decode(), msg.topic))
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        writer.writerow((msg.topic, msg.payload))
        #print(Data)

    client.subscribe("Indus/inflow/sensor1")
    client.subscribe("Indus/outflow/sensor1")
    client.subscribe("Indus/level/sensor1")
    client.subscribe("Jehlum/inflow/sensor1")
    client.subscribe("Jehlum/outflow/sensor1")
    client.subscribe("Jehlum/level/sensor1")
    client.on_message = on_message


def run():
    client = connect_mqtt()
    time.sleep(4)
    subscribe(client)
    time.sleep(4)
    client.loop_forever()


if __name__ == '__main__':
    run()

