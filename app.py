from flask import Flask, request, render_template ,flash, request, redirect, url_for
import cv2
import math
import numpy as np 
import crack
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = os.getcwd()+"\\static\\uploads\\images\\"
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):     
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def rock_paper_scissor():
    
    if request.method == 'POST':
        img = request.files['file']
        
        if 'file' not in request.files:
            flash('Herhangi bir dosya bulunamadı')
            return redirect(request.url)

        file = request.files['file']
        
        if file.filename == '':
            flash('Herhangi bir dosya seçilmemiştir')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            file.save(path)


            
            now = datetime.now()
            current_time = now.strftime("%H-%M-%S")

            resim_adi=f"cikti_{current_time}.png"

            ret = crack.crack(path,resim_adi)
     
            if ret:
                return render_template('result.html',resim_adi=resim_adi)
            else:
                return render_template('result.html',hata="İşlevsel bir problem oluştu")
            
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
