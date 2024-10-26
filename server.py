import asyncio
import websockets

connected_clients = set()

async def chat_handler(websocket, path):
    connected_clients.add(websocket)
    message = await websocket.recv()
    print(len(connected_clients))
    for client in connected_clients:
        if client != websocket:
            try:
                await client.send(message)
            except:
                pass

start_server = websockets.serve(chat_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("Chat server started on ws://localhost:8765")
asyncio.get_event_loop().run_forever()