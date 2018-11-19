# coding:utf8

import os
import xlrd

# 整个excel工作簿缓存
workbook = None
# 当前工作sheet
sheet = None
# 逐行读取时的行数
rr = 0
# 当前sheet的行数
r = 0


# 打开excel
def open_excel(srcfile):
    global workbook, sheet, r, rr
    if not os.path.isfile(srcfile):
        print("error：%s not exist!" % (srcfile))
        return

    # 设置读取excel使用utf8编码
    xlrd.Book.encoding = "utf8"
    # 读取excel内容到缓存workbook
    workbook = xlrd.open_workbook(filename=srcfile)
    # 选取第一个sheet页面
    sheet = workbook.sheet_by_index(0)
    # 设置r为当前sheet的行数
    r = sheet.nrows
    rr = 0
    return


# 切换sheet页面
def get_sheets():
    # 获取所有sheet的名字，并返回
    sheets = workbook.sheet_names()
    print(sheets)
    return sheets


# 切换sheet页面
def set_sheet(name):
    global sheet, r, rr
    # 通过sheet名字，切换sheet页面
    sheet = workbook.sheet_by_name(name)
    r = sheet.nrows
    rr = 0
    return


# 逐行读取
def readline(i):
    global sheet
    global rr
    row = None
    row1 = None
    rr = i

    # 如果当前还没到最后一行，则读取一行
    if (rr < r):
        row = sheet.row_values(rr)
        rr = rr + 1
        i = 0
        row1 = row
        # 如果读取的是小数，则判断是不是整数
        for strs in row:
            if type(strs) == float:
                if strs == int(strs):
                    # 如果是10.0这样的，则取整；如果要输入10.0，请使用在excel里面输入'10.0
                    row1[i] = str(int(strs))
                else:
                    # 其他数据，转为字符串
                    row1[i] = str(strs)
            else:
                row1[i] = strs
            i = i + 1

    return row1


# 调试
if __name__ == '__main__':
    open_excel('../lib/tmp.xls')
    get_sheets()
