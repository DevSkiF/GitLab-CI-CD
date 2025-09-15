#!/bin/bash

STAGE_TYPE=$1
BOT_TOKEN="7471816448:AAFtLce9Xil5QoxE-K1bdxVU7AB3cgRNAN0"
CHAT_ID="513449209"

sleep 3

if [ "$CI_JOB_STATUS" == "success" ]; then
  MESSAGE="Стадия $STAGE_TYPE $CI_JOB_NAME успешно завершена"
else
  MESSAGE="Стадия $STAGE_TYPE $CI_JOB_NAME завершилась с ошибкой!"
fi

curl -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" -d chat_id=$CHAT_ID -d text="$MESSAGE"