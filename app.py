from flask import Flask,send_file
import urllib.parse,os
from PIL import Image,ImageDraw,ImageFont
app=Flask(__name__)
UPI_ID="kirtikapawar57@oksbi"
LEADS=[
 {"client":"Ayyappa Krishi Kendra","phone":"919553844880","work":"Banner"},
 {"client":"Sai Medical Sironcha","phone":"919876543210","work":"Visiting Card"},
]
# Yaha AI Poster banega
def make_poster(name,work):
    img=Image.new('RGB',(1080,1350),(2,6,23))
    d=ImageDraw.Draw(img)
    d.rectangle([0,0,1080,300],fill=(34,197,94))
    d.text((50,50),name,fill="white")
    d.text((50,150),work,fill="white")
    d.text((50,400),f"Contact: {UPI_ID}",fill="white")
    d.text((50,1100),f"Pay: {UPI_ID}",fill=(34,197,94))
    path=f"/tmp/{name}.png"
    img.save(path)
    return path

@app.route("/")
def home():
    cards=""
    for l in LEADS:
        msg=f"Hi {l['client']}, main Omkar OSP se. Aapke liye {l['work']} ka FREE sample banaya hai. Dekhoge? Rs 500 me final dunga. - OSP Design"
        enc=urllib.parse.quote(msg)
        cards+=f"<div style='background:#111827;padding:14px;margin:10px 0;border-radius:12px'><b style='color:#22c55e'>{l['client']}</b><br>📞 {l['phone']}<br><a href='https://wa.me/{l['phone']}?text={enc}' style='display:block;background:#22c55e;color:#000;padding:10px;text-align:center;border-radius:8px;margin-top:8px;text-decoration:none;font-weight:900'>1. AUTO MESSAGE BHEJO</a><a href='/make/{l['client']}' style='display:block;background:#fff;color:#000;padding:10px;text-align:center;border-radius:8px;margin-top:6px;text-decoration:none;font-weight:900'>2. AUTO POSTER BANAO</a><a href='/pay/{l['phone']}' style='display:block;background:#facc15;color:#000;padding:10px;text-align:center;border-radius:8px;margin-top:6px;text-decoration:none;font-weight:900'>3. AUTO PAYMENT QR BHEJO</a></div>"
    return f"<body style='background:#020617;color:#fff;font-family:sans-serif;padding:12px'><h2>OSP FULL AUTO ROBOT 🤖</h2><div style='background:#22c55e;color:#000;padding:12px;border-radius:10px;font-weight:900'>UPI AUTO-RECEIVE: {UPI_ID}<br><span style='font-size:10px'>3 Step - Tu sirf 1-2-3 dabaa</span></div>{cards}<p style='font-size:11px;color:#888;margin-top:20px'>Logic: Step 1 Message -> Step 2 AI Poster -> Step 3 UPI QR. Client Haan bolega to poster auto WhatsApp pe jayega.</p></body>"

@app.route("/make/<name>")
def make(name):
    path=make_poster(name,"Banner Design")
    return send_file(path,mimetype='image/png')

@app.route("/pay/<phone>")
def pay(phone):
    upi_link=f"upi://pay?pa={UPI_ID}&am=500&tn=Payment for Design"
    qr=f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={urllib.parse.quote(upi_link)}"
    msg=f"Payment Rs 500 ka QR. Scan karke pay karo. UPI: {UPI_ID} QR: {qr}"
    enc=urllib.parse.quote(msg)
    return f"<script>window.location='https://wa.me/{phone}?text={enc}'</script>"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=10000)
