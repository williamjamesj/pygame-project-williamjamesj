import socket
import _thread
import globalvariables as globals
import math
import time
class HostConnectionHandler():
    def __init__(self):
        _thread.start_new_thread(self.recvthread,())
        self.dataLog = []
        globals.connecting = True
        return
    def recvthread(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", 5005))
        try:
            while globals.connecting:
                response = ""
                for i in globals.allplayers:
                    response += f"{i},{math.floor(int(globals.allplayers[i][0]))},{math.floor(int(globals.allplayers[i][1]))},"
                response = str.encode(response)
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
                self.dataLog.append(str(data))
        except Exception as E:
            print(E)
        print("A sad day for socketkind")
        sock.close()
        return
    def sayHello(self):
        message = str.encode(f"{globals.name},{math.floor(globals.playerspaceship.percievedx)},{math.floor(globals.playerspaceship.percievedy)},{math.floor(globals.playerspaceship.direction)}")
        self.sock.sendto(message,(self.ip,5005))
        return
    def getData(self):
        tempdata = self.dataLog
        self.dataLog =[]
        return tempdata