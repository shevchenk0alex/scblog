from app import app
from flask import render_template, flash, redirect, url_for
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
        },
        {
            'author': {'username': 'Снежана'},
            'body': 'А я сегодня не пришла!'
        },
        {
            'author': {'username': 'Илья'},
            'body': 'А у меня день рождения!'
        }
    ]
    return render_template('index.html', title='Главная', user=user, posts=posts)
    
@app.route('/about')
def about():
    return "Еще не придумали"
    
@app.route('/robo')
def robo():
    return "робототехника"
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Вход', form=form)