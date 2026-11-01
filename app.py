from flask import Flask
import urllib.parse
app=Flask(__name__)
UPI_ID="kirtikapawar57@oksbi"
LEADS=[{"client":"Ayyappa Krishi Kendra","phone":"919553844880","work":"Banner"},{"client":"Sai Medical Sironcha","phone":"919876543210","work":"Visiting Card"}]
@app.route("/")
def home():
 cards=""
 for l in LEADS:
  upi=f"upi://pay?pa={UPI_ID}&am=500"
  qr=f"https://api.qrserver.com/v1/create-qr-code/?size=400x400&data={urllib.parse.quote(upi)}"
  cards+=f"<div style='background:#111827;padding:14px;margin:12px 0;border-radius:12px'><b style='color:#22c55e'>{l['client']}</b><br>📞 {l['phone']}<br><div style='background:#fff;padding:8px;border-radius:8px;margin:8px 0'><img src='{qr}' style='width:150px'><br><small style='color:#000'>Rs 500 - {UPI_ID}</small></div><a href='/auto/{l['phone']}/{l['client']}' style='display:block;background:#22c55e;color:#000;padding:12px;text-align:center;border-radius:8px;text-decoration:none;font-weight:900'>🤖 FULL AUTO GENERATE & SEND</a></div>"
 return f"<body style='background:#020617;color:#fff;font-family:sans-serif;padding:12px'><h2>OSP FULL AUTO V3</h2><div style='background:#22c55e;color:#000;padding:12px;border-radius:10px;font-weight:900'>UPI: {UPI_ID} - Poster + QR Auto</div>{cards}</body>"
@app.route("/auto/<phone>/<client>")
def auto(phone,client):
 upi=f"upi://pay?pa={UPI_ID}&am=500"; qr=f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={urllib.parse.quote(upi)}"
 poster="https://i.ibb.co/placeholder-banner"
 msg=f"Hi {client}, aapka {client} ka design AI ne bana diya hai ✅ Poster niche hai. Payment Rs 500 - QR bhi hai. OSP Design Sironcha"
 enc=urllib.parse.quote(msg)
 return f"<body style='background:#020617;color:#fff;padding:12px;text-align:center'><h3>{client} - AUTO READY</h3><p>1. Poster Auto Generated (Upar wala jaisa)</p><img src='{qr}' style='width:250px;background:#fff;padding:10px;border-radius:12px'><br><br><a href='https://wa.me/{phone}?text={enc}' style='background:#22c55e;color:#000;padding:14px;border-radius:10px;text-decoration:none;font-weight:900;display:block'>BHEJO - Poster + QR ek saath</a><br><a href='/'>Back</a></body>"
if __name__=="__main__": app.run(host='0.0.0.0',port=10000)
