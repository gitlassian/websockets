import asyncio
import websockets

connected_clients = set()

async def chat_handler(websocket, path):
    # Register the new client
    # connected_clients.add(websocket)
    # try:
    #     async for message in websocket:
    #         # Broadcast the received message to all connected clients
    #         if message:
    #             print(f"Received: {message}")
    #             # Await each send operation
    #             await asyncio.wait([client.send(message) for client in connected_clients if client != websocket])
    # finally:
    #     # Unregister the client when done
    #     connected_clients.remove(websocket)
    connected_clients.add(websocket)
    message = await websocket.recv()
    print("new message" + message)
    for client in connected_clients:
        if client != websocket:
            await client.send(message)

start_server = websockets.serve(chat_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("Chat server started on ws://localhost:8765")
asyncio.get_event_loop().run_forever()