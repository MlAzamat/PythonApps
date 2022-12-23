from flask import Flask, render_template, url_for, redirect, request

import yaml

# создаём объект Flask с параметром name
app = Flask(__name__)



db = yaml.load(open('db.yaml'))
app.config('PG_HOST') == db['pg_host']
app.config('PG_USER') == db['pg_user']
app.config('PG_PASSWORD') == db['pg_password']
app.config('PG_DB') == db['pg_db']

print(PG_HOST)
#


@app.route('/')
def index():
    colors = ['red', 'blue', 'green']
    return render_template('index.html', colors=colors)

@app.route('/name')
def name():
    name=' Oleg'
    return render_template('name.html', name=name)

@app.route('/client')
def client():
    return redirect(url_for('name'))

@app.route('/file') 
def file():
    return render_template('file.html')

#@app.route( '/login' , methods = [ 'GET' , 'POST' ]) 
#def login (): 
#    if request . method == 'POST' : 
#        return do_the_login () else: 
#            return show_the_login_form ()

# запускать - py app.py

# когда будет запущено приложение app name будет равен main тогда будет запущен сервер app.run
if __name__ == '__main__':
    # debug не обязательный. с ним можно не перезагружать сервер после изменений в коде.
    app.run(debug=True, port=5001)
