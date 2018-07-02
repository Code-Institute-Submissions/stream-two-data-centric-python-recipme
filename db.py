import os
import pymysql
if os.path.exists('myenviron.py'):
    import myenviron
from datetime import datetime

log_file =  "static/logs/error_log.txt"

class Db():
    def __init__(self, commit=False):
        self.connection = pymysql.connect(host=os.environ.get('DATABASE_URL'), 
                                            port=3306, user=os.environ.get('DATABASE_USER'),
                                            password=os.environ.get('DATABASE_PASSWORD'), 
                                            db=os.environ.get('DATABASE_NAME'))
        self.commit = commit
        if self.commit:
            self.cursor = self.connection.cursor()
        else:
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)

    def __enter__(self):
        return self.cursor
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

class WriteErrorToLog():
    
    def __init__(self, error, message, file, time_stamp):
        self.error = error
        self.message = message
        self.time_stamp = time_stamp
        self.file = file

    def write_to_doc(self):
        log =  (self.error, self.message, self.time_stamp, "\n")

        try:
            with open(self.file, "a") as file:
                file.writelines(" ".join(log))
        except IOError as e:
            print(e)
        else:
            print("{0} has been written to the error log.".format(log))
            
            
        

