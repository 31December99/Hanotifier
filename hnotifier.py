import yaml
import paho.mqtt.client as mqtt


class Config:
    """Load configuration data """

    def __init__(self, data: {}):
        self.data = data

    @classmethod
    def config(cls, filepath: str) -> {}:
        """Try to load data from this file """
        data = cls._load_yaml(filepath)
        if data:
            return cls(data=data)

    @classmethod
    def _load_yaml(cls, filepath: str) -> {}:
        """check and try to open this file"""
        try:
            with open(filepath) as f_yaml:
                content = yaml.safe_load(f_yaml)
        except FileNotFoundError as e:
            raise f"File Yaml not found: {e}"
        except yaml.YAMLError as e:
            raise f"Yaml Error : {e}"
        return content


class Broker(Config):
    """Load configuration data """

    def __init__(self, data: {}):
        super().__init__(data)


class Mqtt:
    """ Mqtt publisher and subscriber """

    mosquitto: mqtt
    user: str
    passw: str
    address: str
    port: int

    def __init__(self, entity: str):
        self.entity = entity

    @classmethod
    def connect(cls, entity: str):
        _config = Broker.config("mqtt.yaml")
        cls.user = _config.data['user']
        cls.passw = _config.data['passw']
        cls.address = _config.data['address']
        cls.port = _config.data['port']

        cls.mosquitto = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        cls.mosquitto.username_pw_set(cls.user, cls.passw)
        cls.mosquitto.on_connect = Mqtt.on_connect
        cls.mosquitto.on_message = Mqtt.on_message
        cls.mosquitto.connect(cls.address, cls.port, 60)
        cls.mosquitto.loop_start()
        return cls(entity)

    @staticmethod
    def on_connect(client, userdata, flags, reason_code, properties):
        print(f"[{reason_code}] Connected to the Broker")
        # client.subscribe("$SYS/#")
        client.publish("Home/availability", "ON", retain=True)

    @staticmethod
    def on_message(client, userdata, msg):
        print(f"[BROKER RECEIVED:{msg.topic}] <- \"{msg.payload}\"")

    def subscribe(self, topic: str):
        self.mosquitto.subscribe(topic=topic)
