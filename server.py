from flask import Flask,render_template, request
import datetime

app=Flask(__name__)
fnames=[]
dates=[]
time_slots=[]
directions=[]
all_bookings=[]
showall_bookings=[]

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
    booking=(date,time_slot,direction)

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
        if(booking1==(date1,slot1,direction1)):
            showall_bookings.append(booking1)
    print(showall_bookings)
    return render_template('index.html',bookings_list_in_html=showall_bookings)
@app.route("/cabservices")
def cabservices():
    return render_template('cabservices.html')

@app.route("/about")
def about():
    return render_template('about.html')

    