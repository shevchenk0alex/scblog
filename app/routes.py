from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Алексей'}
    posts = [
        {
            'author': {'username': 'Вадим'},
            'body': 'Сегодня я распечатал свою коробочку!'
        },
        {
            'author': {'username': 'Миша'},
            'body': 'Я сделал игру на Scratch!'
        }, 
        {
            'author': {'username': 'Иван'},
            'body': 'А я делал конструкции на базе Arduino!'
        }
    ]
    return render_template('index.html', title='Главная', user=user, posts=posts)
    
@app.route('/about')
def about():
    return "Еще не придумали"
    
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Вход', form=form)