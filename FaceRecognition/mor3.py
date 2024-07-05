import sqlite3
import datetime
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('mor3.db')
        self.cur = self.conn.cursor()
    def drop_create(self):
        self.cur.execute("drop table employee")
        self.cur.execute("CREATE TABLE employee(emp_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT(40) NOT NULL,position TEXT(30) NOT NULL,status INTEGER DEFAULT 1 )")
        """

        -------------------EMPLOYEE-------------
        |---------------|-----------|----------------|-------------|
        |   emp_id      |   name    |    position    |   status    |
        |_______________|___________|________________|_____________|


        """
        self.cur.execute("drop table attendance")
        self.cur.execute("create table attendance(date_ date not null,   emp_id integer not null,   in_time time not null,   out_time time)")
        """

        -------------------ATTENDANCE-------------
        |---------------|-----------|----------------|-------------|
        |   date_       |   emp_id  |    in_time     |   out_time  |
        |_______________|___________|________________|_____________|


        """
        self.conn.commit()
    def attendance_insert(self,emp_id):
        self.cur.execute("select * from attendance where date_=DATE('now') AND emp_id="+str(emp_id))
        data = self.cur.fetchall()
        if len(data)==0:
            self.cur.execute("insert into attendance(date_,emp_id,in_time) values(DATE('now'),"+str(emp_id)+",TIME('now'))")
            self.conn.commit()
            return 1 #------------------------------"now in"
        else:
            data = data[0]
            if(data[2] and  not data[3]):
                self.cur.execute("update attendance set out_time=TIME('now') where date_=DATE('now') AND emp_id= "+str(emp_id))
                self.conn.commit()
                return 0    #-----------------------"now out"
            elif(data[2] and data[3]):
                return -1      #--------------------"already out"
    def employee_attendance(self,emp_id):
        self.cur.execute("SELECT date_,in_time,out_time from ATTENDANCE where emp_id="+str(emp_id))
        data = self.cur.fetchall()
        i=0
        for day in data:
            data[i]=data[i]+(datatime.strptime(str(day[1]),"%H:%M:%S")-datatime.strptime(str(day[2]),"%H:%M:%S").total_seconds(),)
            i+=1
        return data
    def employee_add(self,name,position,status=1):
        self.cur.execute("insert into employee(name,position,status) values('"+name+"','"+position+"','"+str(status)+"')")
        id_=self.cur.execute("select * from employee").fetchall()[-1][0]
        self.conn.commit()
        return id_
    def employee_disable(self,emp_id):
        self.cur.execute("UPDATE employee SET status=0 where emp_id="+str(emp_id))
        self.conn.commit()
        return True
    def employee_update(self,emp_id,position):
        self.cur.execute("UPDATE employee SET position="+str(position)+" where emp_id="+str(emp_id))
        self.conn.commit()
        return True
    def attendance_remove(self,emp_id):
        self.cur.execute("DELETE from attendance where date_=DATE('now') AND emp_id="+str(emp_id))
        self.conn.commit()
    def employee_enable(self,emp_id):
        self.cur.execute("UPDATE employee SET status=1 where emp_id="+str(emp_id))
        self.conn.commit()
    def query(self,query):
        obj = self.cur.execute(str(query))
        self.conn.commit()
        return obj
    def find_name(self,emp_id):
        #self.cur.execute("SELECT name from EMPLOYEE where emp_id="+str(emp_id))
        emp_name=self.cur.execute("SELECT * from EMPLOYEE where emp_id="+str(emp_id)).fetchall()[-1][1]
        self.conn.commit()
        return emp_name
    def employee_status(self,emp_id):
        self.cur.execute("SELECT in_time,out_time from attendance where emp_id="+str(emp_id)+" AND date_ =DATE('now')")
        fetch=self.cur.fetchall()
        if len(fetch) == 0:
            return -1    #--------------------------hasnt yet come
        else:
            if not fetch[0][1]:
                return 1   #-----------------------working now
            else:
                return 0    #-----------------------got out
    def employee_details(self,emp_id):
        #self.cur.execute("SELECT  from EMPLOYEE where emp_id="+str(emp_id))
        execute=self.cur.execute("SELECT name,position from EMPLOYEE where emp_id="+str(emp_id)).fetchall()[0]
        emp_name,position=execute[0],execute[1]
        self.conn.commit()
        return (emp_name,position)        
    def employee_fetch(self):
        data={"sno":[],"id":[],"name":[],"position":[],"in":[],"out":[],"status":[]}
        self.cur.execute("select * from employee where status='1'")
        i=1
        for row in self.cur.fetchall():
            data["sno"].append(i)
            data["id"].append(row[0])
            data["name"].append(row[1])
            data["position"].append(row[2])
            i+=1
            self.cur.execute("select in_time,out_time from attendance where date_=DATE('now') AND emp_id="+str (row[0]))
            in_out=self.cur.fetchall()
            if len(in_out)==0:
                data["in"].append(None)
                data["out"].append(None)
            else:
                for in_,out in in_out:
                    data["in"].append(in_)
                    data["out"].append(out)
            data["status"].append(self.employee_status(row[0]))
            """
                for row in self.cur.fetchall():
                    for id_ in data["id"]:
                        if id_==row[1]:
                            data["in"].append(row[2])
                            print(row[2])
                            data["out"].append(row[3])
                            print(row[3])
                            data["status"].append(self.employee_status(id_))            
            """
        return data
    def __del__(self):
        self.conn.close()
