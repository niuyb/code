#!/usr/bin/env python
# encoding: utf-8
# author: Ksar4
# date: 2021/8/16 14:41

import json


a_list = [{"cmd":"game","result":{"action":"get_config","gameId":129,"userId":32991105,"datamerge":{},"roleId":32991105}},{"cmd":"game","result":{"action":"redpoint","userId":32991105,"clear":True,"module":32,"roleId":32991105}},{"cmd":"game","result":{"action":"get_redpoint","gameId":129,"userId":32991105,"datamerge":{"redpoint":"0001100000001000000000000010000000000000000001100000000000000100000011110110001000010010111"},"roleId":32991105}},{"cmd":"game","result":{"action":"check_login_tasks","gameId":129,"userId":32991105,"tasks":[{"action":"pop_mc_time_limit","params":{"groupList":[{"showType":7,"groupName":"\u5206\u7ec400","productList":[{"id":"H5_P129_qx210813_tl6","name":"\u4e03\u5915\u8d85\u503c\u793c\u76d2","nameurl":"","price":"6","priceurl":"http://hlsgqn.tytuyoo.com/icon/item/rmb_store3.png","desc":"2*\u83b2\u82b1\u706f + 60*\u559c\u9e4a + 60*\u5143\u5b9d + 60vip\u7ecf\u9a8c","discount":[],"pic":"https://hlsghw.tytuyoo.com/3kingdoms/acts/xianshilibao.png","tag":"","buy_type":"direct","price_diamond":"60","clientParams":{"gift_cdn":{"and":{"tag_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/jinrixianding.png","title_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/chaozhi.png"},"android":{"tag_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/jinrixianding.png","title_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/chaozhi.png"},"qq_ios":{"title_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_5_new_wxqq.png"},"wx_ios":{"title_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_5_new_wxqq.png"}},"gift_name":"\u4e03\u5915\u8d85\u503c\u793c\u76d2","hengfubanner":"999%\u6d3b\u52a8\u8d85\u503c","hulaisg":{"cornerMarker":2,"iswechat":0,"mailDesc":"\u798f\u5229\u5df2\u53d1\u653e\u81f3\u8d26\u6237\uff0c\u8bf7\u60a8\u786e\u8ba4\uff01","mailTitle":"\u516c\u4f17\u53f7\u798f\u5229"},"pic":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_7_new3.png","show_type":7,"tap_color":"#5A450C","tap_text":"\u672c\u5c0f\u59d0\u53ea\u505c\u755924\u5c0f\u65f6\uff0c\u9884\u8d2d\u4ece\u901f\uff01","timeLimitGift":{"endTime":"2021-08-19 23:59:59","limitBuyCount":1,"proExpireTs":7200,"productType":"growUp"},"vip_color":"#9EECFF","xg_color":"#614C12"},"vipExp":60,"content":[{"item":"user:diamond","count":60},{"item":"item:4287","count":2},{"item":"item:4275","count":60},{"item":"user_vip_exp","count":60}],"remainBuyCount":1,"proExpireTs":1628963459,"limitBuyCount":1,"productType":"growUp","last_cycle_ts":1628956259,"lastPopTime":1628962138,"currPopCnt":3,"topCount":16,"trigger_times":9,"productId":"H5_P129_qx210813_tl6","isTop":True}]},{"showType":7,"groupName":"\u5206\u7ec42","productList":[{"id":"H5_P129_JTZhf","name":"\u6df7\u670d\u6b66\u795e\u793c\u5305","nameurl":"","price":"98","priceurl":"","desc":"10\u4e2a\u8fd8\u9b42\u4e39+1\u4e2a\u901f\u6548\u4e39+980\u5143\u5b9d+980VIP\u70b9","discount":[],"pic":"https://hlsghw.tytuyoo.com/3kingdoms/acts/xianshilibao.png","tag":"","buy_type":"direct","price_diamond":"980","clientParams":{"gift_cdn":{"and":{"tag_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/growth_discount_newuser1.png","title_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/hundu.png"},"android":{"tag_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/growth_discount_newuser1.png","title_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/hundu.png"},"qq_ios":{"title_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_5_new_wxqq.png"},"wx_ios":{"title_cdn":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_5_new_wxqq.png"}},"gift_name":"\u56e2\u6218\u5fc5\u5907","hengfubanner":"\u56e2\u6218\u5fc5\u5907","hulaisg":{"cornerMarker":2,"iswechat":0,"mailDesc":"\u798f\u5229\u5df2\u53d1\u653e\u81f3\u8d26\u6237\uff0c\u8bf7\u60a8\u786e\u8ba4\uff01","mailTitle":"\u516c\u4f17\u53f7\u798f\u5229"},"pic":"https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_7_new3.png","show_type":7,"tap_color":"#5A450C","tap_text":"\u70ed\u8840\u56e2\u6218\uff0c\u6709\u5907\u65e0\u60a3\uff01\u5fc3\u52a8\u4e0d\u5982\u884c\u52a8~","timeLimitGift":{"endTime":"2021-08-15  21:59:59","limitBuyCount":1,"proExpireTs":90000,"productType":"growUp"},"vip_color":"#9EECFF","xg_color":"#614C12"},"vipExp":980,"content":[{"item":"item:1030","count":10},{"item":"item:1029","count":1},{"item":"user:diamond","count":980},{"item":"user_vip_exp","count":980}],"remainBuyCount":999998,"proExpireTs":1629035999.0,"limitBuyCount":1,"productType":"growUp","last_cycle_ts":1628946011,"lastPopTime":1628962138,"topCount":490,"curBuyCount":0,"trigger_times":106,"currPopCnt":5,"productId":"H5_P129_JTZhf","isTop":True}]}]}},{"action":"pop_first_buy_window","params":{"typeId":"todotask.first_buy_window"}}],"roleId":32991105}},{"cmd":"newbie","result":{"action":"update_guidestep","gameId":129,"userId":32991105,"guideStep":10165,"guideStatus":False,"newDoneList":[10120,10165],"roleId":32991105}},{"cmd":"newbie","result":{"action":"update_guidestep","gameId":129,"userId":32991105,"guideStep":10165,"guideStatus":False,"newDoneList":[10120,10165]}},{"cmd":"newbie","result":{"action":"update_guidestep","gameId":129,"userId":32991105,"guideStep":10165,"guideStatus":False,"newDoneList":[10120,10165]}}]

temp_dict = {'cmd': 'game', 'result': {'action': 'check_login_tasks', 'gameId': 129, 'userId': 32991105, 'tasks': [{'action': 'pop_mc_time_limit', 'params': {'groupList': [{'showType': 7, 'groupName': '\\u5206\\u7ec400', 'productList': [{'id': 'H5_P129_qx210813_tl6', 'name': '\\u4e03\\u5915\\u8d85\\u503c\\u793c\\u76d2', 'nameurl': '', 'price': '6', 'priceurl': 'http://hlsgqn.tytuyoo.com/icon/item/rmb_store3.png', 'desc': '2*\\u83b2\\u82b1\\u706f + 60*\\u559c\\u9e4a + 60*\\u5143\\u5b9d + 60vip\\u7ecf\\u9a8c', 'discount': [], 'pic': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/xianshilibao.png', 'tag': '', 'buy_type': 'direct', 'price_diamond': '60', 'clientParams': {'gift_cdn': {'and': {'tag_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/jinrixianding.png', 'title_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/chaozhi.png'}, 'android': {'tag_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/jinrixianding.png', 'title_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/chaozhi.png'}, 'qq_ios': {'title_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_5_new_wxqq.png'}, 'wx_ios': {'title_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_5_new_wxqq.png'}}, 'gift_name': '\\u4e03\\u5915\\u8d85\\u503c\\u793c\\u76d2', 'hengfubanner': '999%\\u6d3b\\u52a8\\u8d85\\u503c', 'hulaisg': {'cornerMarker': 2, 'iswechat': 0, 'mailDesc': '\\u798f\\u5229\\u5df2\\u53d1\\u653e\\u81f3\\u8d26\\u6237\\uff0c\\u8bf7\\u60a8\\u786e\\u8ba4\\uff01', 'mailTitle': '\\u516c\\u4f17\\u53f7\\u798f\\u5229'}, 'pic': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_7_new3.png', 'show_type': 7, 'tap_color': '#5A450C', 'tap_text': '\\u672c\\u5c0f\\u59d0\\u53ea\\u505c\\u755924\\u5c0f\\u65f6\\uff0c\\u9884\\u8d2d\\u4ece\\u901f\\uff01', 'timeLimitGift': {'endTime': '2021-08-19 23:59:59', 'limitBuyCount': 1, 'proExpireTs': 7200, 'productType': 'growUp'}, 'vip_color': '#9EECFF', 'xg_color': '#614C12'}, 'vipExp': 60, 'content': [{'item': 'user:diamond', 'count': 60}, {'item': 'item:4287', 'count': 2}, {'item': 'item:4275', 'count': 60}, {'item': 'user_vip_exp', 'count': 60}], 'remainBuyCount': 1, 'proExpireTs': 1628963459, 'limitBuyCount': 1, 'productType': 'growUp', 'last_cycle_ts': 1628956259, 'lastPopTime': 1628962138, 'currPopCnt': 3, 'topCount': 16, 'trigger_times': 9, 'productId': 'H5_P129_qx210813_tl6', 'isTop': True}]}, {'showType': 7, 'groupName': '\\u5206\\u7ec42', 'productList': [{'id': 'H5_P129_JTZhf', 'name': '\\u6df7\\u670d\\u6b66\\u795e\\u793c\\u5305', 'nameurl': '', 'price': '98', 'priceurl': '', 'desc': '10\\u4e2a\\u8fd8\\u9b42\\u4e39+1\\u4e2a\\u901f\\u6548\\u4e39+980\\u5143\\u5b9d+980VIP\\u70b9', 'discount': [], 'pic': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/xianshilibao.png', 'tag': '', 'buy_type': 'direct', 'price_diamond': '980', 'clientParams': {'gift_cdn': {'and': {'tag_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/growth_discount_newuser1.png', 'title_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/hundu.png'}, 'android': {'tag_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/growth_discount_newuser1.png', 'title_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/hundu.png'}, 'qq_ios': {'title_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_5_new_wxqq.png'}, 'wx_ios': {'title_cdn': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_5_new_wxqq.png'}}, 'gift_name': '\\u56e2\\u6218\\u5fc5\\u5907', 'hengfubanner': '\\u56e2\\u6218\\u5fc5\\u5907', 'hulaisg': {'cornerMarker': 2, 'iswechat': 0, 'mailDesc': '\\u798f\\u5229\\u5df2\\u53d1\\u653e\\u81f3\\u8d26\\u6237\\uff0c\\u8bf7\\u60a8\\u786e\\u8ba4\\uff01', 'mailTitle': '\\u516c\\u4f17\\u53f7\\u798f\\u5229'}, 'pic': 'https://hlsghw.tytuyoo.com/3kingdoms/acts/time_limit_gift/show_7_new3.png', 'show_type': 7, 'tap_color': '#5A450C', 'tap_text': '\\u70ed\\u8840\\u56e2\\u6218\\uff0c\\u6709\\u5907\\u65e0\\u60a3\\uff01\\u5fc3\\u52a8\\u4e0d\\u5982\\u884c\\u52a8~', 'timeLimitGift': {'endTime': '2021-08-15  21:59:59', 'limitBuyCount': 1, 'proExpireTs': 90000, 'productType': 'growUp'}, 'vip_color': '#9EECFF', 'xg_color': '#614C12'}, 'vipExp': 980, 'content': [{'item': 'item:1030', 'count': 10}, {'item': 'item:1029', 'count': 1}, {'item': 'user:diamond', 'count': 980}, {'item': 'user_vip_exp', 'count': 980}], 'remainBuyCount': 999998, 'proExpireTs': 1629035999.0, 'limitBuyCount': 1, 'productType': 'growUp', 'last_cycle_ts': 1628946011, 'lastPopTime': 1628962138, 'topCount': 490, 'curBuyCount': 0, 'trigger_times': 106, 'currPopCnt': 5, 'productId': 'H5_P129_JTZhf', 'isTop': True}]}]}}, {'action': 'pop_first_buy_window', 'params': {'typeId': 'todotask.first_buy_window'}}], 'roleId': 32991105}}


for i in a_list:
    
    print i

# temp_dict

temp = json.dumps(temp_dict,ensure_ascii=False)


print temp


if __name__ == "__main__":

    for i in userId:
        key = KEY.format(userId=i)
        ret = daobase.executeUserCmd(i, EXPIRE, key, EXPIRE_TIME)
        results[i] = ret