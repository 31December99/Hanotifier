## HA-notifier
Example script to forwards your Telegram messages to a Home Assistant entity (sensor),
utilizing the MQTT protocol and the Mosquitto broker. 
Just talk to bot

### Usage

1. Get a token bot from Botfather

### Dependencies

- requirements.txt

### Installation

1. Clone this repository.
2. Install the required dependencies using PIP.
3. create hanotifier.yaml file

### hanotifier.yaml
- bot_token:  *your telegram bot token* 
- api_id:  *your api_id telegram account*
- api_hash: *your api_hash telegram account*
- ha_token: *your home assistant token* 
- ha_address: *your home assistant server address*
- ha_port:  *your home assistant server port*
- mqtt_user: *your mosquitto user name*
- mqtt_passw: *your mosquitto password*
- mqtt_port: *your mosquitto server port*

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

### Output example

- [Success] Connected to Telegram
- [Success] Connected to the Broker
- [SENT:Home/helltopic] "22.34 Vdc" -> [Sensore]
- [BROKER RECEIVED:Home/helltopic] <- "b'22.34 Vdc'"
- [SENT:Home/helltopic] "Hey !" -> [Sensore]
- [BROKER RECEIVED:Home/helltopic] <- "b'Hey !'"