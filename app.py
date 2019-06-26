# coding:utf-8
import datetime
import hashlib
import os
import sys
from flask import Flask, request, make_response, render_template, jsonify, session, redirect, url_for
from urllib2 import Request as R
from urllib2 import urlopen as U
import json

from werkzeug.utils import secure_filename

from tools import *

appID = "************"
AppSecret = "************"
index_url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx************redirect_uri=************\index&response_type=code&scope=snsapi_userinfo&state=1&connect_redirect=1#wechat_redirect"
list_url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx************&redirect_uri=************\list&response_type=code&scope=snsapi_userinfo&state=1&connect_redirect=1#wechat_redirect"
url_code = "https://api.weixin.qq.com/sns/oauth2/access_token?appid={appid}&secret={appsecret}&code={code}&grant_type=authorization_code"
url_retoken = "https://api.weixin.qq.com/sns/oauth2/refresh_token?appid={appid}&grant_type=refresh_token&refresh_token={refresh_token}"
url_info = "https://api.weixin.qq.com/sns/userinfo?access_token={access_token}&openid={openid}&lang=zh_CN"

# host = 'localhost'
host = '************'
port = ************
user = '************'
passwd = '************'
charset = '************'
db = '************'
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources=r'/*')
app.config['SECRET_KEY'] = os.urandom(24)




# TODO 读取静态文件
# @app.route('/<path>')
# def today(path):
# #     if path == "MP_verify_b7PdLm4fs8SjR4wN.txt":
#         base_dir = os.path.dirname(__file__)
#         resp = make_response(open(os.path.join(base_dir, path)).read())
#         resp.headers["Content-type"]="application/json;charset=UTF-8"
#         return resp


@app.route('/index', methods=('GET', 'POST'))
def index():
    openid1 = session.get('openid')
    print session
    for k, v in session.items():
        print k, v
    if openid1 != None:
        session['openid'] = openid1
    code = request.values.get('code')
    if code:
        accessToken = R(url_code.format(appid=appID, appsecret=AppSecret, code=code))
        res_data = U(accessToken)
        print res_data
        res = res_data.read().decode('utf8')
        # res = res_data.read()
        print res
        res_json = json.loads(res)  # 转成json
        access_token = res_json["access_token"]
        refresh_token = res_json["refresh_token"]
        openid = res_json["openid"].strip()
        print openid
        if openid != None:
            session['openid'] = openid
        print session.get('openid')
        resp = render_template('index.html')
        resp = make_response(resp)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    resp = render_template('index.html')
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



