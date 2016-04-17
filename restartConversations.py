#!/usr/bin/env python
import dbus
import sys
from time import sleep

try:
    from config import TOKILL, SERVER, SLEEP
    TOKILL = [k.lower() for k in TOKILL]
except Exception as e:
    print >> sys.stderr, "ERROR %s: %s" % (type(e), e)
    print >> sys.stderr, "Create a config.py file similar to config.example.py first.\n"
    exit(1)

# Based off http://developer.pidgin.im/wiki/DbusHowto
bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService",
                     "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

conns = {}
for chan in purple.PurpleGetConversations():
    name = purple.PurpleConversationGetName(chan)
    if name.lower() in TOKILL:
        conns[name] = purple.PurpleAccountGetConnection(purple.PurpleConversationGetAccount(chan))
        purple.PurpleConversationDestroy(chan)

sleep(SLEEP)
for chan, conn in conns.items():
    purple.ServJoinChat(conn, {
      "server": SERVER,
      "channel": chan
    })
    sleep(1)
