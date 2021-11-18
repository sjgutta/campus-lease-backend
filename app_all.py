"""
Run app

Must add entries to HOSTS file, e.g:
127.0.0.1   campuslease.com
127.0.0.1   api.campuslease.com
"""
from campus_lease import create_app
from werkzeug.serving import run_simple


if __name__ == '__main__':
    app = create_app(auto_reload=True)

    run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)
