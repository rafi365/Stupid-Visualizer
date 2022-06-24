import asyncio
import json
import websockets
#this server is used to broadcast the message sent from audiosender(audiovisualizer.py) to all client browser listening
USERS = set()

VALUE = 0

async def websocketHandler(websocket):
    global USERS, VALUE
    try:
        # Register user
        USERS.add(websocket)
        # Send current state to user
        await websocket.send(json.dumps(VALUE))
        # Manage state changes
        async for message in websocket:
            event = json.loads(message)
            print("Received : ",message)
            websockets.broadcast(USERS, json.dumps(event))
    finally:
        # Unregister user
        USERS.remove(websocket)

async def main():
    print("Starting server")
    async with websockets.serve(websocketHandler, "localhost", 8001):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())