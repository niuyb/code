#!/usr/bin/env python
# encoding: utf-8
# author: Ksar4
# date: 2021/8/20 11:10

from itertools import chain
from copy import deepcopy
import poker.util.timestamp as pktimestamp

from freetime.util import log as ftlog
from poker.entity.configure import configure, gdata
from poker.entity.dao import gamedata
from poker.entity.events import tyeventbus as pkeventbus
from poker.entity.events.tyevent import EventConfigure
from poker.entity.dao import daobase
from poker.util import tools

from idlethree.entity.conf import GAME_ID
from idlethree.entity import itime, util, const, redpoint
from idlethree.item import item
from idlethree.entity import openapi




@classmethod
def _hincrby(cls, userId, field, count=1):
        field = "awardCountNew"
        key = cls.KEY.format(userId=userId)
        ret = daobase.executeUserCmd(userId, cls.HINCRBY, key, field, count)
        daobase.executeUserCmd(userId, cls.EXPIRE, key, cls.EXPIRE_TIME)
        return ret

from idlethree.plugins.activitys.qingdian_memory import DB
DB._hincrby = _hincrby