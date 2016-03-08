#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import random, requests, sys, json, time
import datetime
"""
http://oauth.vk.com/authorize?client_id=3087106&scope=messages,wall,offline&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token
"""
str1='''
some text 1
'''

str2='''
some text 2
'''

str3='''
some text 3
'''
vk='''https://api.vk.com/method/'''
def send_congr(id, token, v=5.45):
    congr=[str1, str2, str3]
    params={}
    params['id']=id
    params['order']='''hints'''
    params['access_token']=token
    params['v']=v
    params['fields']='sex'
    url=vk+'friends.get'
    js=json.loads(requests.get(url, params=params).text)
    friends=js['response']['items']
    params.pop('fields')
    params.pop('order')
    url=vk+'messages.send'
    congratilated=set(int(line.strip()) for line in open('friends.txt'))
    print(congratilated)
    for f in friends:
        if f['sex']==1 and int(f['id']) not in congratilated:
            r=random.randint(0,2)
            text=congr[r]
            print(f['id'], '  ', f['first_name'],'  ', f['last_name'])
            params['user_id']=f['id']
            params['message']=text
            r=requests.post(url, params=params)
            print(r.text, '  ', datetime.datetime.now(), '\n')
            res=json.loads(r.text)
            try:
                res=res['error']
            except KeyError:
                with open('friends.txt', 'a') as fl:
                    fl.write(str(f['id'])+'\n')
                    fl.close()
                time.sleep(random.randint(3,7))
    
send_congr(sys.argv[1], sys.argv[2])
    
