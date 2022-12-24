from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from db_select import get_student_details

# создаём объект Flask с параметром name
app = Flask(__name__)
Bootstrap(app)


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

@app.route('/css') 
def css():
    return render_template('css.html')

@app.route('/form_db', methods=['GET','POST']) 
def form_db():
    if request.method == 'POST':
        result_select = str(get_student_details(2))
        return render_template('form_db.html', result_select=result_select)
    return render_template('form_db.html', result_select = 'Введите пароль')

@app.route( '/login' , methods = [ 'GET' , 'POST' ]) 
def login(): 
    if request . method == 'POST' : 
        return 'Регистрация успешна'
    return render_template('login.html')

@app.route( '/onlybutton' , methods = [ 'GET' , 'POST' ]) 
def onlybutton(): 
    if request . method == 'POST' : 
        msg = 'Ураа, поехали !!!'
        return render_template('onlybutton.html', msg=msg)
    return render_template('onlybutton.html')

@app.errorhandler(404)
def page_not_found(e):
    #return 'Ooops! this page was not found ;('
    return render_template('error404.html')

# запускать - py app.py

# когда будет запущено приложение app name будет равен main тогда будет запущен сервер app.run
if __name__ == '__main__':
    # debug не обязательный. с ним можно не перезагружать сервер после изменений в коде.
    app.run(debug=True, port=5001)
