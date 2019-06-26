# coding:utf-8
# 添加一个新的店员之后需要添加的表结构
import datetime

import pymysql

host = '************'
port = ************
user = '************'
passwd = '************'
charset = '************'
db = '************'



dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = dbclient.cursor()


# 创建表
def add_time(add_date):
    sql = '''
        CREATE TABLE `%s` (
      `time_number` INT(20) DEFAULT NULL,
      `starttime` VARCHAR(20) DEFAULT NULL,
      `endtime` VARCHAR(20) DEFAULT NULL,
      `waiter` INT(20) DEFAULT NULL,
      `waiter_flag` INT(1) DEFAULT '1',
      `yuliu1` VARCHAR(20) DEFAULT NULL,
      `yuliu2` VARCHAR(20) DEFAULT NULL,
      `yuliu3` VARCHAR(20) DEFAULT NULL
    ) ENGINE=MYISAM DEFAULT CHARSET=utf8mb4;
    '''

    a = sql.replace('%s', add_date)

    try:
        cursor.execute(a)
        dbclient.commit()
        return 1
    except Exception as e:
        print e
        dbclient.rollback()
        return 0



# 插入数据
def insert_time(insert_date,yuangong):
    sql = '''
INSERT  INTO `%s`(`time_number`,`starttime`,`endtime`,`waiter`,`waiter_flag`,`yuliu1`,`yuliu2`,`yuliu3`) VALUES
(1,'9:00','9:30',yuangong,1,NULL,NULL,NULL),
(2,'9:30','10:00',yuangong,1,NULL,NULL,NULL),
(3,'10:00','10:30',yuangong,1,NULL,NULL,NULL),
(4,'10:30','11:00',yuangong,1,NULL,NULL,NULL),
(5,'11:00','11:30',yuangong,1,NULL,NULL,NULL),
(6,'11:30','12:00',yuangong,1,NULL,NULL,NULL),
(7,'12:00','12:30',yuangong,1,NULL,NULL,NULL),
(8,'12:30','13:00',yuangong,1,NULL,NULL,NULL),
(9,'13:00','13:30',yuangong,1,NULL,NULL,NULL),
(10,'13:30','14:00',yuangong,1,NULL,NULL,NULL),
(11,'14:00','14:30',yuangong,1,NULL,NULL,NULL),
(12,'14:30','15:00',yuangong,1,NULL,NULL,NULL),
(13,'15:00','15:30',yuangong,1,NULL,NULL,NULL),
(14,'15:30','16:00',yuangong,1,NULL,NULL,NULL),
(15,'16:00','16:30',yuangong,1,NULL,NULL,NULL),
(16,'16:30','17:00',yuangong,1,NULL,NULL,NULL),
(17,'17:00','17:30',yuangong,1,NULL,NULL,NULL),
(18,'17:30','18:00',yuangong,1,NULL,NULL,NULL),
(19,'18:00','18:30',yuangong,1,NULL,NULL,NULL),
(20,'18:30','19:00',yuangong,1,NULL,NULL,NULL);
'''

    a = sql.replace('%s', insert_date)
    print yuangong
    print type(yuangong)
    a = a.replace('yuangong', yuangong)
    print a
    try:
        cursor.execute(a)
        dbclient.commit()
        return 1
    except Exception as e:
        print e
        dbclient.rollback()
        return 0


# 删除表
def delete_time(delete_date):
    sql = "DROP TABLE `%s`;"
    data = (delete_date,)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
        return 1
    except Exception as e:
        print e
        dbclient.rollback()
        return 0


# 修改员工状态
def update_flag(update_date, yuangongid, time_number, flag):
    if flag == 0:
        sql = "UPDATE `%s` SET `waiter_flag` = 0 WHERE `waiter` = %d AND `time_number` = %d;"
    if flag == 1:
        sql = "UPDATE `%s` SET `waiter_flag` = 1 WHERE `waiter` = %d AND `time_number` = %d;"
    data = (update_date,yuangongid,time_number)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
        return 1
    except Exception as e:
        print e
        dbclient.rollback()
        return 0