@app.route('/list', methods=('GET', 'POST'))
def list1():
    # dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    # cursor = dbclient.cursor()
    openid2 = session.get('openid')
    if openid2 != None:
        session['openid'] = openid2
    code = request.values.get('code')
    if code:
        accessToken = R(url_code.format(appid=appID, appsecret=AppSecret, code=code))
        res_data = U(accessToken)
        res = res_data.read().decode('utf8')
        # res = res_data.read()
        res_json = json.loads(res)  # 转成json
        access_token = res_json["access_token"]
        refresh_token = res_json["refresh_token"]
        openid = res_json["openid"].strip()
        session['openid'] = openid

        print session.get('openid')
        resp = render_template('list.html')
        resp = make_response(resp)

        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    resp = render_template('list.html')
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# 查询所有订单
@app.route('/allorders', methods=('GET', 'POST'))
def search_order():
    openid3 = session.get('openid')
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    sql = "SELECT * FROM orders WHERE order_user = '%s' ORDER BY `order_date`,`order_time`"
    data = (openid3,)
    cursor.execute(sql % data)
    orders = cursor.fetchall()
    a = []
    for aorder in orders:
        b = {}

        sql = "SELECT activity_project FROM projects WHERE project_id = %d"
        data = (aorder[4],)
        cursor.execute(sql % data)
        order_project = cursor.fetchall()[0]

        sql = "SELECT * FROM dianpu WHERE dianpu_id = %d"
        data = (aorder[11],)
        cursor.execute(sql % data)
        dianpu_info = cursor.fetchall()

        sql = "SELECT activity_price,activity_img FROM activities WHERE activity_name = '%s'"
        data = (aorder[3],)
        cursor.execute(sql % data)
        order_price = cursor.fetchall()[0]

        b['order_username'] = aorder[0]
        b['order_phone'] = aorder[1]
        b['order_waiter'] = aorder[2]
        b['order_activity'] = aorder[3]
        b['order_acttype'] = aorder[4]
        b['order_liuyan'] = aorder[5]
        b['order_id'] = aorder[6]
        b['order_project'] = order_project
        b['order_price'] = order_price[0]
        b['order_date'] = aorder[7]
        b['order_user'] = aorder[8]
        b['order_time'] = aorder[9]
        b['order_timenum'] = aorder[10]
        b['order_flag'] = aorder[12]
        b['order_shopid'] = dianpu_info
        b['order_img'] = order_price[1]
        a.append(b)

    res = json.dumps(a, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res



@app.route('/des', methods=('GET', 'POST'))
def des():
    return render_template('des.html')


@app.route('/class', methods=('GET', 'POST'))
def class1():
    proid = request.values.get('procid')
    print proid
    res = render_template('class.html', proid=proid)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res




# TODO 获取微信服务号code
@app.route('/codeinfo')
def getCode():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    code = request.args.get('code')
    if code:
        accessToken = R(url_code.format(appid=appID, appsecret=AppSecret, code=code))
        res_data = U(accessToken)
        res = res_data.read().decode('utf8')
        # res = res_data.read()
        res_json = json.loads(res)  # 转成json
        access_token = res_json["access_token"]
        refresh_token = res_json["refresh_token"]
        openid1 = res_json["openid"].strip()
        sql = "INSERT INTO weixinuser (openid) VALUES ('%s')"
        data = (openid1)
        cursor.execute(sql % data)
        cursor.commit()
        return render_template('index.html')

    print 0
    return "0"


# TODO 选取产品类型界面
@app.route('/protychos', methods=('POST', 'GET'))
def protychos():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    sql = "SELECT * from projects"
    cursor.execute(sql)
    s = cursor.fetchall()
    contents = []
    for content in s:
        contents.append(content)
    print type(contents)
    sql1 = "SELECT MAX(activity_price) FROM activities WHERE activity_project = %d"
    sql2 = "SELECT MIN(activity_price) FROM activities WHERE activity_project = %d"
    a = {}
    for content in contents:
        b = {}
        data = (content[2],)
        cursor.execute(sql1 % data)
        max_price = cursor.fetchall()[0][0]
        cursor.execute(sql2 % data)
        min_price = cursor.fetchall()[0][0]
        b['max_price'] = max_price
        b['min_price'] = min_price
        b['content'] = content[1]
        b['procid'] = content[2]
        b['aimg'] = content[3]
        a[content[0]] = b
    dbclient.commit()

    res = json.dumps(a, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 后台页面返回所有品牌的格式
@app.route('/prolist', methods=('POST', 'GET'))
def prolist():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    sql = "SELECT * from projects"
    cursor.execute(sql)
    s = cursor.fetchall()
    contents = []
    for content in s:
        contents.append(content)
    sql1 = "SELECT MAX(activity_price) FROM activities WHERE activity_project = %d"
    sql2 = "SELECT MIN(activity_price) FROM activities WHERE activity_project = %d"
    a = []
    for content in contents:
        b = {}
        data = (content[2],)
        cursor.execute(sql1 % data)
        max_price = cursor.fetchall()[0][0]
        cursor.execute(sql2 % data)
        min_price = cursor.fetchall()[0][0]
        b['proname'] = content[0]
        b['max_price'] = max_price
        b['min_price'] = min_price
        b['content'] = content[1]
        b['procid'] = content[2]
        b['aimg'] = content[3]
        a.append(b)
    # for content in contents:
    dbclient.commit()

    res = json.dumps(a, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 护理类型选择界面
@app.route('/projechos', methods=('POST', 'GET'))
def projechos():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    project_id = request.values.get('proid')
    sql = "SELECT * from activities WHERE activity_project = '%d'"
    data = (int(project_id),)
    cursor.execute(sql % data)
    contents = cursor.fetchall()
    dbclient.commit()
    b = []
    for content in contents:
        a = {}
        a['an'] = content[0]
        a['ap'] = content[1]
        a['aif'] = content[2]
        a['apro'] = content[3]
        a['aphone'] = content[4]
        a['aprice'] = content[5]
        a['aid'] = content[6]

        b.append(a)
    res = json.dumps(b, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


#TODO 返回所有护理产品
@app.route('/allact', methods=('GET','POST'))
def allact():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()

    sql = "SELECT activity_name,activity_place,activity_content,activity_project,activity_phone,activity_price,activity_id,activity_time,activity_img FROM activities"
    cursor.execute(sql)
    contents = cursor.fetchall()
    b = []
    for content in contents:
        a = {}
        sql = 'SELECT `activity_project` FROM projects WHERE project_id = %d'
        data = (content[3],)
        cursor.execute(sql % data)
        proname = cursor.fetchone()[0]
        a['an'] = content[0]
        a['ap'] = content[1]
        a['aif'] = content[2]
        a['aproid'] = content[3]
        a['aproname'] = proname
        a['aphone'] = content[4]
        a['aprice'] = content[5]
        a['aid'] = content[6]
        a['atime'] = content[7]
        a['aimg'] = content[8]
        b.append(a)
    res = json.dumps(b, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res



# TODO 护理产品详情预约界面
@app.route('/actinfo', methods=('POST', 'GET'))
def actinfo():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    activity_id = request.values.get('actid')
    dianpu_id = 1


    sql = "SELECT * from dianpu"
    cursor.execute(sql)
    dianpus = cursor.fetchall()
    dianpus_list = []
    dianyuans_list = []
    for dianpu in dianpus:
        dianpus_dict = {}
        dianpus_dict['dianpu_id'] = dianpu[0]
        dianpus_dict['dianpu_name'] = dianpu[1]
        dianpus_dict['dianpu_place'] = dianpu[2]
        dianpus_dict['dianpu_phone'] = dianpu[3]
        dianpus_list.append(dianpus_dict)

    sql = "SELECT * FROM dianyuan WHERE dianyuan_dianpu = %d"
    data = (dianpu_id,)
    cursor.execute(sql % data)
    dianyuans = cursor.fetchall()
    for dianyuan in dianyuans:
        dianyuans_dict = {}
        dianyuans_dict['dianyuan_name'] = dianyuan[0]
        dianyuans_dict['dianyuan_phone'] = dianyuan[1]
        dianyuans_dict['dianyuan_id'] = dianyuan[2]
        dianyuans_dict['dianyuan_dianpu'] = dianyuan[3]
        dianyuans_list.append(dianyuans_dict)


        # 通过店铺id获得店员们并返回
        # sql = "SELECT * FROM dianyuan WHERE dianyuan_dianpu = %d"
        # data = (dianpu[0],)
        # cursor.execute(sql % data)
        # dianyuans = cursor.fetchall()
        # b = {}
        # c = []
        # for dianyuan in dianyuans:
        #     dianyuans_dict = {}
        #     dianyuans_dict['dianyuan_name'] = dianyuan[0]
        #     dianyuans_dict['dianyuan_phone'] = dianyuan[1]
        #     dianyuans_dict['dianyuan_id'] = dianyuan[2]
        #     c.append(dianyuans_dict)
        # b[dianpu[0]]=(c)
        # dianyuans_list.append(b)


    sql = "SELECT * from activities WHERE activity_id = '%d'"
    data = (int(activity_id),)
    cursor.execute(sql % data)
    content = cursor.fetchone()
    print content

    # 返回所有起始时间
    # sql = "SELECT starttime FROM halfhour"
    # cursor.execute(sql)
    # userful_times = []
    # s = cursor.fetchall()
    # for i in s:
    #     userful_times.append(i)

    return_content = {}
    sql = "SELECT activity_project FROM projects WHERE project_id = '%d'"
    data = (int(content[3]))
    cursor.execute(sql % data)
    project_name = cursor.fetchone()[0]
    sql = "select order_username,order_phone FROM orders WHERE order_user = '%s' ORDER BY order_id DESC  LIMIT 0,1;"
    openid = session.get('openid')
    # openid = "oC0Lm1OJm_hhFH-NbC4gLBLzoTEY"
    data = (openid,)
    cursor.execute(sql % data)
    dangqianuser = cursor.fetchone()
    if dangqianuser == None:
        dangqianuser = (u"", u"")
    return_content['shops'] = dianpus_list
    return_content['waiters'] = dianyuans_list
    # TODO 需要查询品牌对应的名字
    return_content['pname'] = content[0]
    return_content['pid'] = activity_id
    return_content['pplace'] = content[1]
    return_content['pinfo'] = content[2]
    return_content['protype_name'] = project_name
    return_content['protype_id'] = content[3]
    return_content['pphone'] = content[4]
    return_content['pprice'] = content[5]
    return_content['proid'] = content[6]
    return_content['ptime'] = content[7]
    return_content['dquser'] = dangqianuser
    # return_content['use_times'] = userful_times
    res = json.dumps(return_content, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 选取店铺后传回店员们
@app.route('/sptwt', methods=('GET','POST'))
def shop_to_waiters():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    dianpu_id = int(request.values.get('shopid'))
    sql = "SELECT * FROM dianyuan WHERE dianyuan_dianpu = %d"
    data = (dianpu_id,)
    cursor.execute(sql % data)
    dianyuans = cursor.fetchall()
    dianyuans_list = []

    for dianyuan in dianyuans:
        dianyuans_dict = {}
        dianyuans_dict['dianyuan_name'] = dianyuan[0]
        dianyuans_dict['dianyuan_phone'] = dianyuan[1]
        dianyuans_dict['dianyuan_id'] = dianyuan[2]
        dianyuans_list.append(dianyuans_dict)
    res = json.dumps(dianyuans_list, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 预约请求处理
@app.route('/order_send', methods=('POST', 'GET'))
def order_send():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    now_time_number = None
    shopid = int(request.values.get('shopid'))
    try:
        waiter = int(request.values.get('waiter'))
    except TypeError:
        waiter = 0
    order_date = request.values.get('order_date').replace('-', '')
    # activity_type = request.values.get('activity_type')
    activity_time = request.values.get('ptime')
    activity_time = int(activity_time)
    print activity_time
    print type(activity_time)
    shijianduans = activity_time / 30
    if activity_time % 30 != 0:
        shijianduans += 1

    # 寻找当前时间
    now_time = datetime.datetime.now()
    now_date = now_time.strftime("%Y%m%d")
    is_today = False
    sql = "SELECT table_name FROM information_schema.TABLES WHERE table_name = '%s';"
    data = (order_date,)
    cursor.execute(sql % data)
    c = cursor.fetchall()
    print len(c)
    if len(c) == 0:
        sql = "SELECT dianyuan_id FROM dianyuan;"
        cursor.execute(sql)
        dianyuans = cursor.fetchall()
        add_time(order_date)
        for dianyuan in dianyuans:
            insert_time(order_date,str(dianyuan[0]))
    if int(order_date) == int(now_date):
        is_today = True

    now_h = int(now_time.strftime("%H"))
    now_m = int(now_time.strftime("%M"))
    if waiter == 0:
        sql = "SELECT dianyuan_id FROM dianyuan WHERE dianyuan_dianpu = %d"
        data = (shopid,)
        cursor.execute(sql % data)
        dianyuans = cursor.fetchall()
        v = []
        for dianyuan in dianyuans:
            v.append(dianyuan[0])

    else:
        beg = waiter
        end = waiter + 1
        v = [waiter, waiter + 1]
    use_times = {}
    for i in v:
        sql = "SELECT time_number,starttime,waiter_flag FROM `%s` WHERE waiter = %d"
        data = (order_date, i)
        cursor.execute(sql % data)
        contents = cursor.fetchall()
        print contents
        time_length = len(contents)
        if time_length == 0:
            res = json.dumps([{'404':'没有可预约的时间'}], ensure_ascii=False)
            res = make_response(res)
            res.headers['Access-Control-Allow-Origin'] = '*'
            return res
        print 'time_length', time_length
        if is_today:
            for content in contents:
                h = int(content[1].split(':')[0].strip())
                m = int(content[1].split(':')[1].strip())

                if h == now_h and now_m < 30:
                    if m == 30:
                        now_time_number = int(content[0])
                    else:
                        now_time_number = int(content[0]) + 1
                    break

                if h == now_h and now_m >= 30:
                    if m == 30:
                        now_time_number = content[0] + 1
                    else:
                        now_time_number = content[0] + 2
                    break

        else:
            now_time_number = 1



        # TODO 需要完善的时间段选择问题
        if now_time_number > (time_length + 1 -shijianduans):
            res = json.dumps([{'404': '没有可预约的时间'}], ensure_ascii=False)
            res = make_response(res)
            res.headers['Access-Control-Allow-Origin'] = '*'
            return res
        for j in range(now_time_number, time_length):
            sql = "SELECT waiter_flag,starttime FROM `%s` WHERE waiter = %d limit %d,%d"
            data = (order_date, i, j-1, shijianduans)
            cursor.execute(sql % data)
            contents = cursor.fetchall()
            if len(contents) != shijianduans:
                break
            for content in contents:
                if content[0] == 0:
                    break
            use_times[j + 1] = [contents[0][1],i]




    if len(use_times) == 0:
        res = json.dumps([{'404': '没有可预约的时间'}], ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    res = json.dumps([use_times], ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 处理订单
# 服务：头部护理 30min  1
#      身体护理 50min  2
#      全身护理 60min  3
@app.route('/orprces', methods=('POST', 'GET'))
def order_process():
    openid = session.get('openid').encode('utf-8')
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    order_username = request.values.get('order_username').encode('utf-8')
    order_phone = request.values.get('order_phone').encode('utf-8')
    order_waiter = int(request.values.get('order_waiter'))
    order_activity = request.values.get('order_activity').encode('utf-8')
    order_acttype = int(request.values.get('order_acttype'))
    order_liuyan = request.values.get('order_liuyan').encode('utf-8')
    order_odate = request.values.get('o_date').encode('utf-8')
    order_otime = request.values.get('o_time').encode('utf-8')
    order_otime_num = int(request.values.get('o_timenum'))

    order_shopid = int(request.values.get('shopId'))
    order_user = openid

    a = {}
    try:

        sql = "INSERT INTO orders (order_username,order_phone,order_waiter,order_activity,order_acttype,order_liuyan,order_date,order_user,order_time,order_timenum,order_dianpu) VALUES ('%s','%s',%d,'%s',%d,'%s','%s','%s','%s',%d,%d);"
        # sql = "INSERT INTO orders (order_username) VALUES (order_username);"
        #
        # data = ()
        data = (
            order_username, order_phone, order_waiter, order_activity, order_acttype, order_liuyan, order_odate,
            order_user,
            order_otime, order_otime_num, order_shopid)
        cursor.execute(sql % data)
        dbclient.commit()
        # cursor.execute(sql)

    except Exception as e:
        print e
        a['code'] = 400

    sql = "SELECT activity_time FROM activities WHERE activity_name = '%s'"
    data = (order_activity,)
    cursor.execute(sql % data)
    a_time = int(cursor.fetchall()[0][0])
    times = a_time / 30
    if a_time % 30 != 0:
        times += 1
    for i in range(0, times):
        update_flag(order_odate.replace('-', ''), order_waiter, order_otime_num + i,0)
    res = json.dumps(a, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 自己写的登陆装饰器
def is_login(func):
    def inner(*args,**kwargs):
        if not session.get("user"):
            return redirect("/login")
        else:
            return func(*args,**kwargs)
    return inner


# TODO 登陆
@app.route('/login',methods=('POST','GET'))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        cursor = dbclient.cursor()
        username = request.values.get('username')
        password = request.values.get('password')
        new_passwd = hashlib.md5(password).hexdigest()
        sql = "SELECT id,dianpu,password FROM adminuser WHERE username = '%s'"
        data = (username,)
        cursor.execute(sql % data)

        login_user = cursor.fetchall()[0]

        user_id = login_user[0]
        user_dianpu = login_user[1]
        old_passwd = login_user[2]

        if new_passwd == old_passwd:
            session['shopid'] = user_dianpu
            session['login_user'] = user_id
            res = json.dumps({'code': 200,'msg': '登陆成功','user_id':user_id,'shop':user_dianpu}, ensure_ascii=False)
            res = make_response(res)
            res.headers['Access-Control-Allow-Origin'] = '*'
            return res
            # return redirect('/shop1')
        else:
            res = json.dumps({'code': 400,'msg': '用户名或密码错误'}, ensure_ascii=False)
            res = make_response(res)
            res.headers['Access-Control-Allow-Origin'] = '*'
            return res



# TODO 注册
@app.route('/register')
def register():
    pass


# TODO 查询当前店铺下所有订单
@app.route('/shopallorders', methods=('GET','POST'))
def shopallorders():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    shopid = int(request.values.get('shopid'))
    sql = "SELECT `order_username`,`order_phone`,`order_waiter`,`order_activity`,`order_acttype`,`order_liuyan`,`order_id`,`order_date`,`order_user`,`order_time`,`order_timenum`,`order_dianpu`,`order_flag`,`is_callback`,`order_comment` FROM `orders` WHERE `order_dianpu` = %d"

    if 'orderby' in request.values:
        orderby = int(request.values.get('orderby'))
        if orderby == 1:
            sql = "SELECT `order_username`,`order_phone`,`order_waiter`,`order_activity`,`order_acttype`,`order_liuyan`,`order_id`,`order_date`,`order_user`,`order_time`,`order_timenum`,`order_dianpu`,`order_flag`,`is_callback`,`order_comment` FROM `orders` WHERE `order_dianpu` = %d ORDER BY `order_date`,`order_time`"
        if orderby == 0:
            sql = "SELECT `order_username`,`order_phone`,`order_waiter`,`order_activity`,`order_acttype`,`order_liuyan`,`order_id`,`order_date`,`order_user`,`order_time`,`order_timenum`,`order_dianpu`,`order_flag`,`is_callback`,`order_comment` FROM `orders` WHERE `order_dianpu` = %d ORDER BY `order_date` DESC,`order_time` DESC"

    data = (shopid,)
    cursor.execute(sql % data)
    allorders = cursor.fetchall()
    contents = []
    for order in allorders:
        content = {}
        sql = "SELECT `activity_project` FROM projects WHERE project_id = %d"
        data = (order[4],)
        cursor.execute(sql % data)
        acttypename = cursor.fetchone()[0]

        sql = "SELECT `dianyuan_name` FROM dianyuan WHERE dianyuan_id = %d"
        data = (order[2],)
        cursor.execute(sql % data)
        waiter_name = cursor.fetchone()[0]

        content['order_username'] = order[0]
        content['order_phone'] = order[1]
        content['order_waiterid'] = order[2]
        content['order_waitername'] = waiter_name
        content['order_activity'] = order[3]
        content['order_acttype'] = order[4]
        content['order_actname'] = acttypename
        content['order_order_liuyan'] = order[5]
        content['order_id'] = order[6]
        content['order_order_date'] = order[7]
        content['order_user'] = order[8]
        content['order_time'] = order[9]
        content['order_timenum'] = order[10]
        content['order_dianpu'] = order[11]
        content['order_flag'] = order[12]
        content['order_iscallback'] = order[13]
        content['order_comment'] = order[14]
        contents.append(content)
    res = json.dumps(contents,ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res



# TODO 将订单状态置为已完成
@app.route('/isfinish',methods=('GET','POST'))
def order_is_finish():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    order_id = int(request.values.get('order_id'))
    sql = "UPDATE orders SET order_flag = 1 WHERE order_id = %d"
    data = (order_id,)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
        res = json.dumps({'code':'200','msg':'修改成功'}, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    except Exception as e:
        print e
        dbclient.rollback()
        res = json.dumps({'code': '400', 'msg': '修改失败'}, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res


# TODO 将订单状态置为未完成
@app.route('/isnotfinish',methods=('GET', 'POST'))
def order_is_not_finish():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    order_id = int(request.values.get('order_id'))
    sql = "UPDATE orders SET order_flag = 0 WHERE order_id = %d"
    data = (order_id,)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
        res = json.dumps({'code':'200','msg':'修改成功'}, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    except Exception as e:
        print e
        dbclient.rollback()
        res = json.dumps({'code': '400', 'msg': '修改失败'}, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res


# TODO 将订单设置为已回访状态
@app.route('/iscallback', methods=('GET','POST'))
def iscallback():
    order_id = int(request.values.get('order_id'))
    sql = "UPDATE orders SET is_callback = 1 WHERE order_id = %d"
    data = (order_id,)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
        res = json.dumps({'code': '200', 'msg': '修改成功'}, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    except Exception as e:
        print e
        dbclient.rollback()
        res = json.dumps({'code': '400', 'msg': '修改失败'}, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res


# TODO 将订单设置为未回访状态
@app.route('/isnotcallback', methods=('GET','POST'))
def isnotcallback():
    order_id = int(request.values.get('order_id'))
    sql = "UPDATE orders SET is_callback = 0 WHERE order_id = %d"
    data = (order_id,)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
        res = json.dumps({'code': '200', 'msg': '修改成功'}, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    except Exception as e:
        print e
        dbclient.rollback()
        res = json.dumps({'code': '400', 'msg': '修改失败'}, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res


# TODO 订单回访内容修改
@app.route('/update_comment', methods=('GET','POST'))
def update_order_comment():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    order_id = int(request.values.get('order_id'))
    order_comment = request.values.get('order_comment')
    sql = "UPDATE `orders` SET `order_comment` = '%s' WHERE `order_id` = %d "
    data = (order_comment,order_id)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
        res = json.dumps({
            'code': 200,
            'msg': '修改成功'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res

    except Exception as e:
        print e
        dbclient.rollback()
        res = json.dumps({
            'code': 400,
            'msg': '修改失败'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res





# TODO 店员相关操作

# TODO 新创建一个店员
@app.route('/add_person',methods=('GET', 'POST'))
def add_waiter():
    """
    :param person_name:店员名字 person_phone:店员电话 person_shop:店员所属店铺 person_date:店员上班日期
    :return:
    """
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    waiter_name = request.values.get('person_name')
    waiter_phone = request.values.get('person_phone')
    waiter_dianpu = request.values.get('person_shop')
    waiter_date = request.values.get('person_date')
    try:
        sql = "INSERT INTO dianyuan (dianyuan_name,dianyuan_phone,dianyuan_dianpu) VALUES ('%s','%s',%d)"
        data = (waiter_name, waiter_phone,waiter_dianpu)
        cursor.execute(sql % data)
        dbclient.commit()

        res = json.dumps({
            'code':200,
            'msg':'修改成功'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    except Exception as e:
        print e
        dbclient.rollback()
        res = json.dumps({
            'code':400,
            'msg':'修改失败'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res


# TODO 店员请假
@app.route('/dianyuan_rest', methods=('GET', 'POST'))
def dianyuan_rest():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    dianyuan_id = request.values.get('dianyuan_id')
    rest_date = request.values.get('rest_date')
    rest_days = request.values.get('rest_days')




# 允许上传图片的类型
def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp','jpeg','JPEG'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


from pypinyin import lazy_pinyin

# TODO 新建一个产品品牌
@app.route("/newpro",methods=('GET', 'POST'))
def new_pro():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    pro_name = request.values.get('pro_name')
    pro_info = request.values.get('pro_info')
    try:
        f_img = request.files['file']
        if not (f_img and allowed_file(f_img.filename)):
            return json.dumps({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、jpg、bmp、jpeg"}, ensure_ascii=False)
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, '/static/img/' + secure_filename(''.join(lazy_pinyin(f_img.filename))))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f_img.save(upload_path)
        sql = "INSERT INTO projects (activity_project,project_info,project_img) VALUES ('%s','%s','%s')"
        data = (pro_name, pro_info, '/static/img/' + secure_filename(''.join(lazy_pinyin(f_img.filename))))
    except Exception as e:
        print e
        # print pro_name.encode('utf8')
        # print pro_info.encode('utf8')
        sql = "INSERT INTO projects (activity_project,project_info) VALUES ('%s','%s')"
        data = (pro_name, pro_info)
        # res = json.dumps({
        #     'proname': pro_name,
        #     'proinfo': pro_info
        # }, ensure_ascii=False)
        # res = make_response(res)
        # res.headers['Access-Control-Allow-Origin'] = '*'
        # return res

    try:
        cursor.execute(sql % data)
        dbclient.commit()
        res = json.dumps({
            'code': 200,
            'msg': '添加成功'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    except Exception as e:
        print sql
        print data
        print '数据库语句错误w'
        print e
        dbclient.rollback()
        res = json.dumps({
            'code': 400,
            'msg': '添加失败'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res



# TODO 上传图片
@app.route('/uploadimg', methods=('GET','POST'))
def uploadimg():
    if request.method == "GET":
        return render_template('uploadimg.html')
    if request.method == 'POST':
        f_img = request.files['pro_img']

        if not (f_img and allowed_file(f_img.filename)):
            return json.dumps({"code": 1001, "msg": "请检查上传的图片类型，仅限于png、jpg、bmp、jpeg"}, ensure_ascii=False)
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, '/static/img/', secure_filename(''.join(lazy_pinyin(f_img.filename))))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        # upload_path = os.path.join(basepath, 'static/img', secure_filename(f_img.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f_img.save(upload_path)
        return json.dumps({"code": 200, "msg": "上传成功"}, ensure_ascii=False)


# TODO 返回所有产品类型
@app.route('/allpro',methods=('GET', 'POST'))
def all_pro():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    sql = "SELECT activity_project,project_id FROM projects"
    cursor.execute(sql)
    projects_t = cursor.fetchall()
    b = []
    for project in projects_t:
        a = {}
        a['project_name'] = project[0]
        a['project_id'] = project[1]
        b.append(a)
    res = json.dumps(b, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 新建一个活动
@app.route('/newact',methods=('GET', 'POST'))
def new_act():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    activity_project = int(request.values.get('pro_id'))
    activity_name = request.values.get('act_name')
    activity_content = request.values.get('act_content')
    activity_price = int(request.values.get('act_price'))
    activity_time = request.values.get('act_time')
    try:
        activity_img = request.files['file']
        if not (activity_img and allowed_file(activity_img.filename)):
            return json.dumps({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、jpg、bmp、jpeg"}, ensure_ascii=False)
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, '/static/img/',
                                   secure_filename(
                                       ''.join(lazy_pinyin(activity_img.filename))))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        activity_img.save(upload_path)
        sql = "INSERT INTO activities " \
              "(activity_name,activity_content,activity_project,activity_price,activity_time,activity_img)" \
              "VALUES " \
              "('%s','%s',%d,%d,'%s','%s')"
        data = (activity_name, activity_content, activity_project, activity_price, activity_time,
                '/static/img/' + secure_filename(''.join(lazy_pinyin(activity_img.filename))))
    except Exception as e:
        print e
        sql = "INSERT INTO activities " \
              "(activity_name,activity_content,activity_project,activity_price,activity_time)" \
              "VALUES " \
              "('%s','%s',%d,%d,'%s')"
        data = (activity_name, activity_content, activity_project, activity_price, activity_time)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
        res = json.dumps({
            'code': 200,
            'msg': '添加成功'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    except Exception as e:
        print e
        dbclient.rollback()
        res = json.dumps({
            'code': 400,
            'msg': '添加失败'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res

#TODO 店铺相关操作


# TODO 新建一个店铺
@app.route('/addshop', methods=('GET', 'POST'))
def addshop():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    dp_name = request.values.get('dp_name')
    dp_phone = request.values.get('dp_phone')
    dp_place = request.values.get('dp_place')

    # TODO店铺上传的图片 （需要时再释放）
    # dp_img = request.files['dp_img']
    #
    # if not (dp_img and allowed_file(dp_img.filename)):
    #     return json.dumps({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、jpg、bmp、jpeg"}, ensure_ascii=False)
    # basepath = os.path.dirname(__file__)
    # upload_path = os.path.join(basepath, 'static/img',
    #                            secure_filename(
    #                                ''.join(lazy_pinyin(dp_img.filename))))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
    # dp_img.save(upload_path)

    sql = "INSERT INTO dianpu " \
          "(dianpu_name,dianpu_place,dianpu_phone)" \
          "VALUES " \
          "('%s','%s','%s')"
    data = (dp_name, dp_place, dp_phone)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
        res = json.dumps({
            'code': 200,
            'msg': '添加成功'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    except Exception as e:
        print e
        dbclient.rollback()
        res = json.dumps({
            'code': 400,
            'msg': '添加失败'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res


# TODO 返回所有店铺
@app.route('/allshop')
def allshop():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    sql = "SELECT * FROM dianpu"
    cursor.execute(sql)
    contents = cursor.fetchall()
    # print contents
    a = []
    for content in contents:
        b = {}
        b['dp_id'] = content[0]
        b['dp_name'] = content[1]
        b['dp_place'] = content[2]
        b['dp_phone'] = content[3]
        a.append(b)
    res = json.dumps(a, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 删除店铺
@app.route('/delshop', methods=('GET','POST'))
def delshop():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    shopid = request.values.get('shopid')
    sql = "DELETE  FROM dianpu WHERE dianpu_id = %d"
    data = (shopid,)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
        res = json.dumps({
            'code': 200,
            'msg': '删除成功'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    except Exception as e:
        print e
        dbclient.rollback()
        res = json.dumps({
            'code': 400,
            'msg': '删除失败'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res




# TODO 订单的相关修改
# TODO 删除订单
@app.route('/delorder',methods=('GET', 'POST'))
def delete_order():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    order_id = int(request.values.get('order_id'))
    sql = "SELECT order_waiter,order_time,order_timenum,order_activity,order_date FROM orders WHERE order_id = %d"
    data = (order_id,)
    cursor.execute(sql % data)
    order_content = cursor.fetchone()
    order_waiter = order_content[0]
    order_time = order_content[1].replace(':',"")
    order_timenum = order_content[2]
    order_activity = order_content[3]
    order_date = order_content[4].replace('-', '')

    order_datetime = order_date+order_time
    order_datetime = datetime.datetime.strptime(order_datetime, '%Y%m%d%H%M')
    now_datetime = datetime.datetime.now()

    if now_datetime >= order_datetime:
        sql = "DELETE FROM orders WHERE order_id = '%s'"
        data = (order_id,)
        try:
            cursor.execute(sql % data)
            dbclient.commit()
            res = json.dumps({
                'code': 200,
                'msg': '删除成功'
            }, ensure_ascii=False)
            res = make_response(res)
            res.headers['Access-Control-Allow-Origin'] = '*'
            return res
        except Exception as e:
            print e
            dbclient.rollback()
            res = json.dumps({
                'code': 400,
                'msg': '删除失败'
            }, ensure_ascii=False)
            res = make_response(res)
            res.headers['Access-Control-Allow-Origin'] = '*'
            return res

    sql = "DELETE FROM orders WHERE order_id = '%s'"
    data = (order_id,)
    try:
        cursor.execute(sql % data)
        dbclient.commit()
    except Exception as e:
        print e
        dbclient.rollback()
        res = json.dumps({
            'code': 400,
            'msg': '删除失败，未找到订单'
        }, ensure_ascii=False)
        res = make_response(res)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    sql = "SELECT activity_time FROM activities WHERE activity_name = '%s'"
    data = (order_activity,)
    cursor.execute(sql % data)
    activity = int(cursor.fetchone()[0])
    times = activity / 30
    if times % 30 != 0:
        times += 1
    for i in range(0, times):
        update_flag(order_date,order_waiter,order_timenum,1)
    res = json.dumps({
        'code': 200,
        'msg': '删除成功'
    }, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 所有用户所有店铺的订单
@app.route('/alluserorders')
def alluserorders():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()
    sql = "SELECT * FROM orders"
    cursor.execute(sql)
    orders = cursor.fetchall()
    a = []
    for aorder in orders:
        b = {}
        sql = "SELECT activity_project FROM projects WHERE project_id = %d"
        data = (aorder[4],)
        cursor.execute(sql % data)
        order_project = cursor.fetchall()[0]

        sql = "SELECT * FROM dianpu WHERE dianpu_id = %d"
        data = (aorder[11],)
        cursor.execute(sql % data)
        dianpu_info = cursor.fetchall()

        sql = "SELECT activity_price,activity_img FROM activities WHERE activity_name = '%s'"
        data = (aorder[3],)
        cursor.execute(sql % data)
        order_price = cursor.fetchall()[0]

        b['order_username'] = aorder[0]
        b['order_phone'] = aorder[1]
        b['order_waiter'] = aorder[2]
        b['order_activity'] = aorder[3]
        b['order_acttype'] = aorder[4]
        b['order_liuyan'] = aorder[5]
        b['order_id'] = aorder[6]
        b['order_project'] = order_project
        b['order_price'] = order_price[0]
        b['order_date'] = aorder[7]
        b['order_user'] = aorder[8]
        b['order_time'] = aorder[9]
        b['order_timenum'] = aorder[10]
        b['order_shopid'] = dianpu_info
        b['order_img'] = order_price[1]
        a.append(b)

    res = json.dumps(a, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 查询单个订单的预约人信息
@app.route("/singleorderuser")
def singorder():
    order_id = int(request.values.get('order_id'))
    sql = "SELECT order_username,order_phone,order_waiter FROM orders WHERE order_id = %d"
    data = (order_id,)
    cursor.execute(sql % data)
    order_info = cursor.fetchone()
    order_info = list(order_info)
    res = json.dumps(order_info, ensure_ascii=False)
    res = make_response(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# TODO 更新订单信息
@app.route('/updateorder', methods=('GET', 'POST'))
def update_order():
    dbclient = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = dbclient.cursor()

    order_username = request.values.get('order_username').encode('utf-8')
    order_phone = request.values.get('order_phone').encode('utf-8')
    order_waiter = int(request.values.get('order_waiter'))
    order_date = request.values.get('order_date').encode('utf-8')
    order_time = request.values.get('order_time').encode('utf-8')
    order_timenum = int(request.values.get('order_timenum'))
    order_shopid = int(request.values.get('order_shopid'))



    # res = json.dumps(, ensure_ascii=False)
    # res = make_response(res)
    # res.headers['Access-Control-Allow-Origin'] = '*'
    # return res



if __name__ == '__main__':
    # reload(sys)  # 2
    # sys.setdefaultencoding('utf-8')
    app.run(host='0.0.0.0', port='5000', debug=True)
    # app.run(host='0.0.0.0', port='5000', debug=False)

