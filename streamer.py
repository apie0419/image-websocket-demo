import asyncio
import websockets
import cv2
import io
import json
import threading
import numpy as np

class Streamer(threading.Thread):
    
    def __init__(self, host="localhost", port=8765):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.connected = False

    async def serve(self, websocket, path):
        print ("Start Serving")
        while self.connected:
            data = await websocket.recv()
            if data is None:
                continue
            memfile = io.BytesIO()
            memfile.write(data)
            memfile.seek(0)
            frame = np.load(memfile)

            # ret, jpeg = cv2.imencode('.jpg', frame)
    
            cv2.imshow("Frame", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == ord("Q"):
                break
        

    def run(self):
        print ("Start")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        start_server = websockets.serve(self.serve, self.host, self.port)
        self.connected = True
        loop.run_until_complete(start_server)
        loop.run_forever()
    
    def disconnect(self):
        self.connected = False