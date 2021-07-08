# -*- coding:utf-8 -*-
import json

from datetime import datetime, timedelta

from hashlib import md5


def md5digest(md5str):
    '''
    计算一个字符串的MD5值, 返回32位小写的MD5值
    '''
    m = md5()
    m.update(md5str)
    md5code = m.hexdigest()
    return md5code.lower()


params = {"method":"gmIncrItem","itemId":"item:1011","roleId":10001,"count":2,"platform":1,"editor":"guorong","code":"31f8bce4f8643e308c72e5317bf4235c"}

keys = sorted(params.keys())

checkstr = ''
for k in keys:
    # 签名只签 int， str， float(复合类型不参与签名)
    if k == "code" or not isinstance(params[k], ( str, int, float)):
        continue
    checkstr += k + '=' + str(params[k]) + '&'

# print checkstr
checkstr = checkstr[:-1]
checkstr = "sgGmSign-" + checkstr + "-X93KiNAd"

code = params.get("code")


# print "sgGmSign-count=33&id=60e57d501ffe40a71ea1914c&itemId=item:1010&method=gmIncrItem-X93KiNAd"
# print checkstr

curCode = md5digest(checkstr)


# print curCode == "812c3b8444f16aae7a89624052085379"




print (curCode)




