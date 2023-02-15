import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Process message and send response
        response = self.process_message(message)

        # Send response back to WebSocket client
        await self.send(json.dumps({
            'response': response
        }))

    def process_message(self, message):
        # Process the message received from the WebSocket client
        # and return the response
        pass
