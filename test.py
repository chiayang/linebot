from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser

import random

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi('nu2OHZJBl5br8W4zT7CcyLy+kvc1ed5d1oLr7Zw+oBUnfC0BmoHOELiYJ9k51UhHgAY0S36N7eIi5NQ/9eAs5fRQn4Rb2r1Emy1JCA00MyfpKKffgLrczTpdADLUEp5Z+4oKX/tgq4WRo1JtFykUnQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c06432784369678e5fe946f458e75a68')


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    
    if event.source.user_id != "Uc5df4ddce57b7997360dac4805a42fca":
        
        # Phoebe 愛唱歌
        pretty_note = '♫♪♬'
        pretty_text = ''
        
        for i in event.message.text:
        
            pretty_text += i
            pretty_text += random.choice(pretty_note)
    
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=pretty_text)
        )

if __name__ == "__main__":
    app.run()



# from flask import Flask, request, abort

# from linebot import (LineBotApi, WebhookHandler)
# from linebot.exceptions import (InvalidSignatureError)
# from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

# import os
# import sys


# app = Flask(__name__)

# # get channel_secret and channel_access_token from your environment variable
# channel_secret = os.getenv('c06432784369678e5fe946f458e75a68', None)
# channel_access_token = os.getenv('nu2OHZJBl5br8W4zT7CcyLy+kvc1ed5d1oLr7Zw+oBUnfC0BmoHOELiYJ9k51UhHgAY0S36N7eIi5NQ/9eAs5fRQn4Rb2r1Emy1JCA00MyfpKKffgLrczTpdADLUEp5Z+4oKX/tgq4WRo1JtFykUnQdB04t89/1O/w1cDnyilFU=', None)
# if channel_secret is None or channel_access_token is None:
#     print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
#     sys.exit(1)

# line_bot_api = LineBotApi(channel_access_token)
# handler = WebhookHandler(channel_secret)

# # 此為 Webhook callback endpoint
# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body（負責）
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         print("Invalid signature. Please check your channel access token/channel secret.")
#         abort(400)

#     return 'OK'

# # decorator 負責判斷 event 為 MessageEvent 實例，event.message 為 TextMessage 實例。所以此為處理 TextMessage 的 handler
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     # 決定要回傳什麼 Component 到 Channel
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))


# if __name__ == '__main__':
#     app.run()
