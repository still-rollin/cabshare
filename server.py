from flask import Flask,render_template, request
from flask_mail import Mail, Message 
import datetime

app = Flask(__name__)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'cabsharebphc@gmail.com',
    MAIL_PASSWORD = '',
))

mail = Mail(app)
 
fnames=[]
dates=[]
time_slots=[]
directions=[]
all_bookings=[]
showall_bookings=[]
seats=[]
dic={'id':0}
def getnewid():
    dic['id']=dic['id']+1
    return (dic['id'])

@app.route("/")
def hello_world():
    return render_template('index.html', all_bookings=all_bookings)

@app.route("/book") 
def random():
    return render_template('book.html') 
@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/add_booking")
def addbooking():
    fname = request.args.get('fname') 
    fnames.append(fname)
    print(fnames)
    date=request.args.get('trip-start')
    dates.append(date)
    print(dates)
    time_slot=request.args.get('time_slot')
    time_slots.append(time_slot)
    print(time_slots)
    direction=request.args.get('direction')
    directions.append(direction)
    print(directions)
    seat=request.args.get('seat')
    seats.append(seat)
  
    booking=(date,time_slot,direction,seat,getnewid())
   
    
    all_bookings.append(booking)
    print(all_bookings)
    return render_template('index.html', bookings_list_in_html=all_bookings)

@app.route("/filter")
def filter():
    fname1 = request.args.get('fname') 
    print("filtering")
    date1 = request.args.get('trip-start') 
    slot1=request.args.get('time_slot')
    direction1=request.args.get('direction')
    print((fname1,date1,slot1,direction1))
    for booking1 in all_bookings:
        if(booking1[0]==date1 and booking1[1]==slot1 and booking1[2]==direction1):
            showall_bookings.append(booking1)
    print(showall_bookings)
    return render_template('index.html',bookings_list_in_html=showall_bookings)
@app.route("/cabservices")
def cabservices():
    return render_template('cabservices.html')

@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/update")
def update():
    id=request.args.get('val')
    print ("id",id)
    i=0
    for booking in all_bookings:
        print("booking[4]",booking[4])
        if(int(booking[4])==int(id)):

            all_bookings[i]=(booking[0],booking[1],booking[2],int(booking[3])-1,booking[4])
            print(booking[3])
            sendmail(booking)
        i=i+1
    return render_template('index.html',bookings_list_in_html=all_bookings)
def sendmail(booking):
    msg = Message( 
                    'CabShare | New Seat Request ', 
                    sender ='cabsharebphc@gmail.com', 
                    recipients = ["ayaansiddiqui1462@gmail.com"] 
                ) 
    msg.body = "Hello,\nThis email is to inform you that a new seat has been requested for your cab. Details are : \n Direction: " +booking[2]+ " \n Date: " + booking[0] + "\n Time slot: " + booking[1] + "\n Remaining available seats= " +booking[3]+"\n Please contact as per your convenience.\n Best Regards,\n The Cabshare Team"
    mail.send(msg) 
    return 'Sent'

if __name__ == '__main__': 
    app.run(debug = True) 
