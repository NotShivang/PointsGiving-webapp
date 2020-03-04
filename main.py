import os
from flask import Flask, render_template, request

import pymysql 

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

app = Flask(__name__)


if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,
                              host=host, db=db_name)


uname = ""
tpid=0
uid=0
balance=0
@app.route('/')
def main():

	with cnx.cursor() as cursor:
	
		cursor.execute('SELECT UserId, Name, Role from Users;')
		data = cursor.fetchall()

	return render_template('home.html', data=data)

@app.route('/Login')
def tlogin():
    return render_template('Login.html')

#need add logic to reroute to adminhome
@app.route('/Login', methods=['POST'])
def login():
	global uname
	global tpid
	global uid
	global balance
	UserID = request.form['UserID']
	_UserID = str(UserID)
	uid=_UserID
	pwd = request.form['pwd']
	_pwd = str(pwd)
	with cnx.cursor() as cursor:
		cursor.execute('SELECT count(*) from Users where UserId = %s and Password = %s ;',(_UserID,_pwd))
		d = cursor.fetchone()
		cursor.execute('select max(TimePeriodId) from User_Month;')
		tpid=int(cursor.fetchone()[0])
		
		if(d!=(0,)):
			cursor.execute('SELECT Name from Users where UserId = %s and Password = %s ;',(_UserID,_pwd))
			uname=str(cursor.fetchone()[0])
			cursor.execute('SELECT Role from Users where UserId = %s and Password = %s ;',(_UserID,_pwd))
			adm=str(cursor.fetchone()[0])
			if(adm=='Admin'):
				return render_template('tadmin.html')
			else:
				cursor.execute('SELECT PointsToGive FROM User_Month WHERE UserId = %s and TimePeriodId=%s;', (uid,tpid))
				balance = int(cursor.fetchone()[0])
				return render_template('thome.html')
		else:
			return str("Wrong UserID or Wrong Password")
			
@app.route('/userhome')
def t():
	global uname
	global tpid
	global uid
	pr=0
	with cnx.cursor() as cursor:
		
		cursor.execute('Select Description from Time_Periods where TimePeriodId=%s;',(tpid))
		d=str(cursor.fetchone()[0])
		for i in range(1,tpid+1):
			cursor.execute('select PointsReceived from User_Month where UserId=%s and TimePeriodId=%s;',(uid,i))
			pr=pr+int(cursor.fetchone()[0])
		cursor.execute('SELECT SenderId,ReceiverId,NumberOfPoints,Message,TimePeriodId from Transactions where SenderId=%s or ReceiverId=%s;',(uid,uid))
		data=cursor.fetchall()
	return render_template('userhome.html', uname = uname, pr=pr,data=data,tpid=tpid,d=d)
	
@app.route('/adminhome')
def t2():
	global uname
	return render_template('adminhome.html', uname = uname)

@app.route('/sendpoints')
def sendpoints():
	global balance
	global tpid
	global uid
	with cnx.cursor() as cursor:
		cursor.execute('SELECT PointsToGive FROM User_Month WHERE UserId = %s and TimePeriodId=%s;', (uid,tpid))
		balance = int(cursor.fetchone()[0])
		cursor.execute('SELECT UserId from Users where Name != %s and Role!="Admin";',uname)
		recs=cursor.fetchall()
	return render_template('sendpoints.html',recs=recs,balance=balance)

#shivang can you take a look at this?
#not sure how to get id of user logged in: we have a global variable called uname that stores the username of person logged in
#its not sending back to userhome.html page and not updating the database

@app.route('/sendpoints', methods=['POST'])
def postsendpoints():
	global uname
	global tpid
	global uid
	global balance
	r = str(request.form['receiverid'])
	receiver = int(r[1])
	pointssent = int(request.form['pointstosend'])
	m = str(request.form['mess'])
	with cnx.cursor() as cursor:
		if (balance >= pointssent):
			cursor.execute('INSERT INTO Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints,Message) VALUES (%s, %s, %s, %s, %s);', (uid,receiver,tpid,pointssent,m))
			cursor.execute('commit;')
			cursor.execute('UPDATE User_Month SET PointsToGive = PointsToGive-%s WHERE UserID=%s and TimePeriodId=%s;', (pointssent,uid,tpid))
			cursor.execute('commit;')
			cursor.execute('UPDATE User_Month SET PointsReceived = PointsReceived+%s WHERE UserID=%s and TimePeriodId=%s;', (pointssent,receiver,tpid))
			cursor.execute('commit;')
			balance=balance-pointssent
			return render_template('thome.html')
		else: 
			return str("You do not have enough points for this transaction")
	

