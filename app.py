
# coding=utf-8
from flask import Flask, render_template, request,jsonify
import execute
import time
import threading
import jieba
"""
定义心跳检测函数
"""
def heartbeat():
    print (time.strftime('%Y-%m-%d %H:%M:%S - heartbeat', time.localtime(time.time())))
    timer = threading.Timer(60, heartbeat)
    timer.start()
# timer = threading.Timer(60, heartbeat)
# timer.start()


# app = Flask(__name__,static_url_path="/static")
#
# @app.route('/message', methods=['POST'])

#"""定义应答函数，用于获取输入信息并返回相应的答案"""
def reply(text):
#从请求中获取参数信息
    # req_msg = request.form['msg']
    req_msg = text
#将语句使用结巴分词进行分词
    req_msg=" ".join(jieba.cut(req_msg))
    #调用decode_line对生成回答信息
    res_msg = execute.predict(req_msg)
    #将unk值的词用微笑符号袋贴
    res_msg = res_msg.replace('_UNK', '^_^')
    res_msg=res_msg.strip()
    
    # 如果接受到的内容为空，则给出相应的回复
    if res_msg == ' ':
      res_msg = '请与我聊聊天吧'

    return "人工智障：" + res_msg
    # return jsonify( { 'text': res_msg } )

# 启动APP
if (__name__ == "__main__"):
    #host = '0.0.0.0', port = 8808
    # app.run()
    print("LemonBot-一款真正人性化的五毛钱智障")
    while True :
        text = input("Sa：")
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print(reply(text))
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


