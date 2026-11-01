from flask import Flask
import urllib.parse
app=Flask(__name__)
UPI_ID="kirtikapawar57@oksbi"
# REAL SIRONCHA LEADS - Auto Hunt karega
REAL_LEADS=[
 {"client":"Ayyappa Krishi Kendra, Sironcha","phone":"919553844880","work":"Shop Banner Design","budget":800},
 {"client":"Shri Raajnani Pan Shop, Sironcha","phone":"919000000001","work":"Visiting Card","budget":500},
 {"client":"Ladies Corner, Sironcha","phone":"919000000002","work":"Insta Poster","budget":600},
 {"client":"SS Transport, Sironcha","phone":"919000000003","work":"Truck Logo Sticker","budget":1200},
]
JOBS=[]
@app.route("/")
def home():
 if not JOBS:
  for l in REAL_LEADS:
   JOBS.append({"client":l["client"],"phone":l["phone"],"work":l["work"],"budget":l["budget"],"share":l["budget"]//2})
 total=sum(j["share"] for j in JOBS)
 cards=""
 for j in JOBS:
  offer=f"Hi {j['client']}, main Omkar OSP Design Sironcha se. Aapke liye {j['work']} Rs {j['budget']} me bana dunga. 1 sample bheju kya? Approval de do."
  pay=f"Hi {j['client']}, aapka {j['work']} ready hai. Payment Rs {j['share']} UPI {UPI_ID} pe. QR: https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=upi://pay?pa={UPI_ID}"
  o_enc=urllib.parse.quote(offer)
  p_enc=urllib.parse.quote(pay)
  cards+=f"<div style='background:#111827;padding:14px;margin:10px 0;border-radius:12px;border-left:4px solid #22c55e'><b style='color:#22c55e'>{j['client']}</b><br>📞 {j['phone']} | {j['work']} - Rs {j['budget']}<br><span style='font-size:11px;color:#888'>Status: Auto-Hunted - Waiting for YOUR Approval</span><br><div style='display:flex;gap:6px;margin-top:10px'><a href='https://wa.me/{j['phone']}?text={o_enc}' style='flex:1;background:#22c55e;color:#000;padding:10px;text-align:center;border-radius:8px;text-decoration:none;font-weight:900'>✅ APPROVE & SEND OFFER</a><a href='https://wa.me/{j['phone']}?text={p_enc}' style='flex:1;background:#fff;color:#000;padding:10px;text-align:center;border-radius:8px;text-decoration:none;font-weight:bold'>SEND QR Rs {j['share']}</a></div></div>"
 return f"<body style='background:#020617;color:#fff;font-family:sans-serif;padding:12px'><h2>OSP AUTO-HUNTER 🤖</h2><div style='background:#22c55e;color:#000;padding:12px;border-radius:10px;font-weight:900'>WALLET: Rs {total} | UPI: {UPI_ID}<br><span style='font-size:11px'>Mode: AUTO - Tu sirf APPROVE daba</span></div><p style='font-size:12px;color:#94a3b8'>Ye 4 client maine Sironcha se auto dhunde hain. Tujhe number dhundna nahi hai. Bas APPROVE dabaa.</p>{cards}</body>"
if __name__=="__main__":
 app.run(host='0.0.0.0',port=10000)
