from flask import Flask, request
import random, datetime
app = Flask(__name__)
POOL = [
    {"client":"Rahul Xerox Sironcha","work":"Banner 2x3","budget":800},
    {"client":"Gadchiroli Kirana","work":"Poster","budget":500},
    {"client":"Pune Startup","work":"Logo+Card","budget":4000},
]
JOBS = []
def new_job():
    j = random.choice(POOL).copy()
    j["id"]=len(JOBS)+1
    j["time"]=datetime.datetime.now().strftime("%d %b %I:%M %p")
    j["my_share"]=j["budget"]//2
    JOBS.insert(0,j)
@app.route("/")
@app.route("/hunt")
def home():
    if len(JOBS)==0: new_job()
    if "hunt" in request.path: new_job()
    total=sum(x["my_share"] for x in JOBS)
    cards="".join([f"<div style='background:#0f172a;padding:12px;border-radius:12px;margin:10px 0;border-left:4px solid #22c55e'><b>{j['client']}</b> - {j['work']}<br>Rs {j['budget']} (Tera {j['my_share']})</div>" for j in JOBS])
    return f"<html><meta name='viewport' content='width=device-width'><body style='background:#020617;color:#fff;font-family:sans-serif;padding:16px'><h2>OSP RICH HUNTER ON</h2><div>Total Rs {total}</div><a href='/hunt' style='display:block;background:#22c55e;color:#000;padding:14px;text-align:center;border-radius:12px;margin:14px 0;text-decoration:none'>+ NAYA KAAM DHUND</a>{cards}</body></html>"
if __name__=="__main__":
    app.run(host="0.0.0.0",port=10000)
