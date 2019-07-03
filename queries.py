import pymysql


#open database connection 
def connect():
    db = pymysql.connect("localhost","root","password","sports")
    curr = db.cursor()
    return db,curr
#creation of tables
def create():
    db,curr=connect()
    curr.execute("create table admin(user varchar(15) primary key, name varchar(20) not null, password varchar(10) not null)")
    curr.execute("create table student(usn varchar(15) primary key, name varchar(40) not null, year int not null, gender char(1) not null, sports varchar(60) not null, member varchar(4) default 'no',p_achievements varchar(40))")
    curr.execute("create table passout(usn varchar(15) not null, name varchar(40) not null,gender char(1) not null, sport varchar(40) not null)")
    curr.execute("create table event(event_id int primary key auto_increment, event_name varchar(20) not null, sport varchar(20) not null, date date not null, venue varchar(20) not null)")
    curr.execute("create table achievements(event_id primary key, position int not null, foreign key (event_id) references event(event_id))")
    db.commit()
    db.close()

#insertion 
def insert():
    db,curr=connect()
    curr.execute("insert into table student values(%s,%s,%s,%s,%s)", ("4ni16cs101","shruti",2016,"football","yes"))

#authenticating the user
def check_login(usn):
    db,curr=connect()
    curr.execute("select * from student where usn = %s", (str(usn)))
    data = curr.fetchall()
    curr.execute("select * from admin where user = %s", (str(usn)))
    data1 = curr.fetchall()
    if (data):
        return 'yes'
    else:
        if (data1):
            return 'yes'

   
        
    db.close()

#registering user
def register1(name,usn,year,gender,sports1,sports2,sports3,achievement):
    db,curr=connect()
    curr.execute("select * from student where usn = %s", (str(usn)))
    data = curr.fetchall()
    if (data):
        db.close()
        return 'yes'
        
    else:
        curr.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)", (str(usn),str(name),str(year),str(gender),str(sports1+' '+sports2+' '+sports3),'no',str(achievement)))
        db.commit()
        db.close()

#authenticating admin login
def admin_login(user,password):
    db,curr=connect()
    curr.execute("select * from admin where user=%s and password=%s", (str(user),str(password)))
    data = curr.fetchall()
    if (data):
        db.close()
        return 'yes'
    else:
        db.close()
        return 'no'




#checking member
def member(usn):
    db,curr=connect()
    curr.execute("select usn,name,sports from student where usn=%s and member='yes'", (str(usn)))
    data = curr.fetchall()
    db.close()
    return data
    
#adding member
def add_member(usn,sports1,sports2,sports3):
    db,curr=connect()
    curr.execute("update student set member='yes',sports=%s where usn = %s", (str(sports1+' '+sports2+' '+sports3),str(usn)))
    db.commit()
    db.close()

# deleting member
def delete1(usn):
    db,curr=connect()
    curr.execute("delete from student where usn=%s", (str(usn)))
    data = curr.fetchall()
    db.commit()
    db.close()


#add_event
def add1(name,sport,date,venue):
    db,curr=connect()
    curr.execute("insert into event(event_name,sport,date,venue)values(%s,%s,%s,%s)", (str(name),str(sport),str(date),str(venue)))
    data = curr.fetchall()
    db.commit()
    db.close()

#add_achievement
def achievement(eventid,position):
    db,curr=connect()
    curr.execute("select * from event where event_id=%s", (str(eventid)))
    data = curr.fetchall()
    if(data):
        curr.execute("insert into achievements values(%s,%s)",(str(eventid),str(position)))
        data = curr.fetchall()
        db.commit()
        db.close()
        return 'yes'
    else:
        return 'no'


#update year
def upyear():
    db,curr=connect()
    curr.execute("update student set year=year+1")
    data = curr.fetchall()
    db.commit()
    db.close()


#trigger for update year
def upd_trigger():
    db,curr=connect()
    curr.execute("create trigger bye before update on student for each row begin if new.year > 4 then insert into passout values(NEW.usn,NEW.name,NEW.gender,NEW.sports);end if;end;")
    
    db.commit()
    db.close()

#delete passout from student
def del_passout():
    db,curr=connect()
    curr.execute("delete from student where year > 4")
    db.commit()
    db.close()

#creating view of achievement table
def create_view_ach():
    db,curr=connect()
    curr.execute("create view ach as select event_name,sport,date,venue,position from event,achievements where achievements.event_id=event.event_id")
    db.commit()
    db.close()

#delete view achievement
def del_view_ach():
    db,curr=connect()
    curr.execute("drop view ach")
    db.commit()
    db.close()

#view achievements
def view_ach():
    db,curr=connect()
    curr.execute("select * from ach")
    data = curr.fetchall()
    db.close()
    return data

#check members
def members():
    db,curr=connect()
    curr.execute("select usn,name,year,gender,sports from student where member='yes'")
    data = curr.fetchall()
    db.close()
    return data

#check registered
def registered():
    db,curr=connect()
    curr.execute("select * from student")
    data = curr.fetchall()
    db.close()
    return data

#create view of event table
def create_view_event():
    db,curr=connect()
    curr.execute("create view ev as select event_id,event_name,sport,venue,date from event")
    db.commit()
    db.close()

#view event
def view_event():
    db,curr=connect()
    curr.execute("select * from ev")
    data = curr.fetchall()
    db.close()
    return data

