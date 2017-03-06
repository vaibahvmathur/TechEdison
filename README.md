Steps to follow  :

    1)	Open  cmd                                                               CMD  ( command prompt)
    2)	Go to a new_folder		                               					CMD
    3)	Pip install virtualenvwrapper					                        CMD
    4)	Type  mkvirtualenv (Env.. Name)					                        CMD
    5)	Pip install Django==1.10.1						                        CMD
    6)	Open Git Bash and ( go to new_folder path ) and type Git init           GIT BASH
    7)	Git clone https://github.com/vaibahvmathur/TechEdison                   GIT BASH
    8)	change directory to  TechEdison/techapp (project folder)                CMD
    9)  put the Tracking-Log.txt file in TechEdison\techapp folder under name log.txt
    10) cd TechEdision (Project folder) 
    9)	Python manage.py runserver					                             CMD
    10)	Type http://127.0.0.1:8000/techapp/  in webbrowser		                 CMD




Question :
	  
    Create a web application and return the expected results via API.

		1.) Totally how many videos each user has played.

		2.) Totally how many courses each user has enrolled.




Logic :

    1)  read user id ( let be uid ) :
 		      a)  go through json data  
		      b)  if userid = uid and event_name = play_video  
                 than increase play_video_counter by 1  with respect to uid

    2) read user id ( let be uid) :
          a) go through json data
          b) if userid = uid and course id = x  
                 get all unique course id list ( i,e  { uid : [x,y,z] } ) 
                 total course for uid = len( uid_course_list)
 
 
 
                     
Result :  Web Screenshot for graph and POSTMAN API snapshot Added                     
