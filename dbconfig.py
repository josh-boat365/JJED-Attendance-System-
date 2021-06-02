import sqlite3

class DB():

    def __init__(self):
        # self.query = query
        self.con = sqlite3.connect("jjed.db")
        self.cur = self.con.cursor()


    def select(self,tb_name,name,email):
        self.cur.execute("SELECT * FROM {} WHERE intern_name=? AND intern_email=?".format(tb_name), (name,email))
        data = self.cur.fetchall()
        return data[0][1]

    def authentication(self,tb_name,col_name1,data1,col_name2,data2):
        self.cur.execute("SELECT * FROM {} WHERE {}=? AND {}=?".format(tb_name,col_name1,col_name2), (data1,data2))
        data = self.cur.fetchall()
        if len(data) > 0:
            return True
        return False
    

    def present(self,tb_name,attendance_bool,intern_name,btn_checked):
        is_present =False
        if btn_checked == "checked":
            is_present = True
            self.cur.execute("INSERT INTO {}({})VALUES(?) WHERE {}=?".format(tb_name,attendance_bool),(is_present,intern_name))
            self.con.commit()
            return True
        return is_present

    # def authentication(self,tb_name,col_name1,data1,col_name2,data2):
    #     try:
    #         self.cur.execute("SELECT * FROM {} WHERE {}=? AND {}=?".format(tb_name,col_name1,col_name2), (data1,data2))
    #         data = self.cur.fetchall()
    #         name = data[0][1]
    #         access_key = data[0][5]
    #         if name == data1 and access_key == data2:
    #             return True
    #     except IndexError:
    #         return False
    #     return False
        # lets change the intern email to contact to access the system
        # and rearrange the table such that we name and contact is at index 1 and 2




    def select_all(self,tb_name):
        self.cur.execute("SELECT * FROM {}".format(tb_name))
        data = self.cur.fetchall()
        return data

    def insert(self,tb_name,col_name1,col_name2,data1,data2):
        self.cur.execute("INSERT INTO {}({},{})VALUES(?,?)".format(tb_name,col_name1,col_name2),(data1,data2))
        self.con.commit()
        return True

    def insert_all(self,tb_name,data):
        self.cur.executemany("INSERT INTO {}(intern_name, intern_school,intern_level,intern_contact,intern_email) VALUES(?,?,?,?,?)".format(tb_name), data)
        self.con.commit()
        return True
        # INSERT INTO interns(intern_name, intern_school,intern_level,intern_contact,intern_email)VALUES(?,?,?,?,?)
    
    def insert_intern(self,tb_name,name_data,school_data, level_data,contact_data, email_data):
        self.cur.execute("INSERT INTO {}(intern_name,intern_school,intern_level,intern_contact,intern_email)VALUES(?,?,?,?,?)".format(tb_name),(name_data,school_data, level_data,contact_data, email_data))
        self.con.commit()
        return True


# to do
# admin should be able to add csv list of interns and it will be converted to a list of tuples and added to the db
    def csv(self,file_path):
        intern_data = []
        file = open(file_path,"r")
        for line in range(len(file)):
            intern_data.append((file[line+1])) #line+1 is avoiding column title
        return self.insert_all(intern_data)

    
    def update(self,tb_name,col2_change,value, col_id, data_id):
        self.cur.execute("UPDATE {} SET {}=? WHERE {}=?".format(tb_name,col2_change,col_id), (value,data_id))
        self.con.commit()
        return True

    def delete_one(self,tb_name,data_id):
        self.cur.execute("DELETE FROM {} WHERE activity_id=?".format(tb_name), (data_id,))
        self.con.commit()
        return True
        
    def delete_rows(self,tb_name):
        self.cur.execute("DELETE FROM {}".format(tb_name))
        self.con.commit()
        return True
    
   

if __name__ =="__main__":
    db = DB()
    # b = db.select("interns", "Enoch Sem","enochsem@gmail.com")
    # print(b)
    # r=db.authentication("interns", "intern_name", "Enoch Sem", "intern_email", "enochsem@gmail.com")
    # print(r)

    # s = db.insert("activities","activity_title","activity_content", "Activity", "Git and Github as a distributed version control system by Sam")
    # print(s)

    db.delete_rows("activities")