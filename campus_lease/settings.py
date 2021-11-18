import os
from distutils.util import strtobool

DB_HOST = os.environ.get('DB_HOST') or 'localhost'
DB_USER = os.environ.get('DB_USER') or 'root'
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME') or 'troylabs'
DB_PORT = os.environ.get("DB_PORT") or 3306
TEST_DB_NAME = os.environ.get("TEST_DB_NAME") or "troylabs_test"
