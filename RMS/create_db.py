import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY,name text,duration text,charges text,description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY,name text,email text,gender text,dob text,contact text,addmission text,course text,state text,city text,pin,address)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()
    con.close()

create_db()    
    