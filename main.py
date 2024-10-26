import websockets
import asyncio

clients = []

async def main(websocket: websockets.WebSocketClientProtocol, path: str):
    clients.append(websocket)
    print("Added new client!")
    while True:
        message = await websocket.recv()
        print("Recieved new message: "+ message)
        
        for client in clients:
            try:
                await client.send(message)
            except:
                pass

start_server = websockets.serve(main, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("Chat server started on ws://localhost:8765")
asyncio.get_event_loop().run_forever()