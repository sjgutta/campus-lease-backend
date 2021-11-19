from flask import Blueprint, request
from campus_lease.models.listing import Listing

listings_bp = Blueprint('api', __name__)


# Returns list of all startups
@listings_bp.route('/listings/submit', methods=['POST'])
def add_listing():
    data = request.form

    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    state = data.get("state")
    zip_code = data.get("zip_code")
    image_url = data.get("image_url")
    email = data.get("email")
    description = data.get("description")
    amenities = data.get("amenities")

    attributes = [name, address, city, state, zip_code, image_url, email, description, amenities]

    for attribute in attributes:
        if not attribute:
            return {"error": "missing a field!"}

    Listing.create(name=name, address=address, city=city, state=state, zip_code=zip_code, image_url=image_url,
                   email=email, description=description, amenities=amenities)

    return {"success": f"Create listing with name {name}!"}


# Returns list of startups with similar names
@listings_bp.route('/listings', methods=['GET'])
def get_listings():
    listings = Listing.select()
    data = [listing.to_json() for listing in listings]
    return {
        "listings": data
    }
