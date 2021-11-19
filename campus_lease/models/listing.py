from campus_lease.models.base import BaseModel
from peewee import CharField, TextField


class Listing(BaseModel):
    name = CharField(max_length=255, null=False)
    address = CharField(max_length=255, null=True)
    city = CharField(max_length=255, null=True)
    state = CharField(max_length=255, null=True)
    zip_code = CharField(max_length=255, null=True)
    image_url = CharField(max_length=255, null=True)
    email = CharField(max_length=255, null=True)
    description = TextField(null=True)
    amenities = TextField(null=True)

    @property
    def to_json(self):
        return {
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "image_url": self.email,
            "description": self.description,
            "amenities": self.amenities
        }
