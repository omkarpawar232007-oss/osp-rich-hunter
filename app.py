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
 for j in JOBS:
  offer_txt=f"Hi {j['client']}, {j['work']} Rs {j['budget']} me bana dunga. OSP Design Sironcha se. Sample dekhoge?"
  offer_enc=urllib.parse.quote(offer_txt)
  upi_link=f"upi://pay?pa={UPI_ID}&pn=Omkar&am={j['share']}&cu=INR"
  upi_enc=urllib.parse.quote(upi_link)
  qr_api=f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={upi_enc}"
  pay_txt=f"Hi {j['client']}, aapka {j['work']} ready hai. Payment Rs {j['share']} is UPI pe kar dijiye: {UPI_ID} . QR: {qr_api}"
  pay_enc=urllib.parse.quote(pay_txt)
  cards+=f"<div style='background:#111827;padding:12px;margin:10px 0;border-radius:12px;border-left:4px solid #22c55e'><b style='color:#22c55e'>{j['client']}</b><br>{j['work']} - Rs {j['budget']} <span style='color:#22c55e'>(Tera {j['share']})</span><br><div style='display:flex;gap:6px;margin-top:8px'><a href='https://wa.me/?text={offer_enc}' target='_blank' style='flex:1;background:#22c55e;color:#000;padding:8px;text-align:center;border-radius:8px;text-decoration:none;font-weight:bold;font-size:12px'>AUTO OFFER</a><a href='https://wa.me/?text={pay_enc}' target='_blank' style='flex:1;background:#fff;color:#000;padding:8px;text-align:center;border-radius:8px;text-decoration:none;font-weight:bold;font-size:12px'>QR BHEJO Rs {j['share']}</a></div></div>"
 return f"<body style='background:#020617;color:#fff;font-family:sans-serif;padding:12px'><h3>OSP RICH HUNTER</h3><div style='background:linear-gradient(90deg,#22c55e,#16a34a);color:#000;padding:14px;border-radius:12px;font-weight:900'>WALLET: Rs {total}<br><span style='font-size:11px'>UPI: {UPI_ID}</span></div><div style='text-align:center;margin:10px 0'><img src='https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=upi://pay?pa={UPI_ID}&pn=Omkar' style='background:#fff;padding:8px;border-radius:10px'><br><span style='font-size:11px;color:#888'>Tera Payment QR - Client isi pe pay karega</span></div><div style='display:flex;gap:8px'><a href='/hunt' style='flex:1;background:#22c55e;color:#000;padding:12px;text-align:center;border-radius:10px;text-decoration:none;font-weight:bold'>+ NAYA CLIENT</a><a href='/withdraw' style='flex:1;background:#111827;color:#fff;padding:12px;text-align:center;border-radius:10px;text-decoration:none;border:1px solid #333'>WITHDRAW</a></div>{cards}</body>"
@app.route("/hunt")
def hunt():
 new_job()
 return home()
@app.route("/withdraw")
def withdraw():
 total=sum(j["share"] for j in JOBS)
 qr=f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=upi://pay?pa={UPI_ID}"
 return f"<body style='background:#020617;color:#fff;font-family:sans-serif;padding:20px;text-align:center'><h2>Withdraw</h2><div style='background:#111827;padding:20px;border-radius:16px'><h1 style='color:#22c55e'>Rs {total}</h1><img src='{qr}' style='background:#fff;padding:10px;border-radius:12px'><p>{UPI_ID}</p><p style='font-size:12px;color:#888'>Client jab QR scan karke pay karega to seedha tere SBI me ayega</p><a href='/' style='color:#22c55e'>Back</a></div></body>"
if __name__=="__main__":
 app.run(host="0.0.0.0",port=10000)
