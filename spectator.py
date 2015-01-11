from Crypto.Cipher import Blowfish
import requests
import json
import base64
from pprint import pprint
import zlib
from SummonerParser import Parser
import sys
import time

params = {
    "server" : "spectator.na.lol.riotgames.com:80",
    "method" : "",
    "platformId" : "NA1",
    "gameID" : "",
    "parameter" : "1"
}

endpoint = "http://%(server)s/observer-mode/rest/consumer/%(method)s/%(platformId)s/%(gameID)s/%(parameter)s/token"

#print endpoint % params

params["gameID"] = '1652568300'
encryptionkey = 'srkE4Oy3U8KgPf7FwjmBNEAKHgHnLibK'

#encryptionKey = q["encryptionKey"]

#print base64.b64decode(encryptionKey)

#decodedencryptionkey = base64.b64decode(encryptionKey)

endkeyframe = -1
previouskeyframe = -1
currentkeyframe = 0

#while currentkeyframe != endkeyframe:
#params["method"] = "getLastChunkInfo"
#print endpoint % params

#r = requests.get(endpoint % params)
#r = json.loads(r.content)

#pprint(r)
while True:
    params["method"] = "getGameMetaData"
    params["parameter"] = '1'
    q = requests.get(endpoint % params)
    q = json.loads(q.content)
    if endkeyframe != q['endGameKeyFrameId']:
        print 'Game has ended'
        break
    #pprint(q)
    previouskeyframe = currentkeyframe
    #print q['lastKeyFrameId']
    params["method"] = "getLastChunkInfo"
    r = requests.get(endpoint % params)
    r = json.loads(r.content)
    currentkeyframe = r['keyFrameId']
    sys.stdout.flush()
    if previouskeyframe == currentkeyframe:
        print 'Waiting for next keyframe, %s' %currentkeyframe
        sys.stdout.flush()
        time.sleep(30)
        continue

    params["method"] = "getKeyFrame"
    params["parameter"] = r['keyFrameId'] #make more consistant
    s = requests.get(endpoint % params)

    bf = Blowfish.new(params['gameID'], Blowfish.MODE_ECB)



    decodedkey = base64.b64decode(encryptionkey)
    decodedkey = bf.decrypt(decodedkey)
    
    paddingbytes = ord(decodedkey[-1])
    keywopadding = decodedkey[:-paddingbytes]

    realencryptionkey = Blowfish.new(keywopadding, Blowfish.MODE_ECB)
    datawpadding = realencryptionkey.decrypt(s.content)
    paddingbytes = ord(datawpadding[-1])
    datawopadding = datawpadding[:-paddingbytes]

    #print datawopadding

    data = zlib.decompressobj(zlib.MAX_WBITS|32)
    answer = data.decompress(datawopadding)
    #print base64.b16encode(answer)

    Parser(base64.b16encode(answer))
    sys.stdout.flush()
    #break
