import time
import asyncio
from hnotifier import Mqtt, Config
from telethon import TelegramClient, events


class Telegram:
    """Load configuration data """
    _config = Config.config("telegram.yaml")
    token = _config.data['token']
    api_id = _config.data['api_id']
    api_hash = _config.data['api_hash']

    def __init__(self, session: str):
        self.notify = None
        self.session = session
        self.client = None

    async def connect(self):
        if not self.session or not self.api_id or not self.api_hash or not self.token:
            raise Exception(f"[Error] Invalid telegram data")
        self.client = TelegramClient("hnotifier", self.api_id, self.api_hash, retry_delay=10)
        await self.client.start(bot_token=self.token)
        print(f"[Success] Connected to Telegram")
        self.register_event_handlers()
        self.notify = Notifier.connect()

    def register_event_handlers(self):
        @self.client.on(events.NewMessage())
        async def handle_new_message(event):
            await self.handle_event(event)

    async def handle_event(self, event):
        self.notify.send(message=event.message.message)


class Notifier:
    topic = "Home/helltopic"
    entity = "Sensore"

    def __init__(self):
        self.notify = Mqtt.connect(self.entity)
        self.notify.subscribe(self.topic)

    @classmethod
    def connect(cls):
        if cls.topic and cls.entity:
            return cls()

    def send(self, message: str):
        self.notify.mosquitto.publish(self.topic, message)
        print(f"[SENT:{self.topic}] \"{message}\" -> [{self.entity}]")
        # time.sleep(5)
        # self.notify.mosquitto.loop_stop()


async def start():
    telegram = Telegram(session="hnotifier")
    await telegram.connect()


async def main():
    loop = asyncio.get_event_loop()
    await asyncio.create_task(start())
    await loop.create_future()


if __name__ == "__main__":
    asyncio.run(main())
