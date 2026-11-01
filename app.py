from flask import Flask
import urllib.parse
app=Flask(__name__)
UPI_ID="kirtikapawar57@oksbi"
LEADS=[
 {"client":"Ayyappa Krishi Kendra","phone":"919553844880","work":"Banner"},
 {"client":"Sai Medical Sironcha","phone":"919876543210","work":"Visiting Card"},
]
@app.route("/")
def home():
    cards=""
    for l in LEADS:
        msg=f"Hi {l['client']}, main Omkar OSP se. Aapke liye {l['work']} ka FREE sample banaya hai. Dekhoge? Rs 500 me final dunga."
        enc=urllib.parse.quote(msg)
        # Ye poster link jo maine AI se banaya tha
        poster_url="https://i.ibb.co/placeholder" 
        pay_msg=f"Payment Rs 500 UPI {UPI_ID} pe. QR: https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=upi://pay?pa={UPI_ID}%26am=500"
        pay_enc=urllib.parse.quote(pay_msg)
        cards+=f"<div style='background:#111827;padding:14px;margin:10px 0;border-radius:12px'><b style='color:#22c55e'>{l['client']}</b><br>📞 {l['phone']}<br><a href='https://wa.me/{l['phone']}?text={enc}' style='display:block;background:#22c55e;color:#000;padding:10px;text-align:center;border-radius:8px;margin-top:8px;text-decoration:none;font-weight:900'>1. AUTO MESSAGE</a><a href='https://wa.me/{l['phone']}?text={pay_enc}' style='display:block;background:#facc15;color:#000;padding:10px;text-align:center;border-radius:8px;margin-top:6px;text-decoration:none;font-weight:900'>2. AUTO POSTER + QR BHEJO</a></div>"
    return f"<body style='background:#020617;color:#fff;font-family:sans-serif;padding:12px'><h2>OSP FULL AUTO ROBOT 🤖</h2><div style='background:#22c55e;color:#000;padding:12px;border-radius:10px;font-weight:900'>UPI: {UPI_ID}</div>{cards}<p style='font-size:11px;color:#22c55e'>✅ Fixed - PIL Error Hataya</p></body>"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=10000)
