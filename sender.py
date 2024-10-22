import websockets
import asyncio

async def send():
    async with websockets.connect("ws://localhost:8765") as websocket:
        message = input("Message: ")
        await websocket.send(message)

while __name__ == "__main__":
    asyncio.run(send())