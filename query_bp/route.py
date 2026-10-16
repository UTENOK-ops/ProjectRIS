from os import path

from flask import Blueprint, abort, render_template, request

from database.sql_provider import SQLProvider
from query_bp.model_route import model_route

blueprint_query = Blueprint('query_bp', __name__, template_folder='templates')
provider = SQLProvider(path.join(path.dirname(__file__), 'sql'))

# Описание параметризованных запросов: все они выполняются по одной схеме
# (форма ввода -> проверка параметров -> SQL-запрос -> таблица с результатом)
QUERIES = {
    'category': {
        'title': 'Товары заданной категории',
        'sql': 'product_by_category.sql',
        'fields': [
            {'name': 'category', 'label': 'Номер категории', 'type': 'number', 'integer': True},
        ],
    },
    'price': {
        'title': 'Товары в заданном диапазоне цен',
        'sql': 'product_by_price.sql',
        'range': True,
        'fields': [
            {'name': 'price_min', 'label': 'Цена от', 'type': 'number'},
            {'name': 'price_max', 'label': 'Цена до', 'type': 'number'},
        ],
    },
    'name': {
        'title': 'Поиск товаров по названию',
        'sql': 'product_by_name.sql',
        'fields': [
            {'name': 'prod_name', 'label': 'Название (или его часть)', 'type': 'text', 'like': True},
        ],
    },
}
HEADERS = ['Название', 'Единица измерения', 'Стоимость']


def get_query(query_name):
    query = QUERIES.get(query_name)
    if query is None:
        abort(404)
    return query


@blueprint_query.route('/', methods=['GET'])
def query_menu():
    return render_template('query_menu.html', queries=QUERIES)


@blueprint_query.route('/<query_name>', methods=['GET'])
def request_handler(query_name):
    query = get_query(query_name)
    return render_template('input_param.html', query_name=query_name, query=query, values={})


@blueprint_query.route('/<query_name>', methods=['POST'])
def result_handler(query_name):
    query = get_query(query_name)
    res_info = model_route(provider, request.form, query)
    if res_info.status:
        return render_template('dynamic.html', prod_title=query['title'],
                               headers=HEADERS, products=res_info.result)
    return render_template('input_param.html', query_name=query_name, query=query,
                           values=request.form, error_message=res_info.error_message)
