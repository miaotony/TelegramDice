#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analysis.py
Telegram Dice Analysis
A simple analysis.
一个简单的数据分析

@Author: MiaoTony
@Create time: 20200429
"""


import json


# 先来看看飞镖🎯 Let's see the result of dart.
results_dart_list = []
cnt = 0
with open('results_dart_all_raw.txt', 'r', encoding='utf-8') as fin:
    while True:
        line = fin.readline()
        if not line:
            break
        # print(line)
        line_json = json.loads(line)
        print(line_json)
        if line_json.get('ok') == True:
            value = line_json.get('result').get('dice').get('value')
            if value:
                cnt += 1
                print(cnt, value)
                results_dart_list.append(value)
print(results_dart_list)
print(len(results_dart_list))

stats_dart = {i: 0 for i in range(1, 7)}
# print(stats_dart)
for i in results_dart_list:
    stats_dart[i] += 1
print("Stats of dart:")
print(stats_dart)


# 再来看看骰子🎲咋样 Let's see the result of dice.
results_dice_list = []
cnt_dice = 0
with open('results_dice_all_raw.txt', 'r', encoding='utf-8') as fin:
    while True:
        line = fin.readline()
        if not line:
            break
        # print(line)
        line_json = json.loads(line)
        print(line_json)
        if line_json.get('ok') == True:
            value = line_json.get('result').get('dice').get('value')
            if value:
                cnt_dice += 1
                print(cnt_dice, value)
                results_dice_list.append(value)
print(results_dice_list)
print(len(results_dice_list))

stats_dice = {i: 0 for i in range(1, 7)}
# print(stats_dice)
for i in results_dice_list:
    stats_dice[i] += 1
print("Stats of dice:")
print(stats_dice)


# 保存结果 Save the results to file.
with open('results_dart_all.txt', 'w', encoding='utf-8') as fout:
    fout.write(str(results_dart_list))
    fout.write('\n')
    fout.write(str(stats_dart))

with open('results_dice_all.txt', 'w', encoding='utf-8') as fout:
    fout.write(str(results_dice_list))
    fout.write('\n')
    fout.write(str(stats_dice))
