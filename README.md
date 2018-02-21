## School Management System

I made this project just for fun and to practice my Django skills so far. I also took my time designing the website. I've attached the psd of the Home Page. Here are the details of the project:

* There are teachers, students, and admin.

* Admin holds the right to do and perform each and every CRUD operation while the teachers and students can only change their profile info to a certain extent or only view their information.

* Added the functionality of a profile picture. If you don't assign one, A rice ball image is the default profile picture for everyone in such case.

* Only one teacher can be added to a class and multiple students can be added to a single class.

* Techer can grade the students. Only those subjects will show which are taught in the class the student is currently in.

* Only Admin can add new semesters, subjects and classes.

Well those were the details.

### What i've done so far:

I've done most of the work. I've made all the relavent views and everything for the admin excecpt the roll call view. I will be updating it in a few days. I've enabaled the teacher to be able to grade only his/her's class students.

### What is left:

I still have to make the views for the student. I have yet to make the views for the Roll Calls. I will be updating the full project in about a week.


## To Run The Program:

First use a virtual environment and install everything listed in requirements.txt. The admin email is : "admin@company.com" and the password is: "aaaa1111".

If however you wish to start fresh, just delete the db.sqlite3 file. Then run manage.py migrate and you'll be on your way. However, please note that the program will not work if you delete the migraions. Don't delete the migrations (you can delete the ones ending with .pyc though). I'm sure there's a workaround but seeing my models.py files and going through the trouble of changing them is kinda too scary atm. T_T

p.s This ps is just for my reference don't worry about it.



Feel free to use it any way you like! :D
