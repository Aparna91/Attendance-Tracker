#!/usr/bin/python

import tracker
import gtk
from time import sleep

class CourseDet:

	def __init__(self, slot):
		filename = "coursedet.glade"
        	self.builder = gtk.Builder()
       		self.builder.add_from_file(filename)
        	self.d = self.builder.get_object("dialog1")
        	b2 = self.builder.get_object("button2")
        	b2.connect("clicked",self.save)
        	b1 = self.builder.get_object("button1")
        	b1.connect("clicked",self.destroy)
        	self.slot = slot
        	self.slot1 = "\'"+str(self.slot)+"\'"
        	self.builder.get_object("label9").set_text(str(self.slot))
        	q = self.builder.get_object("calendar1")
    		q.connect("day_selected_double_click",self.toggle)
    		tracker.t5.count("SlotId having SlotId = %s"%(self.slot1))
    		if tracker.t5.ct is not None:
    			self.builder.get_object("label10").set_text(str(tracker.t5.ct))
    		else:
    			self.builder.get_object("label10").set_text("0")
    		q.connect("next_month",self.change1)
    		q.connect("prev_month",self.change1)
    
        	
        	tracker.t2.join("CourseDet","CourseId","SlotId",str(self.slot1))
   
        	if tracker.t2.str2 is not None:
        		text = ['','','','','']
			list1 = list(tracker.t2.str2)
        		# 2,5,6,7,8
        		text[0] = list1[2]
        		text[1] = list1[5]
        		
        		for i in range(3):
        			text[i+2] = list1[i+6]
        		
        		for i in range(5):
    				self.builder.get_object("entry%s"%(str(i+1))).set_text(str(text[i]))
    		
    		d = q.get_date()
    		d = list(d)
  		d1 = str(d[1]+1)
    		tracker.t5.getall("Date glob '*%s*'"%(str(d1)))
    		for c in tracker.t5.str3:
			a = list(c)		
    			if(a[1]==self.slot):
    				getday = a[2][0:2]
    				if (getday[1]=='/'):
    					getday = getday[0]
  				q.mark_day(int(getday))
    			
	def change1(self,widget):
		widget.clear_marks()
		d = widget.get_date()
    		d = list(d)
  		d1 = "/"+str(d[1]+1)+"/"
    		tracker.t5.getall("Date glob '*%s*'"%(str(d1)))
    		for c in tracker.t5.str3:
			a = list(c)		
    			if(a[1]==self.slot):
    				getday = a[2][0:2]
    				if (getday[1]=='/'):
    					getday = getday[0]
  				widget.mark_day(int(getday))
		widget.thaw()
				
	def save(self,widget):
		text = ['','','','','']
		tracker.t2.join("CourseDet","CourseId","SlotId",str(self.slot1))
		for i in range(5):
			text[i] = self.builder.get_object("entry%s"%(str(i+1))).get_text()

		if tracker.t2.str2 is None:
			tracker.t4.insert(text[0],text[1],text[2],text[3],text[4])
			tracker.t2.insert(str(self.slot),text[0])
		else:
			tracker.t2.get("SlotId = %s"%(str(self.slot1)))
			list1 = list(tracker.t2.str1)
			tracker.t2.update(list1[0],CourseId = text[0])
			list1[2] = "\'"+str(list1[2])+"\'"
			tracker.t4.get("CourseId = %s"%(list1[2]))
			list1 = list(tracker.t4.str1)
			tracker.t4.update(list1[0], CourseId = text[0], CourseName = text[1], ProfName = text[2], RoomNo = text[3], Credits = text[4])
			
	def toggle(self,widget):
		day = widget.get_date()	
		list1 = list(day)
		date1 = ""
		date1 = "\'"+str(list1[2])+"/"+str(list1[1]+1)+"/"+str(list1[0])+"\'"
		date = ""
		date = str(list1[2])+"/"+str(list1[1]+1)+"/"+str(list1[0])
		query = "Date = %s and SlotId = %s"%(str(date1),str(self.slot1))
		print query
		tracker.t5.get(query)
		
		print tracker.t5.str1
		
		if tracker.t5.str1 is None:
			tracker.t5.insert(str(self.slot),date)
			widget.mark_day(list1[2])
		else:
			widget.unmark_day(list1[2])
			tracker.t5.remove1(date,str(self.slot))
		self.builder.get_object("label").set_text("Attendance changed")
		#sleep(.5)
		#self.builder.get_object("label").set_text("")
		
				
	def destroy(self,widget):
        	self.d.hide_all()
        	gtk.main_quit()        	
        	
	def display(self):
		self.d.show_all()
		gtk.main()
			
		
		


