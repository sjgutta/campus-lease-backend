from campus_lease.core import db
from peewee import DoesNotExist


class BaseModel(db.Model):
    def save(self, *args, **kwargs):
        super(BaseModel, self).save(*args, **kwargs)

    @classmethod
    def get_or_none(cls, *args, **kwargs):
        try:
            return cls.get(*args, **kwargs)
        except DoesNotExist:
            return None
