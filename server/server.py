 # importing the library 
import time
import zmq

# intialize ZMQ contextS
context = zmq.Context()

# socket Creating from  intitalized context
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8001")


while True:
    #  Wait for next request from client
    message = socket.recv().decode('utf-8')
    print("Received request: %s" % message)


    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"Done from Server")