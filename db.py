import os
import pymysql
import myenviron
######## TO GO BACK REMOVE THE CONNECTION FROM A SELF INITIALISING class and into s basic class #######
class db():
    def __init__(self, commit=False):
        self.connection = pymysql.connect(host=os.environ.get('DATABASE_HOST'), 
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

