from flask import Flask

app = Flask(__name__)
PROMOTION = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']

BOOTSTRAP = ' <link href="https://cdn.jsdelivr.net/npm/bootstrap@5' + \
    '.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha3' + \
    '84-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" cro' + \
    'ssorigin="anonymous">'


@app.route('/')
def root():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '<br/>'.join(PROMOTION)


@app.route('/image_mars')
def image():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Привет, Марс!</title>
    </head>
    <body>
    <h1>Жди нас, Марс!</h1>
    <img src="/static/img/mars.png" width="200""/>
    <p>Вот она какая, красная планета</p>
    </body>
    </html>
    """


@app.route('/promotion_image')
def promotion_image():
    string = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Колонизация</title>
    {BOOTSTRAP}
    <link rel="stylesheet" href="static/css/style.css"/>
    </head>
    <body>
    <h1 class="red-title">Жди нас, Марс!</h1>
    <img src="/static/img/mars.png" width="200" />
    """
    colors = ['secondary', 'success', 'secondary', 'warning', 'danger']
    for text, color in zip(PROMOTION, colors):
        div = f'<div class="alert alert-{color}" role="alert">{text}</div>'
        string += div
    string += '</body>'
    string += '</html>'
    return string


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
