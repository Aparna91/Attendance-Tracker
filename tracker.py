#!/usr/bin/python

import Tkinter
import sqlite3
import types
import globals

		
class Table:
	
	def __init__(self, conn, tbl_name):
		self.conn = sqlite3.connect(globals.db_path)
		self.cursor = self.conn.cursor()
		self.tbl_name = tbl_name
		
	def insert1(self,t1):
		query = "insert into %s ('Mon','Tue','Wed','Thu','Fri','Sat','Sun') values %s"%(self.tbl_name,str(t1))
		self.cursor.execute(query)
		self.conn.commit()
		
	def insert2(self,t1):
		query = "insert into %s ('SlotId','CourseId') values %s"%(self.tbl_name,str(t1))
		self.cursor.execute(query)
		self.conn.commit()
	
	def insert3(self,t1):
		query = "insert into %s ('CourseId','Title','DueDate','Desc') values %s"%(self.tbl_name,str(t1))
		self.cursor.execute(query)
		self.conn.commit()	

	def insert4(self,t1):
		query = "insert into %s ('CourseId','CourseName','ProfName','RoomNo','Credits') values %s"%(self.tbl_name,str(t1))
		self.cursor.execute(query)
		self.conn.commit()
	
	def insert5(self,t1):
		query = "insert into %s ('SlotId','Date') values %s"%(self.tbl_name,str(t1))
		self.cursor.execute(query)
		self.conn.commit()
		
	def update(self, id_, **kwargs):
		updations = []
		for (k,v) in kwargs.items():
			k = str(k)
			if type(v) == str:
				updations.append( '%s = "%s"'%(k,v))
			else:
				updations.append( '%s = %s'%(k,str(v)))
			
		update_values = ' ,'.join(updations)
		print update_values
		query = 'update %s set %s where Id = %d'%(self.tbl_name,update_values,id_)
		print query
		self.cursor.execute(query)
		self.conn.commit()
	
	def remove(self, id_): 
		self.cursor.execute('delete from %s where Id = (%s)'%(self.tbl_name,id_))
		self.conn.commit()
	
	def get(self, conditions):
		query = 'select * from %s where %s'%(self.tbl_name,str(conditions))
		#print query
		self.cursor.execute(query)
		self.str1 = self.cursor.fetchone()
		self.conn.commit()
		
	def count(self,conditions):
		self.cursor.execute('select count(*) from %s group by %s'%(self.tbl_name,conditions))
		self.ct = self.cursor.fetchone()
		self.conn.commit()
		
	def join(self,tbl_name2,com_col,check_col,value):
		self.cursor.execute('select * from %s,%s where %s.%s = %s.%s and %s = %s'%(self.tbl_name, tbl_name2, self.tbl_name, com_col, tbl_name2, com_col, check_col, value))
		self.str2 = self.cursor.fetchone()
		self.conn.commit()
		
		
class TimeTable(Table):

	def insert(self, mon = "", tue = "", wed = "", thu = "", fri = "", sat = "", sun = ""):
		Table.insert1(self,(mon,tue,wed,thu,fri,sat,sun))

	def remove(self, id_):
		Table.remove(self, id_)
		
	def update(self, id_, **kwargs):
		Table.update(self, (id_), **kwargs)
		
	def get(self, conditions):
		Table.get(self, conditions)
		
	def count(self,conditions):
		Table.count(self,conditions)
		
	def join(self,tbl_name2,com_col,check_col,value):
		Table.join(self,tbl_name2,com_col,check_col,value)
				
class SlotMap(Table):
	
	def insert(self, slot_id, course_id):
		Table.insert2(self, (slot_id, course_id))
		
	def remove(self, id_):
		Table.remove(self, id_)
		
	def update(self, id_, **kwargs):
		Table.update(self, id_, **kwargs)
		
	def get(self, conditions):
		Table.get(self, conditions)
		
	def count(self,conditions):
		Table.count(self,conditions)
		
	def join(self,tbl_name2,com_col,check_col,value):
		Table.join(self,tbl_name2,com_col,check_col,value)	
	
class Assignment(Table):

	def insert(self, course_id, title, duedate, desc):
		Table.insert3(self, (course_id, title, duedate, desc))
		
	def remove(self, id_):
		Table.remove(self, (id_))
	
	def remove1(self, date):
		query = 'delete from %s where DueDate = %s'%(self.tbl_name,str(date))
		print query
		self.cursor.execute(query)
		print "Removed"
		self.conn.commit()
	
	def update(self, id_, **kwargs):
		Table.update(self, id_, **kwargs)
		
	def get(self, conditions):
		Table.get(self, conditions)
		
	def getall(self,conditions):
		self.cursor.execute('select * from %s where %s' %(self.tbl_name,conditions))
		self.str4 = self.cursor.fetchall()
		self.conn.commit()
		
	def count(self,conditions):
		Table.count(self,conditions)
	
	def join(self,tbl_name2,com_col,check_col,value):
		Table.join(self,tbl_name2,com_col,check_col,value)
	
class CourseDetails(Table):

	def insert(self, course_id, course_name, prof_name, room_no, credits):
		Table.insert4(self, (course_id, course_name, prof_name, room_no, credits))
		
	def remove(self, id_):
		Table.remove(self, (id_))
		
	def update(self, id_, **kwargs):
		Table.update(self, id_, **kwargs)
			
	def get(self, conditions):
		Table.get(self, conditions)
		
	def count(self,conditions):
		Table.count(self,conditions)
	
	def join(self,tbl_name2,com_col,check_col,value):
		Table.join(self,tbl_name2,com_col,check_col,value)
		
class Absences(Table):

	def insert(self, slot_id, date):
		Table.insert5(self,(slot_id, date))
		
	def remove1(self, date, slot_name):
		date1 = '\'' + date + '\''
		name = '\'' + slot_name + '\''
		query = 'delete from %s where Date = %s and SlotId = %s'%(self.tbl_name,str(date1),str(name))
		print query
		self.cursor.execute(query)
		print "Removed"
		self.conn.commit()
	
	def get(self,conditions):
		Table.get(self,conditions)
		
	def getall(self,conditions):
		self.cursor.execute('select * from %s where %s' %(self.tbl_name,conditions))
		self.str3 = self.cursor.fetchall()
		self.conn.commit()
		
	def count(self,conditions):
		Table.count(self,conditions)
	
	def join(self,tbl_name2,com_col,check_col,value):
		Table.join(self,tbl_name2,com_col,check_col,value)	
		
t1 = TimeTable("conn", "TimeTable")

t2 = SlotMap("conn", "SlotMap")

t3 = Assignment("conn", "Assignment")

t4 = CourseDetails("conn", "Coursedet")

t5 = Absences("conn", "Absences")

			
