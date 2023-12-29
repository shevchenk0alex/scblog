from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from app.models import User
from flask import request
from urllib.parse import urlsplit

@app.route('/')
@app.route('/index')
@login_required
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
    return render_template('index.html', title='Главная', posts=posts)
    
@app.route('/about')
def about():
    return "Еще не придумали"
    
@app.route('/robo')
@login_required
def robo():
    return "робототехника"
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Такого пользователя не существует или пароль введен неверно')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Поздравляю, теперь вы зарегистрированный пользователь!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)