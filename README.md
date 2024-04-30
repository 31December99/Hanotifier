## HA-notifier
Example script to forwards your Telegram messages to a Home Assistant entity (sensor),
utilizing the MQTT protocol and the Mosquitto broker. 
Just talk to bot

### Usage

1. Get a token bot from Botfather

### Dependencies

- requiremensts.txt

### Installation

1. Clone this repository.
2. Install the required dependencies using PIP.

### Configuration

Create a telegram.yaml:

- token: 
- api_id: 
- api_hash: 

Create a mqtt.yaml
- 
- user: 
- passw: 
- address: 
- port: 

### MQTT Sensor Configuration
Append this entity to your configuration.yaml

```yaml
mqtt:
  sensor:
    name: "Sensore"
    unique_id: "sensore_"
    state_topic: "Home/helltopic"
    availability_topic: "Home/availability"
    payload_available: "ON"
    payload_not_available: "OFF"
```
### Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License

### Output 

- [Success] Connected to Telegram
- [Success] Connected to the Broker
- [SENT:Home/helltopic] "22.34 Vdc" -> [Sensore]
- [BROKER RECEIVED:Home/helltopic] <- "b'22.34 Vdc'"
- [SENT:Home/helltopic] "Hey !" -> [Sensore]
- [BROKER RECEIVED:Home/helltopic] <- "b'Hey !'"