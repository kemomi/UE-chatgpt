import os
import web
from flask import Flask, request
from ChatGPT.Official import Chatbot
from kemomi.handle import Handle
from sendwx.ue import epic 
from chatgptmain.ueChatgpt import ueChatpt
from chatgptmain.Chatgpt import Chatgptwx
import threading
app = Flask(__name__)

#这是微信接收到消息后向chatgpt发送信息的一个线程

def sendtogpt(question,wxuser):
        # if  is False
        try:
            chatbot=ueChatpt().ueChatptfuction(wxuser)
            ask=Chatgptwx().send_gpt(question, wxuser, chatbot)
            # ask=str(chatgptwx().send_to_chagpt(question,wxuser))
            # lstripask=str.lstrip(ask)
            print(str.lstrip(ask))
            message_list=[str.lstrip(ask)]
            # print(ask)
            WeChat().send_text(message_list, wxuser)
            return
        except Exception as Argument:
            return (Argument)
class Request(object):
    def GET(self):
        sEchoStr=Handle().GET()
        return sEchoStr
    def POST(self):
        question,wxuser=Handle().POST()
        t = threading.Thread(target=sendtogpt,args=(question,wxuser,))
        t.start()
        # print(web.ctx.values())
        # print(CreateTime)
        # print(web.ctx.values())
        
    