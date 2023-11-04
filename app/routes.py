from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Aлексей'}
    return '''
<html>
    <head>
        <title>Главная страница - schoolblog</title>
    </head>
    <body>
        <h1>Привет, ''' + user['username'] + '''!</h1>
    </body>
</html>'''