# -*- coding: utf-8 -*-

#########################################################################
#  Matheus Fillipe -- 26, August of 2020                                #
#                                                                       #
#########################################################################
#  Description: Simple python IRC bot with regex matching based commands#
#                                                                       #
#                                                                       #
#  If you just want to edit basics of the bot look up commands.py and   # 
#  settings.py                                                          #
#########################################################################


#TODO URL READER

import socket, re, utils
from commands import *
from utils import log, debug
from settings import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

log('soc created |', s)
remote_ip = socket.gethostbyname(HOST)
log('ip of irc server is:', remote_ip)

s.connect((HOST, PORT))

log('connected to: ', HOST, PORT)

nick_cr = ('NICK ' + NICK + '\r\n').encode()
s.send(nick_cr)
usernam_cr= ('USER '+" ".join([USERNAME]*3)+' :rainbow pie \r\n').encode()
s.send(usernam_cr)
if utils.SINGLE_CHAN:
    s.send(('JOIN '+CHANNELS[CHAN_N]+' \r\n').encode()) #chanel
else:
    for chan in CHANNELS:
        s.send(('JOIN '+chan+' \r\n').encode()) #chanel

def send_message(message, channel):
    if type(message)==str:
        s.send((str('PRIVMSG ' + channel) + " :"+ message + ' \r\n').encode())
    if type(message)==list:
        for msg in message:
            send_message(msg, channel)

while 1:
    data = s.recv(4096).decode('utf-8')
    debug(data)
    if data.find("PING")!=-1 and len(data.split(":"))>=3 and 'PING' in data.split(":")[2]: 
        s.send(str('PONG ' + data.split(':')[1] + '\r\n').encode())
        log('PONG sent \n')
        continue

    try:
        channel=data.split()[2]
        splitter="PRIVMSG "+channel+" :"
        msg=splitter.join(data.split(splitter)[1:])

        for cmd in utils.regex_commands:
            for reg in cmd:
                m=re.match(reg, msg, flags=re.IGNORECASE)
                if m:
                    result=cmd[reg](m)
                    if result:
                        send_message(result, channel)
                        continue

        for word in msg.split(" "):
            if len(word)<6:
                continue
            result=None
            word=word.strip()
            if word[-1] in [" ", "?", ",", ";", ":", "\\"]:
                word=word[:-1]
            if utils.validateUrl(word):
                result=utils.url_commands[-1](word)
            if result:
                send_message(result, channel)

    except Exception as e:
        log("ERROR IN MAINLOOP: ",e)

s.close()
