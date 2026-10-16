#создаем контекст менеджера
import psycopg2
from psycopg2 import connect


class DBContextManager:
    def __init__(self, db_connect: dict):
        self.conn = None
        self.cursor = None
        self.db_connect = db_connect

    def __enter__(self): #создание объект значение и курсор
        try:
            self.conn = connect(**self.db_connect)
            self.cursor = self.conn.cursor()
            return self.cursor
        except psycopg2.Error as err: #передается, если происходит ошибка в процессе подключения и передается код ошибки
            print(err.pgerror)
            return None # вместо курсора возвращается None

#метод exit
    def __exit__(self, exc_type, exc_val, exc_tb): #упарвление передается, когда выполнены все конструкции, составляющие оператор with
        if exc_type: # Если произошли исключения, то сообщаем о них
            print(exc_type)
            print(exc_val)
        if self.cursor: # создан ли курсор
            if exc_type:
                self.conn.rollback() # И возникли исключения, то откатываемся
            else:
                self.conn.commit() # И не было исключения, то фиксируем изменения
            self.cursor.close()
            self.conn.close()
        return True # исключение обработано, дальше не передается
