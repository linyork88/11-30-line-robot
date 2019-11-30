# 準備資料
import json
file=open("search.txt",mode="r",encoding="utf-8")
data=json.load(file)
file.close() #一定要關，否則會出現你的程式正被使用


#flask
#建立網站伺服器
from flask import * #載入flask模組
app=Flask("MY website")#建立一個網站應用程式物件

#網站的網址:http://主機名稱/路徑?參數名稱=資料&參數名稱=資料&...
#例如：http://127.0.0.1:5000/
@app.route("/")#指定對應的網址路徑
def home(): #對應的處理函式
    return "<h3>Hello Flask</h3><div>this is line 1</div><script>alert('Hello');</script>" #回應給前端的訊息

#例如：http://127.0.0.1:5000/test.php?keyword=關鍵字
@app.route("/test.php")#指定對應的網址路徑
def test(): #對應的處理函示
    #取得網址列上的參數:request.args.get(參數名稱,預設值)
    keyword=request.args.get("keyword",None)
    if keyword==None:
        return redirect("/") #導向到路徑 /
    else:
        if keyword in data:
            return "中文:"+data[keyword]
        else:
            return "沒有翻譯"#回應給前端的訊息

app.run() #啟動伺服器