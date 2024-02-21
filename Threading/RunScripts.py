import os
from subprocess import call
from subprocess import Popen

Popen(['nohup', 'python', 'exampleScripts.py'],
                 stdout=open('null1', 'w'),
                 stderr=open('logfile.log', 'a'),
                 start_new_session=True )
                 
Popen(['nohup', 'python', 'exampleScripts.py'],
                 stdout=open('null2', 'w'),
                 stderr=open('logfile.log', 'a'),
                 start_new_session=True )

Popen(['nohup', 'python', 'exampleScripts.py'],
                 stdout=open('null3', 'w'),
                 stderr=open('logfile.log', 'a'),
                 start_new_session=True )                 


call(['python', 'exampleScripts.py', 'A', '&'])
