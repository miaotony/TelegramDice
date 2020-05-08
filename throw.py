#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
throw.py
Telegram Dice Analysis
Throw darts / Roll dice
执行扔飞镖 / 掷骰子

@Author: MiaoTony
@Create time: 20200427
"""

import requests
import json
import time

# INPUT Telegram Bot TOKEN & Chat ID HERE
bot_token = "123456789:ABCDEFGADGSGDHGAFGHDJFHFGKJFUKGHF"
chat_id = '-456789123'

url = "https://api.telegram.org/bot{}/sendDice".format(bot_token)

payload = {'chat_id': chat_id,
           'emoji': '🎲'}  # 🎯

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# 20k times
for i in range(20000):
    print(i)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(time_str)
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.encoding = 'utf-8'
        result = response.text
        print(result)

        with open('results_dice_raw.txt', 'a+', encoding='utf-8') as fout:
            fout.write(result)
            fout.write('\n')
        time.sleep(2)  # ATTENTION: Limitation is 20 msg/min/chat.
    except Exception as e:
        print(e)
