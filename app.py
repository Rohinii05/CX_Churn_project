from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open("model.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def Customer_Churning_Data():
    accountlength=int(request.form.get("accountlength"))
    internationalplan=int(request.form.get("internationalplan"))
    voicemailplan=float(request.form.get("voicemailplan"))
    numbervmailmessages=float(request.form.get("numbervmailmessages"))
    totaldayminutes=float(request.form.get("totaldayminutes"))
    totaldaycalls=float(request.form.get("totaldaycalls"))
    totaldaycharge=float(request.form.get("totaldaycharge"))
    totaleveminutes=float(request.form.get("totaleveminutes"))
    totalevecalls=float(request.form.get("totalevecalls"))
    totalevecharge=float(request.form.get("totalevecharge"))
    totalnightminutes=float(request.form.get("totalnightminutes"))
    totalnightcalls=float(request.form.get("totalnightcalls"))
    totalnightcharge=float(request.form.get("totalnightcharge"))
    totalintlminutes=float(request.form.get("totalintlminutes"))
    totalintlcalls=float(request.form.get("totalintlcalls"))
    totalintlcharge=float(request.form.get("totalintlcharge"))
    numbercustomerservicecalls=float(request.form.get("numbercustomerservicecalls"))
    
    result=model.predict(np.array([[accountlength,internationalplan,voicemailplan,numbervmailmessages,totaldayminutes,
                                    totaldaycalls,totaldaycharge,totaleveminutes,totalevecalls,totalevecharge
                                    ,totalnightminutes,totalnightcalls,totalnightcharge,totalintlminutes,
                                    totalintlcalls,totalintlcharge,numbercustomerservicecalls]]))
    
    if result[0]==1:
        return "<h1 style='color:green'>CHURNED</h1>"
    else:
        return "<h1 style='color:red'>NOT CHURNED</h1>"  

app.run(debug=True,port=8080)