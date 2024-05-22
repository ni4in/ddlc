import cv2 
import json 
import logging
import base64
import eventlet.wsgi
import socketio
import eventlet

capturing = False
sio = socketio.Server(ping_timeout=20)
app = socketio.WSGIApp(sio)
FORMAT = "%(asctime)s : %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%H:%M:%S")

def start_capture():
    global capturing
    capturing= True
    while capturing:
        logging.info('starting the capturing')
        img = cv2.imread('baboon.png')
        base64_img = base64.b64encode(img).decode('utf8')
        json_img = json.dumps({'img':base64_img})
        logging.info("the json dictionary is %s",{'img':base64_img})
        sio.emit('result',json_img)
        sio.sleep(2)

def stop_capture():
    global capturing
    capturing = False

@sio.event
def start_inspection(sid,data):
    logging.info('started inspection')
    start_capture()

@sio.event
def stop_inspection(sid,data):
    logging.info('stop inspection')
    stop_capture()
    sio.sleep(1)
    


if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('',5001)),app)

        

   
    