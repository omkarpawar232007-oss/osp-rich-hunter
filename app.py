from flask import Flask
import random,datetime,urllib.parse
app=Flask(__name__)
UPI_ID="kirtikapawar57@oksbi"
POOL=[("Rahul Xerox Sironcha","Banner 2x3 Design",800),("Sai Medical Sironcha","Visiting Card",600),("Pune Startup Hub","Logo + Letterhead",4000),("Nagpur Cloth Store","Insta Poster Pack",2500),("Aheri Kirana","Price List Banner",500),("Gadchiroli Classes","Admission Poster",1200),("Chamorshi Hotel","Menu Card",3000)]
JOBS=[]
def new_job():
 c,w,b=random.choice(POOL)
 JOBS.insert(0,{"client":c,"work":w,"budget":b,"share":b//2,"time":datetime.datetime.now().strftime("%I:%M %p")})
 if len(JOBS)>20:
  JOBS.pop()
@app.route("/")
def home():
 if not JOBS:
  new_job()
 total=sum(j["share"] for j in JOBS)
 cards=""
 for idx,j in enumerate(JOBS):
  offer_txt=f"Hi {j['client']}, {j['work']} Rs {j['budget']} me bana dunga. OSP Design Sironcha se. Sample dekhoge?"
  pay_txt=f"Hi {j['client']}, aapka {j['work']} ready hai. Payment Rs {j['share']} is UPI pe: {UPI_ID}"
  cards+=f"<div style='background:#111827;padding:12px;margin:10px 0;border-radius:12px;border-left:4px solid #22c55e'><b style='color:#22c55e'>{j['client']}</b><br>{j['work']} - Rs {j['budget']}<br><div style='display:flex;gap:6px;margin-top:8px'><button onclick=\"let n=prompt(' {j['client']} ka WhatsApp number daal (91 ke saath) ex: 919876543210'); if(n){{window.open('https://wa.me/'+n+'?text='+encodeURIComponent(`{offer_txt}`),'_blank')}} \" style='flex:1;background:#22c55e;color:#000;padding:8px;border-radius:8px;border:0;font-weight:bold'>AUTO OFFER</button><button onclick=\"let n=prompt(' {j['client']} ka number daal'); if(n){{window.open('https://wa.me/'+n+'?text='+encodeURIComponent(`{pay_txt} QR: https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=upi://pay?pa={UPI_ID}%26am={j['share']}`),'_blank')}} \" style='flex:1;background:#fff;color:#000;padding:8px;border-radius:8px;border:0;font-weight:bold'>QR BHEJO</button></div></div>"
 return f"<body style='background:#020617;color:#fff;font-family:sans-serif;padding:12px'><h3>OSP RICH HUNTER - FIXED</h3><div style='background:#22c55e;color:#000;padding:14px;border-radius:12px;font-weight:900'>WALLET: Rs {total} | UPI: {UPI_ID}</div><div style='display:flex;gap:8px;margin:12px 0'><a href='/hunt' style='flex:1;background:#22c55e;color:#000;padding:12px;text-align:center;border-radius:10px;text-decoration:none;font-weight:bold'>+ NAYA CLIENT</a></div>{cards}<script></script></body>"
@app.route("/hunt")
def hunt():
 new_job()
 return home()
@app.route("/withdraw")
def withdraw():
 total=sum(j["share"] for j in JOBS)
 return f"<body style='background:#020617;color:#fff;padding:20px;text-align:center'><h2 style='color:#fff'>Rs {total}</h2><img src='https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=upi://pay?pa={UPI_ID}' style='background:#fff;padding:10px;border-radius:12px'><p style='color:#fff'>{UPI_ID}</p><a href='/' style='color:#22c55e'>Back</a></body>"
if __name__=="__main__":
 app.run(host="0.0.0.0",port=10000)
