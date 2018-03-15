import paho.mqtt.client as mqtt
import requests
import xml.etree.ElementTree as ET
import sys
import datetime

file = open("log.txt", "a")
AHHost = "130.240.5.130:8045"
MQTTHost = "130.240.5.130"
def arrowHeadGet():
    #print all services registered at Arrowhead promt to msg these.
    r = requests.get("http://"+AHHost+"/servicediscovery/service")
    root = ET.fromstring(r.text)
    print("These are the existing ArrowHead services:")
    for service in root:
        print(service[2].text)
    print("\n")

def mqttSub():
    #subscribe to mqtt topic
    print("MQTT SUB to notification topic")

def mqttMsg():
    #send msg to mqtt topic
    print("MQTT MSG")
    topic = input("Service:\n -> ")
    msg = input("Message:\n -> ")
    client.publish(topic,msg,0,False)
    
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("job")
    client.subscribe("notification")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    file.write("(" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ") " + "Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTTHost, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()


def mqttSendJob():
    client.publish("jobs", "jobdata", 0, False)

inputs = {
    '1' : arrowHeadGet,
    '2' : mqttSub,
    '3' : mqttMsg,
    '4' : mqttSendJob,
    '5' : quit
}

run = True;
while run:
    print("Options: \n1. Show Arrowhead registered services\n2. Subscribe to MQTT topic notification\n"+
          "3. Send MQTT message\n4. Send job\n5. Quit")
    choice = input("-> ")
    if choice not in inputs:
        print("No such option ;)")
    else:
        inputs[choice]()

def quit():
    file.close()

    client.loop_stop()
    
    client.disconnect()
    
    sys.exit(0)



