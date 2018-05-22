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



############# UPLOAD IMAGES ###############################
"""
@app.route('/my_recipme/<username>/add_recipe/upload', methods=['GET', 'POST'])
def upload_photo(username):
    if request.method == 'POST':
        if 'File' not in request.files:
            flash('No file selected')
            return redirect('my_recipme/<username>/add_recipe')
        file = request.files['File']
        if file.filename == '':
            flash('No selected file')
            return redirect('my_recipme/<username>/add_recipe')
        if file and uploads.Upload(file.filename).allowed_file():
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            extension = filename.split('.')
            source = app.config['UPLOAD_FOLDER']+'/%s' % filename
            destination = app.config['UPLOAD_FOLDER']+'/%s' % username + '.' + extension[1]
            os.rename(source, destination )
            new_filename = username + '.' + extension[1]
            print(source, destination)
            print(extension)
            #print(app.config['UPLOAD_FOLDER']+'/%s' % filename)
            #print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/get_photo/%s/%s' % (username, new_filename))
        else:
            flash('Invalid file-type, please upload jpg, png or gif only')
            return redirect('my_recipme/<username>/add_recipe')

@app.route('/get_photo/<username>/<new_filename>')
def retrieve_photo(username, new_filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], new_filename)

"""