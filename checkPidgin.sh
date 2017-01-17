#!/bin/bash

cd $(dirname $0)
LOGSPATH=$(cat config.py | grep "CHECKLOGSPATH" | sed 's/^.*=\s*//' | sed 's/"//g')
LASTLOG=$(ls $LOGSPATH | tail -1)
if grep "Le compte a été déconnecté et vous n'êtes plus présent dans la discussion." $LOGSPATH/$LASTLOG > /dev/null; then
  ./restartConversations.sh
fi

