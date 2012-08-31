#!/usr/bin/python

import globals
import tracker
import gtk

class Settt:

	def __init__(self):
        	
        	filename = "TimetableEntry.glade"
        	self.builder = gtk.Builder()
       		self.builder.add_from_file(filename)
        	self.d = self.builder.get_object("dialog1")
        	
        	
        	tracker.t1.get("Id = 1")
        	if tracker.t1.str1 is not None:
        		text = ['','','','','','','']
			for k in range (9):
				i = k+10
				tracker.t1.get("Id = %s"%(k+1))
				list1 = list(tracker.t1.str1)
				
				j = 0
				for j in range(7):
					text[j] = list1[j+1]
        			#text[1] = str(text[0]) + '-' + str(text[1])
    				
    				j = 0	
    				for j in range(7):
    					query = "entry%s"%(str(i))
    					self.builder.get_object(query).set_text(str(text[j]))
    					i = i+9
    				
    			        	
    		q = self.builder.get_object("button2")
    		q.connect("clicked",self.save)
        	w = self.builder.get_object("button1")
    		w.connect("clicked",self.destroy)	        	
    			        	
	def save(self,widget):
		
		tracker.t1.get("Id = 1")
		
		if tracker.t1.str1 is None:
			text = ['','','','','','','','']
			for k in range (9):
				j = k+10
				i = 0
				for i in range (7):
					query = "entry%s"%(str(j))
					print query
					text[i] = self.builder.get_object(query).get_text()
					j = j+9
				

				print text[0]
					
				tracker.t1.insert(text[0],text[1],text[2],text[3],text[4],text[5],text[6])
		else:
			text = ['','','','','','','','']
			for k in range (9):
				j = k+10
				i = 0
				for i in range (7):
					text[i] = self.builder.get_object("entry%s"%(str(j))).get_text()
					j = j+9
				#list1 = text[0].split("-")
				tracker.t1.update(k+1, Mon = text[0], Tue = text[1], Wed = text[2], Thu = text[3], Fri = text[4], Sat = text[5], Sun = text[6])
						
	
	def destroy(self,widget):
		self.d.hide_all()
	
	def display(self):
	    	self.d.show_all()
	  
a = Settt()






