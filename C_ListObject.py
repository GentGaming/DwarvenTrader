from H_ServerClientCommunication import sendToClient
class ListObject:
    def __init__(self,name):
        self.name = name
def send(message):
    sendToClient(message)

