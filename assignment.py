#!/usr/bin/python

import tracker
import gtk

class Assignment:

	def __init__(self, date):
		filename = "assignment.glade"
        	self.builder = gtk.Builder()
       		self.builder.add_from_file(filename)
        	self.d = self.builder.get_object("dialog1")
        	b2 = self.builder.get_object("button1")
        	b2.connect("clicked",self.save)
        	b1 = self.builder.get_object("button2")
        	b1.connect("clicked",self.destroy)
        	self.date1 = date
        	self.date = "\'"+str(date)+"\'"
        	self.builder.get_object("label1").set_text(str(self.date))
        	b3 = self.builder.get_object("button3")
        	b3.connect("clicked",self.delete)
       		print str(self.date)
       		tracker.t3.get("Duedate = %s"%(str(self.date)))
       		if tracker.t3.str1 is not None:
       			print "AAAAAAAA"
       			a = list(tracker.t3.str1)
       			self.builder.get_object("entry1").set_text(str(a[1]))
       			self.builder.get_object("entry2").set_text(str(a[2]))
       			self.builder.get_object("entry3").set_text(str(a[4]))
       
        def save(self,widget):
        
		text1 = ['','','']
		for i in range(3):
			text1[i] = self.builder.get_object("entry%s"%(str(i+1))).get_text()
			
		if text1[0] != '' or text1[1] != '' or text1[2] != '':
			tracker.t3.get("DueDate = %s"%(str(self.date)))
			if tracker.t3.str1 is None:
				tracker.t3.insert(text1[0],text1[1],self.date1,text1[2])
			else:
				tracker.t3.get("DueDate = %s"%(str(self.date)))
				a = list(tracker.t3.str1)
				tracker.t3.update(a[0], CourseId = text1[0], Title = text1[1], DueDate = self.date1, Desc = text1[2])
        	
        	
        def delete(self,widget):
        	tracker.t3.remove1(self.date)	
        	
        def destroy(self,widget):
        	self.d.hide_all()
        	gtk.main_quit()        	
        	
	def display(self):
		self.d.show_all()
		gtk.main()