#delete view event
def del_view_event():
    db,curr=connect()
    curr.execute("drop view ev")
    db.commit()
    db.close()

#budding star
def buddingstar():
    db,curr=connect()
    curr.execute("select name,sports from student where year=1 and member='YES'")
    data = curr.fetchall()
    db.close()
    return data

#upcoming
def upcoming():
    db,curr=connect()
    curr.execute("select event_name,sport,venue,date from event where date > curdate()")
    data = curr.fetchall()
    db.close()
    return data

#total ach
def achiever():
    db,curr=connect()
    curr.execute("select count(usn) from student where p_achievements='DISTRICT' or p_achievements='NATIONAL' or p_achievements='STATE'")
    data = curr.fetchall()
    db.commit()
    db.close()
    return data

#women ach
def womenach():
    db,curr=connect()
    curr.execute("select name,year,p_achievements from student where gender='F'and (p_achievements='DISTRICT' OR p_achievements='STATE' or p_achievements='NATIONAL') order by name asc")
    data = curr.fetchall()
    db.close()
    return data

#basketball ach
def b_ach():
    db,curr=connect()
    curr.execute("select e.event_name,e.sport,e.venue,e.date,a.position from event e, achievements a where e.event_id=a.event_id and e.sport='BASKETBALL'")
    data = curr.fetchall()
    db.close()
    return data

#volleyball ach
def v_ach():
    db,curr=connect()
    curr.execute("select e.event_name,e.sport,e.venue,e.date,a.position from event e, achievements a where e.event_id=a.event_id and e.sport='VOLLEYBALL'")
    data = curr.fetchall()
    db.close()
    return data

#cricket ach
def c_ach():
    db,curr=connect()
    curr.execute("select e.event_name,e.sport,e.venue,e.date,a.position from event e,achievements a where e.event_id=a.event_id and e.sport='CRICKET'")
    data = curr.fetchall()
    db.close()
    return data

#football ach
def f_ach():
    db,curr=connect()
    curr.execute("select e.event_name,e.sport,e.venue,e.date,a.position from event e,achievements a where e.event_id=a.event_id and e.sport='FOOTBALL'")
    data= curr.fetchall()
    db.close()
    return data

#throwball ach
def t_ach():
    db,curr=connect()
    curr.execute("select e.event_name,e.sport,e.venue,e.date,a.position from event e,achievements a where e.event_id=a.event_id and e.sport='THROWBALL'")
    data = curr.fetchall()
    db.close()
    return data


#basketball
def mbasketball():
    db,curr=connect()
    #curr.execute("drop procedure MB")
    #curr.execute("create procedure MB () select usn,name,year from student where member='YES'and sports like '%BASKETBALL%'and gender='M'")
    curr.execute("call MB()")
    data = curr.fetchall()
    db.commit()
    db.close()
    return data

def fbasketball():
    db,curr=connect()
    #curr.execute("drop procedure FB")
    #curr.execute("create procedure FB () select usn,name,year from student where member='YES' and sports like '%BASKETBALL%' and gender='F'")
    curr.execute("call FB()")
    data = curr.fetchall()
    db.commit()
    db.close()
    return data

#cricket
def mcricket():
    db,curr=connect()
    #curr.execute("drop procedure MC")
    #curr.execute("create procedure MC () select usn,name,year from student where member='YES' and sports like '%CRICKET%' and gender='M'")
    curr.execute("call MC()")
    data = curr.fetchall()
    db.commit()
    db.close()
    return data

#football
def mfootball():
    db,curr=connect()
    #curr.execute("drop procedure MF")
    #curr.execute("create procedure MF () select usn,name,year from student where member='YES' and sports like '%FOOTBALL%' and gender='M'")
    curr.execute("call MF()")
    data = curr.fetchall()
    db.commit()
    db.close()
    return data

def ffootball():
    db,curr=connect()
    #curr.execute("drop procedure FF")
    #curr.execute("create procedure FF () select usn,name,year from student where member='YES' and sports like '%FOOTBALL%' and gender='F'")
    curr.execute("call FF()")
    data = curr.fetchall()
    db.commit()
    db.close()
    return data

#volleyball
def mvolleyball():
    db,curr=connect()
    #curr.execute("drop procedure MV")
    #curr.execute("create procedure MV () select usn,name,year from student where member='YES' and sports like '%VOLLEYBALL%' and gender='M'")
    curr.execute("call FF()")
    data = curr.fetchall()
    db.commit()
    db.close()
    return data

def fvolleyball():
    db,curr=connect()
    #curr.execute("drop procedure FV")
    #curr.execute("create procedure FV () select usn,name,year from student where member='YES' and sports like '%VOLLEYBALL%' and gender='F'")
    curr.execute("call FV()")
    data = curr.fetchall()
    db.commit()
    db.close()
    return data

#throwball
def mthrowball():
    db,curr=connect()
    #curr.execute("drop procedure MT")
    #curr.execute("create procedure MT () select usn,name,year from student where member='YES' and sports like '%THROWBALL%' and gender='M'")
    curr.execute("call MT()")
    data = curr.fetchall()
    db.commit()
    db.close()
    return data

def fthrowball():
    db,curr=connect()
    #curr.execute("drop procedure FT")
    #curr.execute("create procedure FT () select usn,name,year from student where member='YES' and sports like '%THROWBALL%' and gender='F'")
    curr.execute("call FT()")
    data = curr.fetchall()
    db.commit()
    db.close()
    return data
