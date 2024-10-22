import asyncio
import websockets

async def recieve():
    async with websockets.connect("ws://localhost:8765") as websocket:
        message = await websocket.recv()
        print(message)

while __name__ == "__main__":
    asyncio.run(recieve())