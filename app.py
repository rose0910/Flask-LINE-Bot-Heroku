import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("IdVOL5mPTVxo/5IbGnYOVzcUdtjMfyZoLHW+f7IzfwPg8Ulacyx4oFJLhe9I9twLOCw9p/h71EyqCgT1GUX5FGIlp44I9JCqprVWiCT0/Lj5uoSyaj8EzVZHQPcG77P9EdfC1dWwfYCKnNMUIiFJ4gdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.environ.get("da87edeac37d2fa01ba707bb865c5789"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
