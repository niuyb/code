# -*- coding:utf-8 -*-
import json
import random
import time

from datetime import datetime, timedelta

from hashlib import md5


randSeed = (int(time.time()) + random.randint(0, 1000))


print randSeed