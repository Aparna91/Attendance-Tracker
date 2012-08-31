#!/usr/bin/python

import tracker
import settt
import course
import assignment
import gtk
from datetime import date

class  Main:

    def __init__(self):
        filename = "Mainwindow.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(filename)
        self.d = self.builder.get_object("dialog1")
    	q = self.builder.get_object("button1")
    	q.connect("clicked",self.show)
    	w = self.builder.get_object("button2")
    	w.connect("clicked",gtk.main_quit)
    	x = self.builder.get_object("button66")
    	x.connect("clicked",self.refresh)
    	
    	
    	z = self.builder.get_object("calendar1")
    	z.connect("next_month",self.change1)
    	z.connect("prev_month",self.change1)
        z.connect("day_selected_double_click",self.open1)
    	
    	d = z.get_date()
    	d = list(d)
  	d1 = "/"+str(d[1])+"/"
    	tracker.t3.getall("DueDate glob '*%s*'"%(str(d1)))
    	for c in tracker.t3.str4:
    		a = list(c)
    		getday = a[3][0:2]
    		if (getday[1]=='/'):
    			getday = getday[0]
  		z.mark_day(int(getday))
    	
    	
    	
    	for i in range(63):
    		b = self.builder.get_object("button%s"%(i+3))
    		b.connect("clicked",self.coursedet)
    		
    	tracker.t1.get("Id = 1")
        if tracker.t1.str1 is not None:
        	text = ['','','','','','','']
		for k in range (9):
			i = k+3
			tracker.t1.get("Id = %s"%(k+1))
			list1 = list(tracker.t1.str1)
				
			j = 0
			for j in range(7):
				text[j] = list1[j+1]
    			
    			j = 0	
    			for j in range(7):
    				query = "button%s"%(str(i))
    				b = self.builder.get_object(query)
    				b.set_label(text[j])
    				i = i+9
	
	day = date.today()
	day = str(day)
	day = list(day)
	if str(day[5])== "0":
		day[6] = str(int(day[6])-1)
		date1 = "\'"+str(day[8])+str(day[9])+"/"+str(day[6])+"/"+str(day[0])+str(day[1])+str(day[2])+str(day[3])+"\'"
	elif day[5] == "1" and day[6] == "0":
		day[5] = "0"
		day[6] = "9"
		date1 = "\'"+str(day[8])+str(day[9])+"/"+str(day[6])+"/"+str(day[0])+str(day[1])+str(day[2])+str(day[3])+"\'"
	elif day[5] == "1":
		day[6] == str(int(day[6])-1)
		date1 = "\'"+str(day[8])+str(day[9])+"/"+str(day[5])+str(day[6])+"/"+str(day[0])+str(day[1])+str(day[2])+str(day[3])+"\'"
	print date1
	tracker.t3.get("DueDate = %s"%(str(date1)))
	print tracker.t3.str1
	if tracker.t3.str1 is not None:
		self.builder.get_object("label").set_label("ASSIGNMENT DUE FOR TOMORROW !!!") 
	    				
        
    def open1(self,widget):
    	d = widget.get_date()    
    	d1 = list(d)
    	date = str(d1[2])+"/"+str(d1[1])+"/"+str(d1[0])
        a = assignment.Assignment(str(date))
        a.display()
        
        
    def show(self,widget):
    	settt.a.display()
    	
    def coursedet(self,widget):
    	c = course.CourseDet(widget.get_label())
	c.display()
    	
    def refresh(self,widget):
    	self.d.hide_all()
    	gtk.main_quit()
    	b = Main()
    	b.display()


    def display(self):
    	self.d.show_all()
    	gtk.main()


    def change1(self,widget):
	widget.clear_marks()
	d = widget.get_date()
    	d = list(d)
  	d1 = "/"+str(d[1])+"/"
    	tracker.t3.getall("DueDate glob '*%s*'"%(str(d1)))
    	for c in tracker.t3.str4:
    		a = list(c)
    		getday = a[3][0:2]
    		if (getday[1]=='/'):
    			getday = getday[0]
  		widget.mark_day(int(getday))
	widget.thaw()


m = Main()
m.display()
