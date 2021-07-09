import requests
from flask import Flask, render_template, request
from twilio.rest import Client

account_sid = 'ACf30a1fed8d98a3f1576de13e511db950'
auth_token = '2c3914ae241f4d9af34f5f7aaeb40089'
client = Client(account_sid, auth_token)

app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
    return render_template('app.html')

@app.route('/app',methods=['POST','GET'])
def reg():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    src = request.form['source']
    ds = request.form['ds']
    d = request.form['d']
    sdate = request.form['sdate']
    rdate = request.form['rdate']
    count = request.form['count']
    
    covidData = requests.get('https://api.covid19india.org/v4/data.json')
    js = covidData.json()
    conformed = js[ds]['districts'][d]['total']['confirmed']
    total_pop=js[ds]['districts'][d]['meta']['population']
    epass=((conformed/total_pop)*100)
    if epass<30 and request.method=='POST':
        status='CONFIRMED'
        message = client.messages.create(
            to="+917993152245",
            from_="+12672043203",
            body="Dear " + name + " your epass status for travelling to " + ds + " " + d + " is " + " " + status)
        return render_template('screen2.html',f = name, phno = phone , mail = email, cs = "Telangana", place = src, des_s = ds, destination = d, md = sdate, cd = rdate, es = status)
    else:
        status='REJECTED'
        message = client.messages.create(
            to="+917993152245",
            from_="+12672043203",
            body="Dear " + name + " your epass status for travelling to " + ds + " " + d + " is " + " " + status + " due to more covid cases in destination area")
        return render_template('screen2.html',f = name, phno = phone , mail = email, cs = "Telangana", place = src, des_s = ds, destination = d, md = sdate, cd = rdate, es = status)




if __name__=='__main__':
    app.run(debug=True)