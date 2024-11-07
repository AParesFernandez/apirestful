from database.db import get_connection
from .entities.users import Users


class UserModel:

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, email FROM users")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = Users(row[0], row[1], row[2])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user_id(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, email FROM users WHERE id = %s", (id,)
                )
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = Users(row[0], row[1], row[2])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO users (id, nombre, email) 
                    VALUES(%s, %s, %s)""",
                    (user.id, user.nombre, user.email),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s", (user.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE users SET nombre = %s, email = %s
                    WHERE id = %s""",
                    (user.nombre, user.email, user.id)
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
