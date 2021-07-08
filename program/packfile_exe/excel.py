#!/usr/bin/env python
# encoding: utf-8
# author: Ksar4
# date: 2021/6/21 11:26

# 依赖的三方库 要放到打包程序的同一目录下

from copy import deepcopy
import xlrd
import json
import os


class Excel2Json():

    def __init__(self):

        # self.data_dir = os.getenv('AUTO_DATACENTER', '存放excel的文件夹地址')

        self.filename = '0.json'
        # self.filePath = r"D:\file\git_code\program\resourceFund.xls"
        self.filePath = os.getcwd()+r"\resourceFund.xls"
        print(self.filePath)

        self.sheetNames = ''
        print(self.filePath)

        self.resultsDict = {"taskUnits": []}
        self.jsonResult = {}


        self.taskUnitId = "sg.task.resource.fund.%s"
        self.notMetRewardCond = ""
        self.typeId = "sg.bought.product"
        self.minCount = 1
        self.productId = "H5_P129_tower_army_%s"


        self.tasksEmpty = {
                "kindId": "",
                "typeId": "sg.task.simple",
                "name": "",
                "desc": "",
                "pic": "",
                "todo": "hall_tower|fight",
                "count": 0,
                "totalLimit": 1,
                "inheritPrevTaskProgress": 1,
                "inspectors": [
                    {
                        "typeId": "sg.tower.level"
                    }
                ],
                "rewardContent": {
                    "typeId": "FixedContent",
                    "items": []
                },
                "militaryRank": 0
        }



        # filename = os.path.listdir(file)

    # 获取excel数据源
    def get_data(self,filePath):
        """获取excel数据源"""
        try:
            data = xlrd.open_workbook(self.filePath)
            return data
        except Exception as e:
            print(u'excel表格读取失败：%s' % e)
            return None

    def get_productId(self,roundList,productList):

        productDict = {}
        for index in range(1,len(roundList)):
            if roundList[index] not in productDict.keys() :
                productDict[int(roundList[index])] = productList[index]
            else:
                pass
        return productDict

    def getEmptyData(self,maxRound,ProductDict):
        for i in range(1,int(maxRound)+1):
            tempDict = {
                "taskUnitId":self.taskUnitId%i,
                "typeId": self.taskUnitId % i,
                "notMetRewardCond": self.notMetRewardCond,
                "rewardCond": {
                    "typeId": self.typeId,
                    "productId":ProductDict[i],
                    "minCount": self.minCount
                },
                "pools": [
                    {
                        "nextType": "allOpen",
                        "taskOrder":[],
                        "tasks": []
                    }
                ]
            }
            self.resultsDict["taskUnits"].append(tempDict)



    def Excel2Json(self):

        workbook = self.get_data(self.filePath)
        if workbook is not None:
            # # 抓取所有sheet页的名称
            # worksheets = workbook.sheet_names()
            sheet1_name = workbook.sheet_names()[0]
            sheet1 = workbook.sheet_by_name(sheet1_name)

            allRow = sheet1.nrows

            titleRow = sheet1.row_values(0)
            RewardTitle = titleRow[7:]
            # print(titleRow)

            roundRow = sheet1.col_values(1)

            roundRow.remove("RoundNum")
            maxRound = int(max(roundRow))

            tempProductDict = self.get_productId(sheet1.col_values(1),sheet1.col_values(2))
            self.getEmptyData(maxRound,tempProductDict)

            for row in range(1,int(allRow)):
                temprow = sheet1.row_values(row)
                # print(temprow)
                tempRound = int(temprow[1])
                tempTaskUnits = self.resultsDict["taskUnits"][tempRound-1]
                tempTasks  = deepcopy(self.tasksEmpty)

                tempTasks["kindId"] = int(temprow[3])
                tempTasks["name"] = str(temprow[4])
                tempTasks["desc"] = str(temprow[5])
                tempTasks["count"] = int(temprow[6])

                # reward
                RewardList = temprow[7:]
                # print(RewardList)
                for index in range(len(RewardList)):
                    RewardNum = int(RewardList[index])
                    if RewardNum != 0:
                        RewardDict = {
                            "count": RewardNum,
                            "itemId": RewardTitle[index]
                          }
                        tempTasks["rewardContent"]["items"].append(RewardDict)

                    else:
                        pass

                tempTaskUnits["pools"][0]["taskOrder"].append(tempTasks["kindId"])
                tempTaskUnits["pools"][0]["tasks"].append(tempTasks)


            print(self.resultsDict)
            self.jsonResult = json.dumps(self.resultsDict)

            return self.resultsDict
        else:
            return None


    def save_Json(self):

        jsonData = json.dumps(self.resultsDict)
        fileObject = open(self.filename, 'w')
        fileObject.write(jsonData)
        fileObject.close()

        # with open(self.filename, 'w') as file_obj:
        #     json.dump(self.resultsDict, file_obj)



e = Excel2Json()
e.Excel2Json()
e.save_Json()




