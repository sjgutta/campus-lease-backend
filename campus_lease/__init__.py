from dotenv import load_dotenv
# ensuring that environment variables are set
# this is critical for standalone scripts
load_dotenv()

from werkzeug.middleware.proxy_fix import ProxyFix  # noqa


class SubdomainDispatcher(object):
    def __init__(self, api):
        self.app = api

    def __call__(self, environ, start_response):
        host = environ['HTTP_HOST']
        subdomain = host.split(".")[0]

        if subdomain == "api":
            app = self.app
        else:
            app = self.app

        return app(environ, start_response)


def create_app(auto_reload=False):
    from campus_lease.api import create_app as create_api_app

    app = create_api_app()

    if auto_reload:
        app.jinja_env.auto_reload = True

    app.wsgi_app = SubdomainDispatcher(app.wsgi_app)

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_port=1, x_proto=1)

    return app
