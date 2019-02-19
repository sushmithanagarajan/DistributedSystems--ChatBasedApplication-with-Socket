
import socket                                                                                                   #import all the required packages
import threading                                                                                                #import threading
from datetime import datetime, time as datetime_time, timedelta
import datetime
import time


class ThreadedServer(object):                                                                                    #create a class ThreadedServer
    def __init__(self, host, port):                                                                              #Init function is the first function called after main
        self.host = host                                                                                         #Declare host at runtime
        self.port = port                                                                                         #Declare port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                            #Declare socket with Sock stream , af_inet
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                                          #set sock for the parameters
        self.sock.bind((self.host, self.port))                                                                   #Bind the port and host with socket

    def listen(self):                                                                                             #Listen function after binding the socket
        self.sock.listen(5)                                                                                         #Listens upto 5 clients
        while True:
            client, address  = self.sock.accept()                                                                   #accept the client , address of client socket
            clientlist.append(client)                                                                               #append the client to a list of clients
            size = 1024                                                                                             #size of the messages
            name = client.recv(size)                                                                                #receive the name of the client through a object
            print "Client : " +name+ "  has entered the room"
            client.settimeout(500)                                                                                  #set timeout for client
            threading.Thread(target = self.listenToClient,args = (client,address)).start()                          #create thread for every client and listen to it
            #ThreadID = threading.get_ident()  # print the thread ID
            #print "Thread: " + str(ThreadID)

    def broadcast(self,response,client):                                                                            #broadcast function to brodcast all messages sent to server
        for i in clientlist:                                                                                        #if the client is in the clientlist then send response
            if i !=self.sock:                                                                                       #checks if the client should not send msg to itself
                i.sendall(response)                                                                                 #send response to all the connected clients


    def listenToClient(self, client, address):                                                                      #listen to the particular client
        size = 2048
        ThreadID = threading.current_thread()  # print the thread ID
        print "Thread: " + str(ThreadID)
        while True:
            try:

                data = client.recv(size)                                                                            #receive the msg which the client sends
                client.send(data)                                                                                   #Send the data received
                print data

                data1 = data.split(":")[0]
                data2 = data.split(":")[1]
                if data1!= "exit":                                                                                  #if the data is not a exit msg
                    print data
                    addr = str(address[1])
                    date = datetime.datetime.now()
                    length = len(data)
                    response = "client: " +data1+ " : " +data2                                                      #print the data from the client
                    print response
                    print "HTTP/1.1 200 OK"                                                                         #print the HTTP response format
                    print "Date " +str(date)
                    print "Server:Pycharm"
                    print "content Length: " +str(length)
                    print "Content-Type: text"
                    self.broadcast(response,client)
                else:
                    exitmsg = "client " +data2+ " is closed"                                                             #if the data is an exit message
                    client.send(exitmsg)
                    response = exitmsg
                    self.broadcast(response,client)
                    print "broadcasted"
                    #client.close()                                                                                  #close the client
            except:                                                                                                 #if any OS breaks occur close the client and break
                return False

if __name__ == "__main__":                                                                                          #first loop to be encountered
   while True:
       port_num = 1234                                                                                              #port num specified
       clientlist=[]                                                                                                #client list for the active list of clients
       ThreadedServer('',port_num).listen()                                                                         #call the listen function of the class Threadedserver


#References
#https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
#https://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
#http://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
#https://stackoverflow.com/questions/41785969/python-tcp-server-accepting-connections-and-broadcasting-commands
#https://stackoverflow.com/questions/10810249/python-socket-multiple-clients
#https://stackoverflow.com/questions/42062391/how-to-create-a-chat-window-with-tkinter
#https://stackoverflow.com/questions/919897/how-to-find-a-thread-id-in-python
#http://effbot.org/tkinterbook/frame.htm
#https://stackoverflow.com/questions/34276663/tkinter-gui-layout-using-frames-and-grid
#https://stackoverflow.com/questions/42062391/how-to-create-a-chat-window-with-tkinter
#http://effbot.org/tkinterbook/button.htm
#https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
#https://stackoverflow.com/questions/18550710/pack-labels-right-next-to-entry-box-in-tkinter-python
#https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings
#https://github.com/mikegpl/pythonchat/blob/master/server_select.py
#http://code.activestate.com/recipes/580757-chatbox-megawidget-for-tkinter/
#https://github.com/mikegpl/pythonchat
#https://github.com/mikegpl/pythonchat/blob/master/client.py
#https://pythonadventures.wordpress.com/2010/10/18/get-url-info/
#https://github.com/requests/requests/issues/1335
#https://stackoverflow.com/questions/2932511/letter-count-on-a-string
#https://stackoverflow.com/questions/9692979/calculating-content-length-with-python
#https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
#http://www.pythonforbeginners.com/requests/using-requests-in-python
#https://www.sitepoint.com/community/t/send-httpresponse-to-client/44691


