import os
from flask import Flask, request, redirect, url_for


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

class Upload():
    
    def __init__(self, filename):
        self.filename = filename
    
    def allowed_file(self):
        return '.' in self.filename and \
           self.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

