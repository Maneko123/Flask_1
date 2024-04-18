from flask import Flask
from os.path import join

app = Flask(__name__)


def get_code(name: str):
    filepath = join('static', 'html', name + '.html')
    file = open(filepath, encoding='UTF-8')
    code = file.read()
    file.close()
    del file
    return code


def render_page(nick: str, level: int, raiting: float):
    str_level = str(level)
    str_raiting = str(raiting)
    code = get_code('index_7')
    return code.replace('%NICK%', nick).replace('%LEVEL%', str_level).replace('%RAITING%', str_raiting)


@app.route('/results/<nick>/<int:level>/<float:raiting>')
def results(nick: str, level: int, raiting: int):
    return render_page(nick, level, raiting)


@app.errorhandler(404)
def page_not_found(error):
    return get_code('not_found_7')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
