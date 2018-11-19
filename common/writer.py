# coding:utf8

import os
import xlrd
from xlutils.copy import copy

# 读取需要复制的excel
workbook = None
# 拷贝的工作空间
wb = None
# 当前工作的sheet页
sheet = None
# 记录生成的文件，用来保存
df = None
# 记录写入的行
row = 0
# 记录写入的列
clo = 0


# 复制并打开excel
def copy_open(srcfile, dstfile):
    global workbook
    global wb
    global sheet
    global df

    # 判断要复制的文件是否存在
    if not os.path.isfile(srcfile):
        print(srcfile + " not exist!")
        return

    # 判断要新建的文档是否存在，存在则提示
    if os.path.isfile(dstfile):
        print("warning：" + dstfile + " file already exist!")

    # 记录要保存的文件
    df = dstfile
    # 读取excel到缓存
    workbook = xlrd.open_workbook(filename=srcfile, formatting_info=True)
    # 拷贝
    wb = copy(workbook)
    # 默认使用第一个sheet
    sheet = wb.get_sheet('Sheet1')
    return


# 切换sheet页面
def set_sheet(name):
    global sheet
    global wb
    # 通过sheet名字，切换sheet页面
    sheet = wb.get_sheet(name)
    return


# 写入指定单元格，保留原格式
def write(r, c, value):
    global workbook, sheet

    # 获取要写入的单元格
    def _getCell(sheet, r, c):
        """ HACK: Extract the internal xlwt cell representation. """
        # 获取行
        row = sheet._Worksheet__rows.get(r)
        if not row: return None

        # 获取单元格
        cell = row._Row__cells.get(c)
        return cell

    # 获取要写入的单元格
    cell = _getCell(sheet, r, c)
    # 写入值
    sheet.write(r, c, value)
    if cell:
        # 获取要写入的单元格
        ncell = _getCell(sheet, r, c)
        if ncell:
            # 设置写入后格式和写入前一样
            ncell.xf_idx = cell.xf_idx

    return


# 保存
def save_close():
    global wb
    global df
    # 保存复制后的文件
    wb.save(df)
    return
