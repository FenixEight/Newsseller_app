import psycopg2
import psycopg2.extensions
from myforum.lib.db.user import UserManager
from myforum.lib.db.letter import LettersManager

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
from psycopg2.pool import ThreadedConnectionPool


class DataService:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.letter = LettersManager(self)
        self.user = UserManager(self)

    def get_connection(self):
        return psycopg2.connect(self.connection_string)
