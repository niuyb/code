# -*- coding:utf-8 -*-
import json

from datetime import datetime, timedelta

msg={u'notMetRewardCond': u'\u8d2d\u4e70\u4e70\u4e70\u4e70\u4e70\u4e70\u4e70\u4e70\u4e70\u4e70\u4e70\u4e70\u8bd5\u70bc\u57fa\u91d1\u624d\u53ef', u'pools': [{u'nextType': u'allOpen', u'taskOrder': [12980351, 12980352, 12980353, 12980354, 12980355, 12980356, 12980357, 12980358, 12980359, 12980360, 12980361, 12980362, 12980363, 12980364, 12980365, 12980366, 12980367, 12980368, 12980369, 12980370], u'tasks': [{u'count': 5, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c5\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980001, u'militaryRank': 0, u'name': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c5\u5c42\u53ef\u4ee5\u9886\u53d6', u'pic': u'', u'rewardContent': {u'items': [{u'count': 1000, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 10, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c10\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980002, u'militaryRank': 0, u'name': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c10\u5c42\u53ef\u4ee5\u9886\u53d6.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 1500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 20, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c20\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980003, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 1500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 30, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c30\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980004, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 1500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 40, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c40\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980005, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 1500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 50, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c50\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980006, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 2000, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 70, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c70\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980007, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 1500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 90, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c90\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980008, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 1500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 110, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c110\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980009, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 2000, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 125, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c125\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980010, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 1500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 140, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c140\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980011, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 1500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 155, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c155\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980012, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 1500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 180, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c180\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980013, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 2000, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 200, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c200\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980014, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 3000, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 220, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c220\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980015, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 2000, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 240, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c240\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980016, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 2000, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 265, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c265\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980017, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 3000, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 280, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c280\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980018, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 2500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 300, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c300\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980019, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 2500, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}, {u'count': 320, u'desc': u'\u8bd5\u70bc\u8fbe\u5230\u7b2c320\u5c42', u'inheritPrevTaskProgress': 1, u'inspectors': [{u'typeId': u'sg.tower.level'}], u'kindId': 12980020, u'militaryRank': 0, u'name': u'.', u'pic': u'', u'rewardContent': {u'items': [{u'count': 3000, u'itemId': u'user_yuanbao'}], u'typeId': u'FixedContent'}, u'todo': u'hall_tower|fight', u'totalLimit': 1, u'typeId': u'sg.task.simple'}]}], u'rewardCond': {u'minCount': 1, u'productId': u'H5_P129_tower_fund_1', u'typeId': u'sg.bought.product'}, u'taskUnitId': u'sg.task.resource.fund.1', u'typeId': u'sg.task.resource.fund.1'}

#a = json.dumps(msg)

a = json.dumps(msg)
print a













# class A(object):
#
#     def a(self):
#         print "a"
#
#
# class B(A):
#     def a(self):
#         super(B, self).a()
#
#         pass
#
# B().a()


# class A(object):
#
#     def a(self):
#         print "a"
#
#
# class B(A):
#     def a(self):
#         pass
#
# b = B()
#
# A.a(b)