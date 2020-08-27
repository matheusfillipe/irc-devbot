import logging
import os

LOGFILE=None
LEVEL=logging.DEBUG
HOST = 'chat.freenode.com' 
PORT = 6665 
NICK = 'devbot'
PASSWORD = ''
USERNAME = 'devbot'
REALNAME = 'the_0dev_bot'
FREENODE_AUTH = True
SINGLE_CHAN = True
CHANNELS=["#mysupertest", "##0dev"]
CHAN_N=0

# Comment this line if not using password as env variable
PASSWORD=os.environ['PW']
