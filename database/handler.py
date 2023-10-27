import datetime
import hashlib
import random
import typing
import datetime


import mysql.connector

import database.processor
import settings


class Db:
    """Вызывается через with as, берет расписание с sqlite файла shcedule.sql"""

    def __init__(self):
        self.connection = mysql.connector.connect(user=settings.DATABASE['login'],
                                                  host=settings.DATABASE['ip'],
                                                  database=settings.DATABASE['basename'],
                                                  password=settings.DATABASE['password'])
        self.cursor = self.connection.cursor()

    def new_user(self, login: str, password: str) -> bool:
        try:
            self.cursor.execute("INSERT INTO user (`login`, `password`) VALUES (%s, %s)", (login, password))
        except:
            return False
        return True

    def auth_user(self, login: str, password: str) -> str:
        self.cursor.execute("SELECT * FROM user WHERE login=%s AND  password=%s", (login, password))
        hash = None
        if len(self.cursor.fetchall()) > 0:
            hash = hashlib.sha256(str(str(random.randint(0, 999999999999)) + login).encode()).hexdigest()

        self.clear_tokens(login)
        self.cursor.execute('INSERT INTO tokens (`user`, `token`) VALUES (%s, %s)', (login, hash))
        self.connection.commit()
        return hash

    def select_user_from_log_pass(self, login: str, password: str):
        self.cursor.execute("SELECT * FROM user WHERE login=%s AND  password=%s", (login, password))
        return True if len(self.cursor.fetchall()) > 0 else False

    def insert_new_token(self, login: str, hash: str):
        self.cursor.execute('INSERT INTO tokens (`user`, `token`) VALUES (%s, %s)', (login, hash))
        self.connection.commit()

    def clear_tokens(self, login: str) -> bool:
        self.cursor.execute('DELETE FROM `tokens` WHERE `user`=%s', (login,))
        self.connection.commit()
        return True

    def get_user_by_token(self, token: str):
        self.cursor.execute("SELECT * FROM tokens WHERE token=%s", (token,))
        return self.cursor.fetchone()

    def select_user_by_login(self, login: str):
        self.cursor.execute("SELECT * FROM user WHERE login=%s", (login,))
        return self.cursor.fetchone()

    def insert_new_division(self, name: str, hour_work: str, auditoria: str, floor: str, description: str):
        sql = """INSERT INTO `division` (`name`, `hour_work`, `auditoria`, `floor`, `description`) VALUES (%s, %s, %s, %s, %s)"""
        self.cursor.execute(sql, (name, hour_work, auditoria, floor, description,))
        self.connection.commit()
        return True

    def select_division_all(self):
        sql = """SELECT * FROM `division`"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert_new_homework(self, date_homework: datetime, group: str, item: str, homework: str):
        sql = """INSERT INTO `homework` (`date_homework`, `group`, `item`, `homework`) VALUES (%s, %s, %s, %s)"""
        self.cursor.execute(sql, (date_homework, group, item, homework,))
        self.connection.commit()
        return True


    def select_homework_all(self):
        sql = """SELECT * FROM `homework`"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


