import asyncio
import websockets
import cv2
import io
import json
import numpy as np
import requests

async def run():
    requests.post("http://localhost:5000/Open")
    cap = cv2.VideoCapture(0)
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while cap.isOpened():
            ret, frame = cap.read()
            memfile = io.BytesIO()
            np.save(memfile, frame)
            memfile.seek(0)
            data = memfile.read()
            await websocket.send(data)
            if cv2.waitKey(1) & 0xFF == ord('q'):
	            break
        cap.release()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run())