from database.DBcm import DBContextManager
from flask import current_app


def select_list(_sql, user_list: list) -> list | None:
    """
    Выполняет параметризованный SQL-запрос.
    :return: список кортежей (может быть пустым) или None, если при работе с БД произошла ошибка
    """
    result = None
    with DBContextManager(current_app.config['db_config']) as cursor: # обозначаем курсор
        if cursor is None: # Есть ли курсор: создан он или нет
            raise ValueError('Курсор не создан') # создаем искусственное исключение, его обработает __exit__
        cursor.execute(_sql, user_list) #вызываем метод
        result = cursor.fetchall() #извлекаем данные и перемещаем в result
    return result # возвращаем результат SQL-запроса
