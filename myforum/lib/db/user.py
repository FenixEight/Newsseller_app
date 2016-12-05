from myforum.lib.db.base import BaseManager
from myforum.model import User


class UserManager(BaseManager):
    def convert_row(self, row):
        u = User()
        u.user_id = row[0]
        u.full_name = row[1]
        u.email = row[2]
        return u

    def get_user(self, id):
        query = '''
        SELECT * FROM users WHERE user_id = %s
        '''
        params = (id,)
        return self.select_one(query,params)

    def users(self):
        query = '''
        SELECT * FROM users
        '''
        return self.select_all(query)

    def add_user(self, full_name, email):
        query = '''
        INSERT INTO users(full_name, email) VALUES(%s, %s)
        '''
        params = (full_name, email,)
        self.execute(query, params)

    def edit_user(self, user_id, full_name, email):
        query = '''
        UPDATE users SET full_name = %s, email = %s WHERE user_id = %s
        '''
        params = (full_name, email, user_id,)
        self.execute(query, params)

    def delete_user(self, user_id):
        query = '''
        DELETE FROM users WHERE user_id = %s
        '''
        params = (user_id,)
        self.execute(query, params)