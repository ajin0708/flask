from flask import Flask,render_template

app= Flask (__name__)

@app.route('/')
def index():
    return render_template('myself.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/song')
def song():
    return render_template('song.html')

@app.route('/BGMI')
def BGMI():
    return render_template('BGMI.html')

@app.route('/base')
def base():
    return render_template('base.html')

if __name__=="main":
    app.run()