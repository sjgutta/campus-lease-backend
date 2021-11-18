# from flask import request, abort
from campus_lease import factory


def register_blueprints(app):
    from campus_lease.api.listings import listings_bp

    app.register_blueprint(listings_bp)

# def enforce_https():
#     if IS_PRODUCTION:
#         if request.url.startswith('http://'):
#             abort(401, description="API requests must be made via https")


def create_app(testing=False):
    api_app = factory.create_app(template_folder="templates/api", testing=testing)

    register_blueprints(api_app)

    # api_app.before_request(enforce_https)
    return api_app
