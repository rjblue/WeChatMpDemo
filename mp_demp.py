#!/usr/bin/python
# -*- coding: UTF-8 -*-
#微信公众号开发接口demo
#author:jianjian

from flask import Flask,request
import xml.etree.ElementTree as ET
import time
app = Flask(__name__)

#用于通过安全校验
@app.route('/wechat',methods=['GET'])
def check_token():
    echostr = request.args["echostr"]
    return echostr

#处理消息
@app.route('/wechat',methods=['POST'])
def recv_wechat():
    data =  request.stream.read()
    xml_rec=ET.fromstring(data)
    msg_to = xml_rec.find('ToUserName').text
    msg_from = xml_rec.find('FromUserName').text
    content = xml_rec.find('Content').text
    print msg_from,msg_to,content
    return send(msg_from, msg_to,u'你好,我收到了你的消息:%s' % content)

#发送消息
def send(toname, fromname, content):
    reply = """
    <xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        <FuncFlag>0</FuncFlag>
    </xml>
	"""
    resp_str = reply % (toname, fromname, int(time.time()), content)
    return resp_str

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
