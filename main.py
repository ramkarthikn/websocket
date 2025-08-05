import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(f"You said: {message}")

async def main():
    server = await websockets.serve(echo, "0.0.0.0", 10000)
    print("WebSocket server running on port 10000...")
    await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
