import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Notification(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()
        print('connected')

        # Optionally, you can join a group based on user or some criteria
        # await self.channel_layer.group_add(
        #     'some_group_name',
        #     self.channel_name
        # )

    async def disconnect(self, close_code):
        # Optionally, you can leave a group when disconnected
        # await self.channel_layer.group_discard(
        #     'some_group_name',
        #     self.channel_name
        # )
        pass

    async def receive(self, text_data):
        # Parse the incoming data
        data = json.loads(text_data)
        print(data)
        
        # Extract message type and content
        message_type = data.get('type')
        message_content = data.get('message') or data.get('notification')
        
        # Handle different message types
        if message_type == 'text':
            # Handle text messages
            await self.send_text_message(message_content)
        elif message_type == 'notification':
            # Handle notifications
            await self.send_notification(message_content)
        else:
            # Handle unknown message types
            await self.send_error_message("Unknown message type")

    async def send_text_message(self, message):
        print(message)
        # Send a text message back to the WebSocket client
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': message
        }))

    async def send_notification(self, notification):
        print(notification)
        # Send a notification message back to the WebSocket client
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'notification': notification
        }))

    async def send_error_message(self, error_message):
        # Send an error message back to the WebSocket client
        await self.send(text_data=json.dumps({
            'type': 'error',
            'error': error_message
        }))
