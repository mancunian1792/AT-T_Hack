#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 02:25:37 2018

@author: mancunian92
"""

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '2fe46b07420145988dfe17fa53d95c06',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
})

try:    
    with open("/home/mancunian92/Desktop/harish.png", "rb") as imageFile:
        f = imageFile.read()
        body = bytearray(f)
    conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


####################################