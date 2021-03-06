import paho.mqtt.client as mqtt

#I don't understand why this client isn't working, it tells me there is no
#module named 'paho,' so maybe try it on someone besides mine computer and it
#will work. -Sam

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Temperature1")
 #   client.subscribe("PennApps/Smash/Sound")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload)) #where I need to send info to mongodb


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()


#command to fake a hardware publishing
#   mosquitto_pub -d -h iot.eclipse.org -p 1883 -t "PennApps/Smash/Temperature" -m "poop"
#   mosquitto_pub -d -h iot.mootoo.co -p 1883 -t "PennApps/Smash/Temperature/1" -m ""
