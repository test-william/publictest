#encoding:utf8

import requests
import json
from common import writer

# 保存参数
params = {}

# 建立一个请求会话
session = requests.session()
# 保存json处理结果
jsonres = None

# post请求关键字
def post(url,param):
    global jsonres
    # 发送的参数
    p={}
    param = getparams(param)
    # 对标准的http请求参数处理为dist
    if len(param)>0:
        # 分割为键值对
        param = param.split('&')
        for s in param:
            # 分割得到键和值
            ss = s.split('=')
            p[ss[0]] = ss[1]
    # 发送请求
    result = session.post(url,data=p)
    # 处理异常
    try:
        jsonres = None
        # 将结果进行json处理
        jsonres = json.loads(result.content.decode('utf8'))
        print("PASS：请求成功")
        writer.write(writer.row, writer.clo, "PASS")
        writer.write(writer.row, writer.clo + 1, str(jsonres))
    except Exception as e:
        print("FAIL：请求失败，结果处理报错：")
        print(e)
        writer.write(writer.row, writer.clo, "FAIL")
        writer.write(writer.row, writer.clo + 1, e)

    print(str(jsonres))


# 断言相等
def assertequals(key,value):
    global jsonres
    if jsonres is None:
        print("FAIL：json解析错误！")
        writer.write(writer.row, writer.clo, "FAIL")
        writer.write(writer.row, writer.clo + 1, "json解析错误！")
        return

    if str(jsonres[key])==getparams(value):
        print("PASS：断言成功")
        writer.write(writer.row, writer.clo, "PASS")
        writer.write(writer.row, writer.clo + 1, jsonres[key])
    else:
        print("FAIL：断言失败，实际结果：" + str(jsonres[key]))
        writer.write(writer.row, writer.clo, "FAIL")
        writer.write(writer.row, writer.clo + 1, str(jsonres[key]))

# 保存参数
def savejson(key,param):
    global jsonres,params
    try:
        params[param] = jsonres[key]
        print("PASS：保存参数成功")
        writer.write(writer.row, writer.clo, "PASS")
        writer.write(writer.row, writer.clo + 1, jsonres[key])
    except Exception as e :
        print("FAIL：保存参数失败")
        print(e)
        writer.write(writer.row, writer.clo, "FAIL")
        writer.write(writer.row, writer.clo + 1, "保存参数失败")

# 添加头
def addheader(key,value):
    global session
    session.headers[key] = getparams(value)
    print("PASS：添加头成功")
    writer.write(writer.row, writer.clo, "PASS")
    writer.write(writer.row, writer.clo + 1, str(session.headers))

# 获取参数值
def getparams(param):
    global params
    for key in params.keys():
        try:
            param = param.replace('{'+key+'}',params[key])
        except:
            pass
    return param









