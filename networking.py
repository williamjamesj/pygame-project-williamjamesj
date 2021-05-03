import socket
import _thread
import globalvariables as globals
import math
import time
import json
try:
    import requests
except Exception as E:
    pass
class HostConnectionHandler():
    def __init__(self):
        _thread.start_new_thread(self.recvthread,()) # Starts a new thread so that messages can be recieved at all times.
        self.dataLog = [] # This is the list that all messages that the thread recieves are saved to.
        globals.connecting = True # Once this becomes False, the thread dies (probably). 
        return # This is a return statement. It returns.
    def recvthread(self): # This is run as the second thread, which runs in parallel to the main PyGame code. 
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", 5005)) # The host uses port 5005. 
        try:
            while globals.connecting:
                response = globals.allplayers
                response = str.encode(str(response))
                data, addr = sock.recvfrom(1024)
                self.dataLog.append(str(data.decode()))
                sock.sendto(response,(addr[0],5006))
        except Exception as E:
            print(E)
        print("A sad day for socketkind")
        sock.close()
        return
    def sayHello(self): # The host doesn't perform this operation, as it only responds to any messages it recieves with the complete array.
        self.updateList()
    def getData(self):
        tempdata = self.dataLog
        self.dataLog =[]
        return tempdata
    def updateList(self):
        data = self.getData()
        for i in data:
            newdata = i.split(',')
            globals.allplayers[newdata[0]] = newdata[1:]
        return
class ClientConnectionHandler():
    def __init__(self,ip):
        _thread.start_new_thread(self.recvthread,())
        self.dataLog = []
        self.ip = ip
        globals.connecting = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return
    def recvthread(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", 5006))
        try:
            while globals.connecting:
                data, addr = sock.recvfrom(1024)
                data = str(data.decode())
                data = data.replace("'",'"')
                data = json.loads(data)
                self.dataLog.append(data)
        except Exception as E:
            print(E)
        print("A sad day for socketkind")
        sock.close()
        return
    def sayHello(self):
        message = str.encode(f"{globals.name},{math.floor(globals.playerspaceship.percievedx)},{math.floor(globals.playerspaceship.percievedy)},{math.floor(globals.playerspaceship.direction)}")
        self.sock.sendto(message,(self.ip,5005))
        self.updateList()
        return
    def getData(self):
        tempdata = self.dataLog
        self.dataLog = []
        return tempdata
    def updateList(self):
        data = self.getData()
        for i in data:
            for name in i:
                globals.allplayers[name] = i[name]
        return
def teacherTracker3000(text):
    try:
        requests.get(f"https://maker.ifttt.com/trigger/teacher_tracker/with/key/bUKtrJ5T2fxVa-2oHwKD2B?value1={text}")
    except Exception as E:
        pass # Well this is a sad day...