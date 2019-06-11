"""
    封装数据库连接池
"""
import pymysql  # 数据库连接
from DBUtils.PooledDB import PooledDB  # 用于数据库连接池

# 配置数据连接信息
__config = {
    "host": "ip_address",
    "port": 3306,
    "user": "root",
    "password": "password",
    "database": "db_name"
}

# 建立数据库连接池
POOL = PooledDB(
    pymysql, 5,  # 5为连接池里的最少连接数
    **__config,
    # 设置线程池是否打开自动更新的配置，0为False，1为True
    setsession=['SET AUTOCOMMIT = 1']  
)

if __name__ == '__main__':
    # 获取数据库连接
    db = POOL.connection()
    # 创建游标
    cursor = db.cursor()
    # 准备sql
    sql = ""
    # 执行sql
    cursor.execute(sql)
    # data = cursor.fetchall()
    data = cursor.fetchone()[0]
