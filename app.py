 from flask import Flask, request
import random, datetime
app = Flask(__name__)

POOL = [
    {"client":"Rahul Xerox Sironcha","work":"Banner 2x3 Design","budget":800, "num":"+91 9XXXX XXXXX"},
    {"client":"Sai Medical Sironcha","work":"Visiting Card","budget":600, "num":"+91 9XXXX XXXXX"},
    {"client":"Pune Startup Hub","work":"Logo + Letterhead","budget":4000, "num":"+91 7XXXX XXXXX"},
    {"client":"Nagpur Cloth Store","work":"Insta Poster Pack (10)","budget":2500, "num":"+91 8XXXX XXXXX"},
    {"client":"Aheri Kirana","work":"Price List Banner","budget":500, "num":"+91 9XXXX XXXXX"},
    {"client":"Gadchiroli Classes","work":"Admission Poster","budget":1200, "num":"+91 7XXXX XXXXX"},
    {"client":"Chamorshi Hotel","work":"Menu Card Design","budget":3000, "num":"+91 8XXXX XXXXX"},
]

JOBS = []
def new_job():
    j = random.choice(POOL).copy()
    # repeat rokne ke liye check
    if JOBS and JOBS[0]['client'] == j['client']:
        j = random.choice(POOL).copy()
    j["id"]=len(JOBS)+1
    j["time"]=datetime.datetime.now().strftime("%d %b %I:%M %p")
    j["my_share"]=j["budget"]//2
    JOBS.insert(0,j)
    if len(JOBS)>20: JOBS.pop()

@app.route("/")
@app.route("/hunt")
def home():
    if len(JOBS)==0: new_job()
    if "hunt" in request.path: new_job()
    total=sum(x["my_share"] for x in JOBS)
    cards="".join([f"""
    <div style='background:#0f172a;padding:14px;border-radius:16px;margin:12px 0;border:1px solid #1e293b;border-left:4px solid #22c55e'>
    <div style='display:flex;justify-content:space-between'><b style='color:#22c55e'>{j['client']}</b><span style='font-size:11px;color:#94a3b8'>{j['time']}</span></div>
    <div style='margin:4px 0;color:#e2e8f0'>{j['work']}</div>
    <div style='display:flex;justify-content:space-between;align-items:center;margin-top:8px'>
    <div><b>Rs {j['budget']}</b> <span style='color:#22c55e'>(Tera Profit Rs {j['my_share']})</span></div>
    <a href='https://wa.me/91XXXXXXXXXX?text=Hi {j['client']} kaam ke liye' style='background:#22c55e;color:#000;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:12px'>WHATSAPP</a>
    </div>
    </div>""" for j in JOBS])
    
    return f"""
    <html><head><meta name='viewport' content='width=device-width'><title>OSP RICH HUNTER</title></head>
    <body style='background:#020617;color:#fff;font-family:sans-serif;padding:16px;margin:0'>
    <h2 style='margin:0'>🎯 OSP RICH HUNTER <span style='background:#22c55e;color:#000;font-size:10px;padding:3px 8px;border-radius:10px'>ON</span></h2>
    <div style='background:linear-gradient(90deg,#22c55e,#16a34a);color:#000;padding:12px;border-radius:12px;margin:12px 0;font-weight:bold'>Total Profit: Rs {total} | Total Jobs: {len(JOBS)}</div>
    <a href='/hunt' style='display:block;background:#22c55e;color:#000;padding:16px;text-align:center;border-radius:14px;margin:14px 0;text-decoration:none;font-weight:900;font-size:18px;box-shadow:0 0 20px #22c55e55'>+ NAYA KAAM DHUNDO</a>
    {cards}
    <div style='text-align:center;color:#475569;font-size:11px;margin-top:30px'>Made for Omkar - Sironcha</div>
    </body></html>
    """
if __name__=="__main__":
    app.run(host="0.0.0.0",port=10000)
