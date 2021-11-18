from flask import Flask
from campus_lease.core import db


def create_app(login_manager=None, template_folder=None, static_url_path=None, static_folder=None, testing=False):
    app = Flask("campus_lease", template_folder=template_folder, static_url_path=static_url_path,
                static_folder=static_folder)

    app.config.from_object('campus_lease.settings')

    if testing:
        db_name = app.config['TEST_DB_NAME']
    else:
        db_name = app.config['DB_NAME']

    app.config['DATABASE'] = 'mysql://%s:%s@%s:%s/%s?charset=utf8mb4' % (
        app.config['DB_USER'], app.config['DB_PASSWORD'], app.config['DB_HOST'], app.config['DB_PORT'], db_name
    )

    db.init_app(app)

    if login_manager:
        login_manager.init_app(app)

    return app
