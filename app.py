import json
from os import path

from flask import Flask, render_template

from query_bp.route import blueprint_query

app = Flask(__name__)

with open(path.join(path.dirname(__file__), 'data', 'db_config.json')) as f: # параметры подключения к БД
    app.config['db_config'] = json.load(f)

app.register_blueprint(blueprint_query, url_prefix='/query')


@app.route('/')
def main_menu():
    return render_template('main_menu.html')


@app.route('/exit')
def exit_func():
    return render_template('exit.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
