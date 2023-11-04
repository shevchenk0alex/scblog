from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Алексей'}
    return render_template('index.html', title='Главная', user=user)