from flask import Flask, render_template, url_for, redirect, request

# создаём объект Flask с параметром name
app = Flask(__name__)

@app.route('/')
def index():
    return "{'id' : 123}"

@app.route('/name')
def name():
    return render_template('name.html')

@app.errorhandler(404)
def page_not_found(e):
    return 'Ooops! this page was not found ;('

if __name__ == '__main__':
    # debug не обязательный. с ним можно не перезагружать сервер после изменений в коде.
    app.run(debug=True, port=5001)
