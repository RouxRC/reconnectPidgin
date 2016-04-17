#!/bin/bash

cd $(dirname $0)
pidgin &
sleep 30
echo 'export DBUS_SESSION_BUS_ADDRESS="'$DBUS_SESSION_BUS_ADDRESS'"' > DBUS_SESSION_ADDRESS.sh
