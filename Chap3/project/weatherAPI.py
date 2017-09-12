#! /urs/bin/env python3
# coding=utf-8

import re, string, requests, os, json



    
# 查询天气
def weather(city):
    location = str(city)
    personalKey = 'aujwvfmqnvpkrgrq'
    url = 'https://api.seniverse.com/v3/weather/now.json?key=' + personalKey  + '&location=' + location  + '&language=zh-Hans&unit=c'
    data = requests.get(url)
    import json
    json = json.loads(data.text) 
    
    if 'status' in json:
        failed = "查询失败！"
        return failed
    else:    
        c = json["results"][0]["location"]["name"]
        w = json["results"][0]["now"]["text"]
        t = json["results"][0]["now"]["temperature"]
        updateTime = json["results"][0]["last_update"]
            
        collectCity = c 
        collect = c +'\n' + w + '\n' + t + '℃' + '\n' + '更新时间：' + updateTime
        
        return collect
         