#encoding:utf8

from common import reader,writer
from keywords import HTTP as http

# 运行用例
def runCases(line):
    # 用例没有关键字
    if len(line[3])<1:
        print("用例格式错误："+str(line))
        writer.write(writer.row,writer.clo,"FAIL")
        writer.write(writer.row, writer.clo+1, "用例格式错误")
        return

    # 执行post关键字
    if line[3] == "post":
        http.post(line[4],line[5])
        return

    # 执行post关键字
    if line[3] == "assertequals":
        http.assertequals(line[4], line[5])
        return

    # 执行post关键字
    if line[3]=="savejson":
        http.savejson(line[4],line[5])
        return

    # 执行post关键字
    if line[3]=="addheader":
        http.addheader(line[4],line[5])
        return

    # 所有关键字都不匹配
    writer.write(writer.row, writer.clo, "FAIL")
    writer.write(writer.row, writer.clo + 1, "没有该关键字")

# 打开excel用例
reader.open_excel("../lib/HTTP.xls")
#写入的excel结果
writer.copy_open("../lib/HTTP.xls","../lib/HTTP-result.xls")
writer.clo = 7
# 逐行读取excel到list
for i in range(0,reader.r):
    # print(reader.readline(i))
    writer.row = i
    line = reader.readline(i)
    if len(line[0])>0 or len(line[1])>0:
        print(line)
    else:
        runCases(line)

writer.save_close()