@app.route('/redeempoints')
def redeempoints():
	global uid
	with cnx.cursor() as cursor:
		cursor.execute('SELECT sum(PointsReceived) FROM User_Month WHERE UserId = %s;', (uid))
		redeembalance = int(cursor.fetchone()[0])
	return render_template('redeempoints.html',redeembalance=redeembalance)

@app.route('/redeempoints', methods=['POST'])
def postredeempoints():
	pointstoredeem = int(request.form['redeeming'])
	global tpid
	global uid
	with cnx.cursor() as cursor:
		cursor.execute('SELECT sum(PointsReceived) FROM User_Month WHERE UserId = %s;', (uid))
		redeembalance = int(cursor.fetchone()[0])
		if (int(redeembalance) >= int(pointstoredeem)):
			cursor.execute('UPDATE User_Month SET PointsRedeemed = PointsRedeemed + %s WHERE UserId = %s and TimePeriodId = %s;', (pointstoredeem, uid, tpid))
			cursor.execute('commit;')
			cursor.execute('UPDATE User_Month SET PointsReceived = PointsReceived - %s WHERE UserId = %s and TimePeriodId = %s;', (pointstoredeem, uid, tpid))
			cursor.execute('commit;')
			redeembalance = int(redeembalance) - int(pointstoredeem)
			return render_template('thome.html')
		else: 
			return str("You do not have this many points to redeem")

@app.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')

@app.route('/report1')
def report1():
	with cnx.cursor() as cursor:
		cursor.execute('select * from r1;')
		data1=cursor.fetchall()
		cursor.execute('select * from r11;')
		data=cursor.fetchall()
	return render_template('report1.html',data=data,data1=data1)

@app.route('/report2')
def report2():
	global tpid
	with cnx.cursor() as cursor:
		cursor.execute('select max(TimePeriodId) from User_Month;')
		tpid=int(cursor.fetchone()[0])
		cursor.execute('select UserId,PointsToGive,TimePeriodId from User_Month where TimePeriodId=%s;',tpid)
		data=cursor.fetchall()
	return render_template('report2.html',data=data)

@app.route('/report3')
def report3():
	global tpid
	with cnx.cursor() as cursor:
		cursor.execute('select max(TimePeriodId) from User_Month;')
		tpid=int(cursor.fetchone()[0])
		cursor.execute('select UserId,sum(PointsRedeemed),TimePeriodId from User_Month where TimePeriodId>%s group by TimePeriodId,UserId;',(tpid-2))
		data=cursor.fetchall()
	return render_template('report3.html',data=data)
	

@app.route('/endmonth')
def endmonth():
	global tpid
	return render_template('endmonth.html',tpid=tpid)
	
@app.route('/endmonth', methods=['POST'])
def postem():
	global tpid
	with cnx.cursor() as cursor:
		cursor.execute('select max(TimePeriodId) from User_Month;')
		tpid=int(cursor.fetchone()[0])
		tpid=tpid+1
		desc = str(request.form['description'])
		cursor.execute('insert into Time_Periods values (%s,%s);',(tpid,desc))
		cursor.execute('commit;')
		cursor.execute('insert into User_Month(UserId,PointsGiven,PointsReceived,PointsRedeemed,TimePeriodId,PointsToGive) values (2,0,0,0,%s,1000);',(tpid))
		cursor.execute('commit;')
		cursor.execute('insert into User_Month(UserId,PointsGiven,PointsReceived,PointsRedeemed,TimePeriodId,PointsToGive) values (3,0,0,0,%s,1000);',(tpid))
		cursor.execute('commit;')
		cursor.execute('insert into User_Month(UserId,PointsGiven,PointsReceived,PointsRedeemed,TimePeriodId,PointsToGive) values (4,0,0,0,%s,1000);',(tpid))
		cursor.execute('commit;')
		cursor.execute('insert into User_Month(UserId,PointsGiven,PointsReceived,PointsRedeemed,TimePeriodId,PointsToGive) values (5,0,0,0,%s,1000);',(tpid))
		cursor.execute('commit;')
		cursor.execute('insert into User_Month(UserId,PointsGiven,PointsReceived,PointsRedeemed,TimePeriodId,PointsToGive) values (6,0,0,0,%s,1000);',(tpid))
		cursor.execute('commit;')
	return render_template('tadmin.html')
	
	
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8181, debug=True)

