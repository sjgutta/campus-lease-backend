from campus_lease.settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from playhouse.flask_utils import FlaskDB


class MyFlaskDB(FlaskDB):
    def connect_db(self):
        # Don't connect if already connected (e.g. when raven/sentry does query to DB)
        if self.database.is_closed():
            self.database.connect()


class DBConfig(object):
    DB_NAME = DB_NAME
    DB_USER = DB_USER
    DB_PASSWORD = DB_PASSWORD
    DB_HOST = DB_HOST
    DB_PORT = DB_PORT


db = MyFlaskDB()
