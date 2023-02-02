# Flood-Management-System-using-IOT

## Getting Started
# Installation
Install packages and set up environment

```
pip install requirements
```
# Usage
Run the following files simultaneously in 3 different terminals. 
Terminal 1:
Launching the COAP server
```
python ../subscriber_server/coap_server.py
```

Terminal 2:
Launching the MQTT subscriber
```
python ../subscriber_server/mqtt_subscriber.py
```

Terminal 3:
Launching data simulators; publishers and client for mqtt and coap protocol. 
```
python simulator.py
```

