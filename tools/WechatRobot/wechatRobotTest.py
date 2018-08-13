#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 09:53:06 2018

@author: madawei1
"""


import requests
import itchat
import random

KEY = '8c3db0d35ae14779867f8168cb9bdca8'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots=['——By机器人小杨','——By机器人白杨','——By反正不是本人']
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply

itchat.auto_login(enableCmdQR=-2)#数字1，-1，2，大小调节尺寸，正负号调节反色
itchat.run()

itchat.logout()