# ИС «Супермаркет» — Лабораторная работа №1. Работа с запросами

## Структура
```
app.py                     главное меню (/), выход (/exit), регистрация blueprint
data/db_config.json        параметры подключения к БД (app.config['db_config'])
data/supermarket.sql       скрипт создания тестовой таблицы product
database/DBcm.py           контекстный менеджер DBContextManager
database/select.py         select_list — выполнение параметризованного запроса
database/sql_provider.py   SQLProvider — загрузка SQL-файлов
query_bp/route.py          blueprint «Работа с запросами» (/query/...)
query_bp/model_route.py    проверка параметров и выполнение запроса (модель)
query_bp/sql/*.sql         тексты параметризованных запросов
query_bp/templates/        query_menu.html, input_param.html, dynamic.html
templates/                 main_menu.html, exit.html
```

## Маршруты
| URL | Метод | Назначение |
|---|---|---|
| `/` | GET | Главное меню |
| `/exit` | GET | Завершение работы |
| `/query/` | GET | Меню запросов |
| `/query/<query_name>` | GET | Форма ввода параметров |
| `/query/<query_name>` | POST | Выполнение запроса, таблица результата или форма с ошибкой |

## Запуск
```
pip install -r requirements.txt
createdb -U postgres supermarket
psql -U postgres -d supermarket -f data/supermarket.sql
python app.py        # http://127.0.0.1:5001
```
