from flask import Flask
import random
import datetime
app = Flask(__name__)
POOL = [
("Rahul Xerox Sironcha", "Banner 2x3 Design", 800),
("Sai Medical Sironcha", "Visiting Card", 600),
("Pune Startup Hub", "Logo + Letterhead", 4000),
("Nagpur Cloth Store", "Insta Poster Pack", 2500),
("Aheri Kirana", "Price List Banner", 500),
("Gadchiroli Classes", "Admission Poster", 1200),
("Chamorshi Hotel", "Menu Card", 3000),
]
JOBS = []
def new_job():
    client, work, budget = random.choice(POOL)
    job = {"client": client, "work": work, "budget": budget, "share": budget//2, "time": datetime.datetime.now().strftime("%d %b %I:%M %p")}
    JOBS.insert(0, job)
    if len(JOBS) > 20:
        JOBS.pop()
@app.route("/")
def home():
    if not JOBS:
        new_job()
    total = sum(j["share"] for j in JOBS)
    html = ""
    for j in JOBS:
        html += f"<div style='background:#111827;padding:14px;border-radius:14px;margin:10px 0;border-left:4px solid #22c55e'><b style='color:#22c55e'>{j['client']}</b><br>{j['work']}<br>Rs {j['budget']} <span style='color:#22c55e'>(Tera {j['share']})</span> <span style='float:right;font-size:11px;color:#888'>{j['time']}</span></div>"
    return f"<body style='background:#020617;color:white;font-family:sans-serif;padding:15px'><h2>OSP RICH HUNTER</h2><div style='background:#22c55e;color:black;padding:10px;border-radius:10px;font-weight:bold'>Total Profit: Rs {total}</div><a href='/hunt' style='display:block;background:#22c55e;color:black;padding:15px;text-align:center;border-radius:12px;margin:15px 0;text-decoration:none;font-weight:900'>+ NAYA KAAM DHUNDO</a>{html}</body>"
@app.route("/hunt")
def hunt():
    new_job()
    return home()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000
