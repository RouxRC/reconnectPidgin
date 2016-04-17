#!/bin/bash

cd $(dirname $0)
source DBUS_SESSION_ADDRESS.sh
./restartConversations.py
