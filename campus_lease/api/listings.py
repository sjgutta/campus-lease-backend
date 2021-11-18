from flask import Blueprint

listings_bp = Blueprint('api', __name__)


# Returns list of all startups
@listings_bp.route('/listings/submit', methods=['POST'])
def add_listing():
    pass


# Returns list of startups with similar names
@listings_bp.route('/listings', methods=['GET'])
def get_startups_name():
    return "Hello!"
