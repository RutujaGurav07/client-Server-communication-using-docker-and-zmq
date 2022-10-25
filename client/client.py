import zmq

# intialize ZMQ context
context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")

# socket Creating from  intitalized context
socket = context.socket(zmq.REQ)
socket.connect("tcp://172.18.0.2:8001")

for request in range(5):
    socket.send(b"Hello From client")
    #  Get the reply.
    message = socket.recv().decode('utf-8')
    print("Received reply %s [ %s ]" % (request, message))