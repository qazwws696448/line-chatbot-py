import csv

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('EISyJeC+l4ZKw70LI+O+Z84PsC7OFDwshO66ebyECGjxF4A+UB5+o2yszcqIPDjTGQ4/TKdbzVv7YWc+bvj8QrlO+Ss6FaNPIf25Ir/kI0hdJLVjB3q8QX96FsdnVdAseQCRl+w/qKlHetjbYkR1jwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5154bae844564125d7981cb97b1de3b9')

@app.route("/callback", methods=['POST'])
def callback():
    # 從請求中獲取 X-Line-Signature 頭部，用於後續的驗證
    signature = request.headers['X-Line-Signature']

    # 獲取請求正文作為文字（text）
    body = request.get_data(as_text=True)

    # 處理 Webhook
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理文字消息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 這裡可以根據 event.message.text 的內容來判斷要執行哪種功能
    # 例如：查詢位置資訊、行事曆查詢等
    # 下面是一個簡單的回應範例
    if "位置" in user_message or "查詢教室/處室" in user_message:
        reply_message = "https://www.ntut.edu.tw/var/file/7/1007/img/2858/campusMap.jpg"
    elif "行事曆" in user_message:
        reply_message = "https://oaa.ntut.edu.tw/p/412-1008-12781.php?Lang=zh-tw"
    elif "查詢教室/處室" in user_message:
    	reply_message = "https://www.ntut.edu.tw/var/file/7/1007/img/2858/campusMap.jpg"
    elif "停車證申請" in user_message:
    	reply_message = "https://servicecenter.ntut.edu.tw/p/412-1106-15586.php"
    elif "美食" in user_message:
	reply_message= ""
        with open('food.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
            	reply_message=reply_message+row[0]+"|評論:"+row[1]+"|"+row[2]
    elif "課程" in user_message:
	reply_message=""
        with open('class.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
            	reply_message=reply_message+row[0]+"|必修/選修:"+row[1]+"|"+row[2]
    elif "活動" in user_message:
	reply_message=""
        with open('activity.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
            	reply_message=reply_message+row[0]+"|時間:"+row[1]+"|"+row[2]+"|"+row[3]
    elif "餐廳" in user_message:
	reply_message=""
        with open('resturant.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
            	reply_message=reply_message+row[0]+"|價格區間:"+row[1]+"|"+row[2]+"|"+row[3]
    elif "社團" in user_message:
	reply_message="https://stass.ntut.edu.tw/"
    elif "交通資訊" in user_message:
	reply_message="捷運 藍線【板南土城線】忠孝新生4號出口 橘線【中和新蘆線】忠孝新生3號出口(去先鋒比較快)\n"					
	reply_message=reply_message+"搭乘公車 台北科技大學站--212、212直達車、232、262、299及605 忠孝新生路口站--72、109、115、214、222、226、280、290、505、642、665、668、672及松江新生幹線\n"
	reply_message=reply_message+"Ubike站點	忠孝新生3、4號出口站旁 建國南路一段(綜合科館旁) 億光大樓(宿舍)\n"
    elif "入口網站" in user_message:
	reply_message="https://nportal.ntut.edu.tw/index.do?thetime=1697944963579"					
    elif "申請" in user_message:
	reply_message="進修部表單 https://wwwoce.ntut.edu.tw/p/412-1033-103.php?Lang=zh-tw\n教務處 https://oaa.ntut.edu.tw/p/412-1008-12839.php?Lang=zh-tw\n總務處 https://oga.ntut.edu.tw/p/426-1040-7.php?Lang=zh-tw"
    elif "獎學金申請" in user_message:
	reply_message="https://scholarship.ntut.edu.tw/	"					
    elif "新生專區" in user_message:
	reply_message="https://oga.ntut.edu.tw/p/426-1040-7.php?Lang=zh-tw"	"					
    else:
        reply_message = "抱歉，我不明白您的問題。"


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message))

if __name__ == "__main__":
    app.run()
