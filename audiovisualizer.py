# code references
#https://stackoverflow.com/questions/40138031/how-to-read-realtime-microphone-audio-volume-in-python-and-ffmpeg-or-similar
#https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
#https://stackoverflow.com/questions/37402649/python-time-sleep-indefinitely
#https://stackoverflow.com/questions/54648015/python-websockets-how-to-send-message-from-function

# this client sends audio levels from default mic source to echo server using websocket
import sounddevice as sd
import numpy as np
import asyncio
import json
import websockets
audiolevel = 0;
def getsound():
    fs = 44100
    myrecording = sd.rec(1, samplerate=fs, channels=2)
    sd.wait()
    volume_norm = np.linalg.norm(myrecording)*200
    global audiolevel
    audiolevel = volume_norm


async def main():
    print("Starting sender")
    global audiolevel
    while 1:
        getsound()
        async with websockets.connect('ws://127.0.0.1:8001') as websocket:
            try:
                await websocket.send(json.dumps(audiolevel))
                print("sending : ",audiolevel)
            except Exception as e:
                print(e)

asyncio.get_event_loop().run_until_complete(main())