#!/usr/bin/env python
# encoding: utf-8
# author: Ksar4
# date: 2021/8/16 10:24
import json

from poker.entity.dao import daobase

def GetArtifactId(userId,stoneArtifactId):
    K_STONE = "bqp:stone:h:s:%s"

    rKey = K_STONE%userId

    rDict = daobase.executeUserCmd(userId, "HGET", rKey, stoneArtifactId)
    rDict = json.loads(rDict)

    tempArtifactId = rDict.get("artifact",False)
    if tempArtifactId:
        return tempArtifactId
    else:
        return None




