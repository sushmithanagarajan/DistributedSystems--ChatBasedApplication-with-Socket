

import socket                                                                                                       #import all the socket , tkinter packages
from datetime import datetime, time as datetime_time, timedelta                                                     #date time packages to calculate the time between chats
import datetime
import time
from Tkinter import *
import Tkinter
import tkintertable
import threading

def sendmsg():                                                                                                       #function definition for send button
    msg = my_msg.get()                                                                                               #get the user written input msg
    print msg                                                                                                        #print msg in console
    end_time = time.time()                                                                                              #calculate the endtime when the msg is received

    delta = (end_time - start_time)
    delta_time = str(timedelta(seconds=delta))
    #time difference between start time and end time, roundoff the value
    total_msg = "[User : "+login_msg + "]  " +str(delta_time)+ " " + msg                                                   #User name and the time diff , msg is printed
    detail_msg = str(login_msg +":"+ msg)
    disbox.insert(END,total_msg)                                                                                        #the msg is been inserted in the listbox
    client.send(detail_msg)                                                                                             #send the client msg to the server
    data = client.recv(size)                                                                                            #receive the broadcasted msg from the server
    disbox.insert(END,data)                                                                                             #print the msgs in the disbox listbox


def login():                                                                                                            #function for Login
    global start_time                                                                                                   #calculate the start time
    start_time = time.time()                                                                                            #start time after the client accepts the connection
    time.sleep(0)                                                                                                       #sleep time for time calculation
    print "We have entered the chatroom:"
    global login_msg
    login_msg = loginmsg.get()                                                                                          #get the client login name
    MSG = "User : " +login_msg+ " has entered the chatroom"                                                             #get the msg
    disbox.insert(END,MSG)                                                                                              #insert the msg in the listbox
    no = login_msg.count("")                                                                                            #print the count of the username
    print no
    if (no <9):                                                                                                         #if username more than 9 characters it would not accept
        client.send(login_msg)                                                                                          #send the client msg to the server
    else:
        disbox.insert(END,"bad clientname")                                                                             #end the bad msg
        client.close()
        print "Bad Username"
        top.quit()

def on_closing(event=None):                                                                                             #function def on chat close
    my_msg.set("exit")                                                                                                  #set exit msg
    print login_msg
    msgclose = "exit"
    close1 =  msgclose + ":" +login_msg                                                                                  #send client close
    client.send(close1)
    exitmsg = client.recv(size)
    print exitmsg
    emsg= "Client " + login_msg+ "has been disconnected"
    #disbox.insert(END , exitmsg)
    disbox.insert(END, emsg)


host = socket.gethostname()                                                                                             #get the hostname of the socket
port = 1234
size = 2000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                                              #set the client socket
client.connect((host, port))                                                                                            #connect the host and port

top = Tk()                                                                                                              #cretae a object for Tkinter
top.title("Chatter Box")                                                                                                #title for the Tkinter GUI

disframe= Frame(top, width=200, height=200)                                                                             #Frame for list box
typframe = Frame(top, width=200, height=200)                                                                            #type frame for typing area
disframe.grid(row=0, sticky="ew")

typframe.grid(row=1, sticky="nsew")
typframe_label = Label(typframe, text='Enter')                                                                          #Enter your label here
typframe_labe2 = Label(typframe, text='Enter your Message Here:')                                                       #Enter the label for msg


loginmsg = StringVar()                                                                                                  #accept the user name variable from the GUI
usernamespace=Entry(typframe,textvariable = loginmsg)
loginmsg.set("")
usernamespace.grid(row=0, column=2)                                                                                     #create a entry box frame
usernamespace.pack()                                                                                                    #send the username box


my_msg = StringVar()                                                                                                    #the mymsg string to accept user given msgs in the text box
messpace=Entry(typframe,textvariable = my_msg)
my_msg.set("")
messpace.pack()


scrollbar = Scrollbar(disframe)  # To navigate through past messages.
scrollbar.pack(side=RIGHT, fill=Y)


disbox = Listbox(disframe, height=15, width=50, yscrollcommand=scrollbar.set)                                           #Listbox for printing typed messages on screen
disbox.pack(side=LEFT, fill=Y)
disbox.pack()


login_button = Button(typframe,text = "Login",command = login)                                                          #Creating login button
login_button.pack()
send_button = Button(typframe, text="Send", command=sendmsg)                                                            #create send button and its action
send_button.pack()

exit_button = Button(typframe,text = "Exit",command=on_closing)                                                         #create exit button
exit_button.pack()
tkinter.mainloop()                                                                                                      #Kickstart the main loop


