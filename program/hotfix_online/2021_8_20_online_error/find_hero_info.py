#!/usr/bin/env python
# encoding: utf-8
# author: Ksar4
# date: 2021/8/14 18:38


# coding: utf-8

import os, json, sys

folder = r'D:\file\git_code\program\hotfix_online\log2'

debug_hero_info_line = """08-08 00:09:28.877142 [823691] I 1088582272 | [ ] out<< [{"cmd":"game","result":{"action":"get_hero_info","gameId":129,"userId":39443346,"hero":{"userId":39443346,"heroId":"Hero_CaoRen","tier":6,"level":260,"star":17,"fp":864116,"lockInfo":{"state":1,"unlockTs":0,"unlockNeedTime":300},"skinId":null,"skinType":null,"magic_weapon":{"lock":0,"already_unlock":1,"star":6,"level":3,"grow_line":6,"change_grow_line":-1},"soldierItemId":"60e7866b0d1c5a4fbce6e04e","artifact":"SA:61b2757f-5140-40e2-b99a-36dbb0889db4","heroItemId":"5fd31ff24079d86b0767a1f7","filter":"designation","maxTier":6,"maxLevel":260,"atkType":"physics","pro":"roudun","camp":"wei","attack":168572,"hp":6653080,"ma":75659,"pa":74461,"speed":2126,"exDmg":0.1,"exDr":0.808,"arp":0,"tenacity":0,"crit":0.25,"exCrit":0.2,"reliefCrit":0,"exSdmg":0.4,"sAgainst":0.1,"block":0.53,"precision":0,"hitRatio":0,"unCtrl":0.05,"unCrit":0,"cntDmgInc":0.1,"cntDr":0.272,"unFrozen":0,"unStun":0,"unSilence":0,"unBleed":0.068,"unPoison":0,"unBurn":0,"skills":[{"skillId":"SKILL_Ju_Shou_Cover1","skillLevel":1,"skillParams":{},"skillName":"\u3010\u589e\u5e45\u3011\u636e\u5b88","skillDesc":"\xb7\u5bf9\u968f\u673a3\u540d\u654c\u4eba\u9020\u6210\u653b\u51fb198%\u7684\u4f24\u5bb3\\n\xb7\u964d\u4f4e\u76ee\u680725%\u901f\u5ea63\u56de\u5408\\n\xb7\u4e3a\u5168\u4f53\u53cb\u519b\u589e\u52a0\u5176\u751f\u547d\u4e0a\u965024%\u7684\u62a4\u76fe"},{"skillId":"SKILL_Jie_Wer","skillLevel":1,"unlockAtTier":1,"skillName":"\u89e3\u56f4","skillDesc":"\xb7\u751f\u547d\u589e\u52a025%\uff0c\u53cc\u9632\u589e\u52a035%\\n\xb7\u6fd2\u6b7b\u65f6\uff0c\u4e3a\u751f\u547d\u503c\u6700\u4f4e\u7684\u53cb\u519b\u589e\u52a0\u5176\u81ea\u8eab\u751f\u547d\u4e0a\u965055%\u7684\u62a4\u76fe"},{"skillId":"SKILL_Gu_Ruo_Jin_Tang","skillLevel":1,"unlockAtTier":3,"skillName":"\u56fa\u82e5\u91d1\u6c64","skillDesc":"\xb7\u4e0a\u573a\u65f6\uff0c\u4e3a\u5168\u4f53\u53cb\u65b9\u589e\u52a0\u66f9\u4ec1\u751f\u547d\u4e0a\u965010/13/15/17/20/30%\u7684\u62a4\u76fe\\n\uff08\u6570\u503c\u57285/9/13/16/18/21\u661f\u65f6\u63d0\u5347\uff09"},{"skillId":"SKILL_Gui_Shen_Zhi_Yong","skillLevel":1,"unlockAtTier":5,"skillName":"\u9b3c\u795e\u4e4b\u52c7","skillDesc":"\xb7\u666e\u901a\u653b\u51fb\u53d8\u4e3a\u653b\u51fb\u654c\u65b9\u524d\u6392\u654c\u4eba\\n\xb7\u670935%\u6982\u7387\u4f7f\u76ee\u6807\u51b0\u51bb2\u56de\u5408"},{"skillId":"SKILL_Bi_Hu_Stone2","skillLevel":1,"skillName":"\u3010\u7075\u77f3\u3011\u5e87\u62a4","skillDesc":"\u4e0a\u573a\u65f6\uff0c\u63d0\u5347\u5168\u4f53\u53cb\u65b93.0%\u7684\u51cf\u4f24\u7387\uff0c\u6301\u7eed1\u56de\u5408"}],"canUpgradeLevel":false,"canUpgradeTier":false,"canChange":true}}}] """

map_heor_id = []

hero_dict={}

files = [
    "2021_08_07_%s_hero.txt",
    "2021_08_08_%s_hero.txt",
    "2021_08_09_%s_hero.txt",
    "2021_08_10_%s_hero.txt",
    "2021_08_11_%s_hero.txt",
    "2021_08_12_%s_hero.txt",
]


def readFile(fileName, execFunc, action):
    if not os.path.exists(fileName):
        # print 'file not exists', fileName
        return


    with open(fileName, 'r') as f:
        for line in f.readlines():
            execFunc(line, action)


    # print "------>len ", len(map_heor_id)


    fw = open('test.txt', 'w')
    fw.write(json.dumps(hero_dict))
    fw.close()


def executeHeroInfoMsg(line, action):
    index = line.find(action)
    if index == -1:
        # print 'action not exists'
        return False

    targetIndex = line.find('heroItemId')
    if targetIndex == -1:
        # print 'heroId not exists'
        return False

    # 找整行信息
    startIndex = line.find("out") + 6
    # allLine = line[startIndex:]
    # tempdict  = json.loads(allLine)



    # 找到heroItemId
    _ = line[targetIndex+13: targetIndex+40]
    heroItemId = _[:_.find('"')]
    if heroItemId in map_heor_id:
        # print 'heroId repeat'
        return False

    map_heor_id.append(heroItemId)

    hero_dict[heroItemId] = line[startIndex:]

    print line[:22], heroItemId







def boot():
    # actions = [
    #     "get_hero_info",
    #     "get_equipment",
    #     "get_magic_weapon",
    #     "hero_artifact_info"
    # ]
    userId = [38947162,5000112674,5000170614,38933396,5000108515,5001543914,52583838,39443346,39449056,49316763,49323362,53730443,53893895,5000156153,5001068447,5001069044,5001069434,5001070220,5001070422,5001351075,5001351561,5001501724]
    action = "hero_artifact_info"

    for fileName in files:
        for uid in userId:
            print '===================', fileName % uid,'==================='
            readFile(os.path.join(folder, fileName % uid), executeHeroInfoMsg, action)


    print len(hero_dict)

# boot()

if __name__ == "__main__":

    print (9980 % 800) + 1