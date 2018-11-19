#encoding:utf8

import requests

# 建立一个请求会话
session = requests.session()

# post请求关键字
def get(url):
    # 发送请求
    result = session.get(url,verify=False)
    # 处理异常
    return result.content.decode('utf8')








