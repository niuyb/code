# -*- coding: utf8 -*-
import math
import os, sys, datetime, time, urllib2, urllib, json

debug = 1
prefix = "idlethree"
workPath = "/home/tyhall51/hall5/source/idlethree/src/idlethree"
distFilePath = "/home/tyhall51/hall5/run/hall/bin/idlethree"

testUserId = 10001
host = "http://192.168.20.39:8000/v2/idlethree/api"


def initArgs():
    global debug
    global prefix
    global workPath
    global destFilePath
    global testUserId
    global host

    srcPath = os.path.dirname(__file__)
    fullPath = os.path.join(srcPath, 'env.json')
    with open(fullPath, 'r') as f:
        data = "\n".join(f.readlines())
        conf = json.loads(data)
        debug = conf.get('debug', 1)
        prefix = conf.get('prefix', 'idlethree')
        workPath = conf.get("workPath", "/home/tyhall51/hall5/source/idlethree/src/idlethree")
        distFilePath = conf.get("destFilePath", "/home/tyhall51/hall5/run/hall/bin/idlethree")
        testUserId = conf.get('testUserId', 1)
        host = conf.get('host', "")


def request(cmd, action, params=None, userId=None):
    if params is None:
        params = {}
    params.update({
        'cmd': cmd,
        'action': action,
        'gameId': 129,
        'userId': testUserId,
        'stoken': 'abcd',
        'clientId': 'H5_2.0_weixin.weixin.0-hall129.weixin.hulaisg'
    })

    if userId:
        params['userId'] = userId

    r = urllib2.urlopen(host, urllib.urlencode(params))
    return json.loads(r.read())


def printLog(content):
    if debug:
        print(content)


def getTodayChangeFiles(workPath):
    try:
        if workPath:
            os.chdir(workPath)

        today = time.strftime("%Y-%m-%d")
        p = os.popen('find . -maxdepth 100 -newermt "{today}" -type f'.format(today=today), 'r')
        data = p.read()
        if data:
            data = data.split('\n')
        else:
            data = []
        p.close()
        return data
    except Exception as e:
        print(e)
        return []


def filterChangeFiles(files, workPath, distFilePath):
    """
    获取有真正变化的问题，根据时间
    """
    result = []
    for f in files:
        if not f or 'py' not in f:
            continue
        motify_time = int(os.path.getmtime(os.path.join(workPath, f)))
        if distFilePath:
            if not os.path.exists(os.path.join(distFilePath, f)):
                result.append(f)
            else:
                old_modify_time = int(os.path.getmtime(os.path.join(distFilePath, f)))
                if old_modify_time < motify_time:
                    result.append(f)
    return result


def copyFile(files, workPath, distFilePath):
    for f in files:
        source_file = os.path.join(workPath, f)
        dist_file = os.path.join(distFilePath, f)
        os.system('cp {sourceFile} {distFile}'.format(sourceFile=source_file, distFile=dist_file))
        printLog('  system command: cp {sourceFile} {distFile}'.format(sourceFile=source_file, distFile=dist_file))


def noticeServer(serverAddr, change_files, prefix):
    transform = []
    for filename in change_files:
        # eg "./plugins/whitelist/white_list.py"
        file_package = prefix + '.' + filename[2:-3]
        file_package = file_package.replace('/', '.')
        transform.append(file_package)
    return request('game', 'debug_auto_reload', {'processId': 'ut', 'change_files': transform})


def boot():
    printLog('== begin ==+')
    initArgs()
    # check today change files
    change_files = getTodayChangeFiles(workPath)
    printLog('\n检测今日文件变化:%s' % len(change_files))
    format_log = '\n'.join(map(lambda d: "  %s" % d, change_files))
    printLog(format_log)

    # filter not change files
    change_files = filterChangeFiles(change_files, workPath, distFilePath)
    printLog('\n有修改的文件变化:%s' % len(change_files))
    format_log = '\n'.join(map(lambda d: "  %s" % d, change_files))
    printLog(format_log)

    # copy file to run/bin directory
    printLog('\n拷贝文件:%s' % len(change_files))
    copyFile(change_files, workPath, distFilePath)

    # notice server to reload py code when has change_files
    if change_files:
        printLog('\n通知服务进行reload')
        resp = noticeServer(host, change_files, prefix)
        printLog("  " + str(resp))

    printLog('== end ==')


# boot()


if __name__ =="__main__":

    pass