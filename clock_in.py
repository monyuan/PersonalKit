"""
    安装模块 xlutils
    pip install xlutils

"""
# 写入Excel模块
import xlrd
from xlwt import Workbook
from xlutils.copy import copy
# 封装数据库
import pymysql
from DBUtils.PooledDB import PooledDB

# 配置数据连接信息
__config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "APTX4869",
    "database": "HrTable"
}

# 建立数据库连接池
POOL = PooledDB(
    pymysql, 5,  # 5为连接池里的最少连接数
    **__config,
    setsession=['SET AUTOCOMMIT = 1']  # 设置线程池是否打开自动更新的配置，0为False，1为True
)

# 表格配置信息
workbook = Workbook()  # 新建一个工作簿
# 表名称
book_name = 'clock_in.xls'
# sheet名称
sheet_name = '2019-05'
title = [["日期", "姓名", "上班时间", "下班时间", "工作时长"], ]


def get_data():
    """
    获取数据库信息，以字典的形式返回
    每一条数据是字典，所有数据是一个集合
    :return: dict
    """
    db = POOL.connection()
    # DictCursor,以字典形式返回数据
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = """
        SELECT t.data_time,u.user_name,t.check_in,t.check_out,TIMEDIFF(t.check_out,t.check_in) as time
        FROM userinfo u JOIN timeinfo t 
        ON u.unique_id = t.unique_id  
    """
    cursor.execute(sql)
    temp = cursor.fetchall()
    # print(temp)
    data = []
    # 把列表里的字典转换正包含值的列表
    for i in temp:
        i['time'] = str(i['time'])  # 把时间替换转换成字符串
        data.append(list(i.values()))  # i.values() 取字典里的v
    print(data)
    return data


def create_xls(path, sheet_name, value):
    """
    创建Excel表
    :param path:  表文件名称
    :param sheet_name:  表格名称
    :param value: 表头
    """
    index = len(value)  # 获取需要写入数据的行数
    # workbook = Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("打卡信息表创建成功！")


def write_xls_append(path, value):
    """
    数据追加的方式写入Excel表
    :param path:  写入的表文件名
    :param value: 写入的数据
    """
    # 获取需要写入数据的行数
    index = len(value)
    # 打开工作簿
    workbook = xlrd.open_workbook(path)
    # 获取工作簿中的所有表格
    sheets = workbook.sheet_names()
    # 获取工作簿中所有表格中的的第一个表格
    worksheet = workbook.sheet_by_name(sheets[0])
    # 获取表格中已存在的数据的行数
    rows_old = worksheet.nrows
    # 将xlrd对象拷贝转化为xlwt对象
    new_workbook = copy(workbook)
    # 获取转化后工作簿中的第一个表格
    new_worksheet = new_workbook.get_sheet(0)
    for i in range(0, index):
        for j in range(0, len(value[i])):
            # 追加写入数据，注意是从i+rows_old行开始写入
            new_worksheet.write(i + rows_old, j, value[i][j])
    # 保存工作簿
    new_workbook.save(path)
    print("Excel写入数据成功！！！")


if __name__ == '__main__':
    data = get_data()

    # 创建打卡信息表
    create_xls(book_name, sheet_name, title)
    write_xls_append(book_name, data)
