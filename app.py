from flask import Flask,flash,redirect,render_template,request
from queries import *
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login (2).html')

@app.route('/home')
def home():
    return render_template('home (2).html')

@app.route('/basketball')
def basketball():
    return render_template('basketball.html')

@app.route('/gallery')
def gallery():
    return render_template('GALLERY.html')

@app.route('/register')
def register():
    return render_template('REGISTER.html')

#@app.route('/cricket')
#def cricket():
   # return render_template('MC.html')

@app.route('/throwball')
def throwball():
    return render_template('throwball.html')

@app.route('/volleyball')
def volleyball():
    return render_template('volleyball.html')

@app.route('/football')
def football():
    return render_template('football.html')

@app.route('/admin')
def admin():
    return render_template('admin (2).html')

@app.route('/check')
def check():
    return render_template('CHECK MEMBER.html')

@app.route('/delete')
def delete():
    return render_template('DELETE MEMBER.html')

@app.route('/add_event')
def add():
    return render_template('Add Event.html')

@app.route('/add_ach')
def add_achievements():
    return render_template('Add achievements.html')

@app.route('/logout_ad')
def logout_admin():
    return render_template('home (2).html')

@app.route('/achievements')
def ach_page():
    return render_template('Achievements (1).html')



#verify login page

@app.route('/verify', methods = ['GET','POST'])
def verify():
    if request.method == 'POST':
        usn = request.form['usn']
        x = check_login(usn)
        if x == 'yes':
            return render_template('home (2).html')
        else:
            return render_template('verify.html')

#verify registering
    
@app.route('/verify1', methods = ['GET','POST'])
def get_home():
    if request.method == 'POST':
        name = request.form['name']
        usn = request.form['usn']
        year = request.form['year']
        gender = request.form['gender']
        sports1 = request.form['sports 1']
        sports2 = request.form['sports 2']
        sports3 = request.form['sports 3']
        achievement = request.form['achievement']
        x = register1(name,usn,year,gender,sports1,sports2,sports3,achievement)
        if x == 'yes':
            return render_template('verify1.html')
        else:
            return render_template('home (2).html')

#verify admin login

@app.route('/verify2', methods = ['GET','POST'])
def ad_login():
    if request.method == 'POST':
        user = request.form['uname']
        password = request.form['psw']
        x = admin_login(user,password)
        if x == 'yes':
            return render_template('admin (2) (2).html')
        else:
            return render_template('verify2.html')
#checking and redirecting to add member

@app.route('/addmember', methods = ['GET','POST'])
def check_member():
    if request.method == 'POST':
        usn = request.form['usn']
        x = member(usn)
        return render_template('Add member.html', result = x)

#member added
@app.route('/verify6', methods = ['GET','POST'])
def addmember():
    if request.method == 'POST':
        usn = request.form['usn']
        sports1 = request.form['sports1']
        sports2 = request.form['sports2']
        sports3 = request.form['sports3']
        add_member(usn,sports1,sports2,sports3)
        return render_template('admin (2) (2).html')

#delete member
@app.route('/verify3', methods = ['GET','POST'])
def delete1_member():
    if request.method == 'POST':
        usn = request.form['usn']
        delete1(usn)
        return render_template('admin (2) (2).html')


#add event

@app.route('/verify4', methods = ['GET','POST'])
def add_event():
    if request.method == 'POST':
        name = request.form['name']
        sport = request.form['sport']
        date = request.form['date']
        venue = request.form['venue']
        add1(name,sport,date,venue)
        return render_template('admin (2) (2).html')

@app.route('/verify5', methods = ['GET','POST'])
def add_ach():
    if request.method == 'POST':
        eventid = request.form['name']
        position = request.form['position']
        x = achievement(eventid,position)
        if x == 'no':
            return render_template('verify7.html')
        else:
            return render_template('admin (2) (2).html')

@app.route('/updateyear')
def update():
    #upd_trigger()
    upyear()
    del_passout()
    return render_template('admin (2) (2).html')


#view ach
@app.route('/viewach', methods = ['GET','POST'])
def ach():
    #del_view_ach()
    #create_view_ach()
    x = view_ach()
    return render_template('viewach.html', result = x)

#view event
@app.route('/viewev', methods = ['GET','POST'])
def ev():
    #del_view_event()
    #create_view_event()
    x = view_event()
    return render_template('View_events.html', result = x)

#view members
@app.route('/view_members', methods = ['GET','POST'])
def vm():
    x = members()
    return render_template('mem.html', result = x)

#view registered
@app.route('/view_registered', methods = ['GET','POST'])
def vr():
    x = registered()
    return render_template('reg_students.html', result = x)


#budding star
@app.route('/buddingstar', methods = ['GET','POST'])
def budding():
   x = buddingstar()
   return render_template('budding men.html', result = x)

#upcoming
@app.route('/upcoming', methods = ['GET','POST'])
def upcoming_event():
    x = upcoming()
    return render_template('UPCOMING EVENTS.html', result = x)

#total achievers
@app.route('/totalach', methods = ['GET','POST'])
def total_ach():
    x = achiever()
    return render_template('TOTAL ACHIEVERS.html', result = x)

#women achievers
@app.route('/womenach', methods = ['GET','POST'])
def women_ach():
    x = womenach()
    return render_template('women achievers.html', result = x)

#basketball achievers
@app.route('/basketballach', methods = ['GET','POST'])
def basket_ach():
    x = b_ach()
    return render_template('bbach.html', result = x)

#volleyball achievers
@app.route('/volleyballach', methods = ['GET','POST'])
def volley_ach():
    x = v_ach()
    return render_template('voach.html', result = x)

#cricket achievers
@app.route('/cricketach', methods = ['GET','POST'])
def cricket_ach():
    x = c_ach()
    return render_template('crach.html', result = x)

#football achievers
@app.route('/footballach', methods = ['GET','POST'])
def football_ach():
    x = f_ach()
    return render_template('fbach.html', result = x)

#throwball achievers
@app.route('/throwballach', methods = ['GET','POST'])
def throwball_ach():
    x = t_ach()
    return render_template('thach.html', result = x)


#basketball 
@app.route('/mbb', methods = ['GET','POST'])
def mbb():
    x = mbasketball()
    return render_template('MB.html', result = x)

@app.route('/fbb', methods = ['GET','POST'])
def fbb():
    x = fbasketball()
    return render_template('FB.html', result = x)

#cricket
@app.route('/cricket', methods = ['GET','POST'])
def mcc():
    x = mcricket()
    return render_template('MC.html', result = x )

#football 
@app.route('/mfb', methods = ['GET','POST'])
def mfb():
    x = mfootball()
    return render_template('MF.html', result = x)

@app.route('/ffb', methods = ['GET','POST'])
def ffb():
    x = ffootball()
    return render_template('FF.html', result = x)

#volleyball 
@app.route('/mvb', methods = ['GET','POST'])
def mvb():
    x = mvolleyball()
    return render_template('MV.html', result = x)

@app.route('/fvb', methods = ['GET','POST'])
def fvb():
    x = fvolleyball()
    return render_template('FV.html', result = x)

#throwball 
@app.route('/mtb', methods = ['GET','POST'])
def mtb():
    x = mthrowball()
    return render_template('MT.html', result = x)

@app.route('/ftb', methods = ['GET','POST'])
def ftb():
    x = fthrowball()
    return render_template('FT.html', result = x)

